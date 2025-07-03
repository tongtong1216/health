from datetime import datetime
from typing import Dict, Any, List, Optional
from .auto_dbcontext import AutoDBContext
from .usrname_to_id import get_user_id

class PostManager:
    
    @staticmethod
    def create_post(username: str, content: str, 
                   image_data: Optional[bytes] = None,
                   mime_type: Optional[str] = None) -> int:
        """
        创建新帖子
        
        Args:
            username: 发帖用户名
            content: 帖子内容 (长度限制取决于前端，但建议不超过5000字符)
            image_data: 可选 - bytes图片数据
            mime_type: 可选 - 图片MIME类型 (当提供图片时必须)
            
        Returns:
            int: 新创建的帖子ID，失败返回0
            
        Raises:
            ValueError: 当提供图片但未提供MIME类型时
        """
        user_id = get_user_id(username)
        if not user_id:
            return 0
            
        # 验证图片和MIME类型
        if image_data and not mime_type:
            raise ValueError("当提供图片时必须指定MIME类型")
            
        # 插入新帖子
        query = """
        INSERT INTO posts (user_id, content, image_data, mime_type)
        VALUES (%s, %s, %s, %s)
        """
        params = (user_id, content, image_data, mime_type)
        
        result = AutoDBContext.execute_query(query, params, commit=True)
        return result if result else 0

    @staticmethod
    def update_post(post_id: int, 
                   new_content: Optional[str] = None,
                   new_image: Optional[bytes] = None,
                   new_mime_type: Optional[str] = None) -> int:
        """
        更新帖子内容或图片
        
        Args:
            post_id: 要更新的帖子ID
            new_content: 可选 - 新的文本内容
            new_image: 可选 - 新的bytes图片数据
            new_mime_type: 可选 - 新图片的MIME类型
            
        Returns:
            int: 受影响的行数 (0表示未更新或更新失败)
            
        Note:
            - 可以单独更新文本或图片，或同时更新两者
            - 传入None保持原值不变
        """
        if not (new_content or new_image or new_mime_type):
            return 0  # 无更新内容
            
        # 动态生成SET子句
        updates = []
        params = []
        
        if new_content is not None:
            updates.append("content = %s")
            params.append(new_content)
            
        if new_image is not None:
            updates.append("image_data = %s")
            params.append(new_image)
            
        if new_mime_type is not None:
            updates.append("mime_type = %s")
            params.append(new_mime_type)
            
        # 如果没有有效更新
        if not updates:
            return 0
            
        query = f"UPDATE posts SET {', '.join(updates)} WHERE post_id = %s"
        params.append(post_id)
        
        return AutoDBContext.execute_query(query, tuple(params), commit=True)

    @staticmethod
    def increment_like_count(post_id: int, increment: int = 1) -> int:
        """
        增加帖子的点赞数
        
        Args:
            post_id: 帖子ID
            increment: 增加的数量 (默认+1，可为负值)
            
        Returns:
            int: 受影响的行数 (0表示帖子不存在)
        """
        query = "UPDATE posts SET like_count = like_count + %s WHERE post_id = %s"
        return AutoDBContext.execute_query(query, (increment, post_id), commit=True)

    @staticmethod
    def delete_post(post_id: int) -> int:
        """
        删除指定帖子
        
        Args:
            post_id: 要删除的帖子ID
            
        Returns:
            int: 受影响的行数 (0表示帖子不存在)
        """
        query = "DELETE FROM posts WHERE post_id = %s"
        return AutoDBContext.execute_query(query, (post_id,), commit=True)

    @staticmethod
    def get_post_by_id(post_id: int, include_image: bool = False) -> Optional[Dict[str, Any]]:
        """
        获取单个帖子的详细信息
        
        Args:
            post_id: 帖子ID
            include_image: 是否包含图片数据 (默认为False)
            
        Returns:
            Optional[Dict]: 帖子详情字典，键包括:
                post_id, created_time, user_id, content, 
                like_count, image_data(可选), mime_type(可选)
        """
        # 根据是否包含图片选择字段
        fields = "post_id, created_time, user_id, content, like_count"
        if include_image:
            fields += ", image_data, mime_type"
            
        query = f"SELECT {fields} FROM posts WHERE post_id = %s"
        result = AutoDBContext.execute_query(query, (post_id,))
        return result[0] if result else None

    @staticmethod
    def get_posts_by_user(username: str, 
                         page: int = 1, per_page: int = 10) -> Dict[str, Any]:
        """
        获取指定用户的所有帖子（分页）
        
        Args:
            username: 用户名
            page: 页码 (从1开始)
            per_page: 每页条数
            
        Returns:
            Dict: 分页结果，包含:
                posts: 帖子列表 (不包含图片数据)
                total: 总帖数
                total_pages: 总页数
                current_page: 当前页码
        """
        user_id = get_user_id(username)
        if not user_id:
            return {'posts': [], 'total': 0, 'total_pages': 0, 'current_page': page}
            
        offset = (page - 1) * per_page
        
        # 主查询：获取当前页帖子 (不含图片)
        data_query = """
        SELECT post_id, created_time, content, like_count
        FROM posts 
        WHERE user_id = %s
        ORDER BY created_time DESC
        LIMIT %s OFFSET %s
        """
        posts = AutoDBContext.execute_query(data_query, (user_id, per_page, offset))
        
        # 计数查询
        count_query = "SELECT COUNT(*) AS total FROM posts WHERE user_id = %s"
        count_result = AutoDBContext.execute_query(count_query, (user_id,))
        total = count_result[0]['total'] if count_result else 0
        
        # 计算总页数
        total_pages = max(1, (total + per_page - 1) // per_page)
        
        return {
            'posts': posts,
            'total': total,
            'total_pages': total_pages,
            'current_page': page
        }

    @staticmethod
    def get_recent_posts(days: int = 7, limit: int = 20) -> List[Dict[str, Any]]:
        """
        获取最近发布的帖子（按时间倒序）
        
        Args:
            days: 时间范围（最近多少天，默认7天）
            limit: 返回的最大帖子数（默认20）
            
        Returns:
            List[Dict]: 帖子列表 (不包含图片数据)
        """
        if days <= 0 or limit <= 0:
            return []
            
        query = """
        SELECT 
            post_id, created_time, user_id, 
            SUBSTRING(content, 1, 100) AS preview, 
            like_count
        FROM posts
        WHERE created_time >= NOW() - INTERVAL %s DAY
        ORDER BY created_time DESC
        LIMIT %s
        """
        return AutoDBContext.execute_query(query, (days, limit))

    @staticmethod
    def get_post_image(post_id: int) -> Optional[Dict[str, Any]]:
        """
        获取帖子的图片数据
        
        Args:
            post_id: 帖子ID
            
        Returns:
            Optional[Dict]: 图片数据字典，格式:
                {
                    'image_data': Base64编码的图片数据,
                    'mime_type': 图片MIME类型
                }
            如果没有图片返回None
        """
        query = "SELECT image_data, mime_type FROM posts WHERE post_id = %s"
        result = AutoDBContext.execute_query(query, (post_id,))
        if not result or not result[0]['image_data']:
            return None
        return result[0]
    
    @staticmethod
    def get_max_id() -> int:
        """
        获取当前帖子表中最大的post_id
        
        Returns:
            int: 最大的post_id，如果表为空则返回0
        """
        query = "SELECT MAX(post_id) AS max_id FROM posts"
        result = AutoDBContext.execute_query(query)
        return result[0]['max_id'] if result and result[0]['max_id'] is not None else 0