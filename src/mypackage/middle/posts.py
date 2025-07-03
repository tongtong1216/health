import base64
import os
from datetime import datetime
from typing import Dict, List, Optional, Any, Union
from data_managers.posts_manager import PostManager
from data_managers.usrname_to_id import get_user_id
from .read_image import read_image

class PostService:
    @staticmethod
    def create_post(username: str, content: str, 
                   image_path: Optional[str] = None,) -> int:
        """
        创建新帖子
        
        Args:
            username: 发帖用户名
            content: 帖子内容
            image_path: 可选 - 图片路径
            mime_type: 可选 - 图片MIME类型
            
        Returns:
            int: 新创建的帖子ID，失败返回0
        """
        # 验证必填字段
        if not content:
            return 0
        
        # 处理图片数据
        image_data = None
        if image_path:
            try:
                image = read_image(image_path)
                image_data = image['image_data']
                mime_type = image['mime_type']
            except Exception :
                return 0
            
            # 验证MIME类型
            if not mime_type:    #提供图片要有正确的MIME类型
                return 0
        
        try:
            # 调用PostManager创建帖子
            return PostManager.create_post(username, content, image_data, mime_type)
        except ValueError :
            # 如果没有提供MIME类型但提供了图片数据，抛出异常
            print("Error: 提供图片时必须指定MIME类型")
            return 0
        except Exception :
            return 0

    @staticmethod
    def update_post(post_id: int, 
                    new_content: Optional[str] = None,
                    new_image_path: Optional[str] = None,
                    new_mime_type: Optional[str] = None) -> int:
        """
        更新帖子内容或图片
        
        Args:
            post_id: 要更新的帖子ID
            new_content: 可选 - 新的文本内容
            new_image_path: 可选 - 新的Base64图片路径
            new_mime_type: 可选 - 新图片的MIME类型
            
        Returns:
            int: 受影响的行数 (0表示未更新或更新失败)
        """
        # 没有提供任何更新内容
        if not (new_content or new_image_path or new_mime_type):
            return 0
        
        # 处理图片数据
        new_image = None
        if new_image_path:
            try:
                # 将Base64字符串解码为字节数据
                image = read_image(new_image_path)
                new_image = image['image_data']
                new_mime_type = image['mime_type']
            except Exception as e:
                return 0
            
            # 验证MIME类型
            if not new_mime_type:
                return 0
        
        try:
            # 调用PostManager更新帖子
            return PostManager.update_post(post_id, new_content, new_image, new_mime_type)
        except Exception :
            return 0


    @staticmethod
    def increment_like_count(post_id: int, increment: int = 1) -> int:
        """
        增加帖子的点赞数
        
        Args:
            post_id: 帖子ID
            increment: 增加的数量 (默认+1,可为负值)
            
        Returns:
            int: 受影响的行数 (0表示帖子不存在)
        """
        try:
            return PostManager.increment_like_count(post_id, increment)
        except Exception :
            return 0


    @staticmethod
    def delete_post(post_id: int) -> int:
        """
        删除指定帖子
        
        Args:
            post_id: 要删除的帖子ID
            
        Returns:
            int: 受影响的行数 (0表示帖子不存在)
        """
        try:
            return PostManager.delete_post(post_id)
        except Exception :
            return 0

    @staticmethod
    def get_post_by_id(post_id: int, include_image: bool =True ) -> Optional[Dict[str, Any]]:
        """
        获取单个帖子的详细信息
        
        Args:
            post_id: 帖子ID
            include_image: 是否包含图片数据 (默认为False)
            
        Returns:
            Optional[Dict]: 帖子详情字典
        """
        try:
            post = PostManager.get_post_by_id(post_id, include_image)
            post['nickname'] = get_user_id(post['user_id'])
            return post
        except Exception :
            return 0

    @staticmethod
    def get_posts_by_user(username: str) -> Dict[str, Any]:
        """
        获取指定用户的所有帖子（分页）
        
        Args:
            username: 用户名
            page: 页码 (从1开始)
            per_page: 每页条数
            
        Returns:
            Dict: 分页结果
        """
        page = 1
        per_page = 10

        try:
            return PostManager.get_posts_by_user(username, page, per_page)
        except Exception as e:
            return {'posts': [], 'total': 0, 'total_pages': 0, 'current_page': page}

    @staticmethod
    def get_recent_posts(days: int = 7, limit: int = 20) -> List[Dict[str, Any]]:
        """
        获取最近发布的帖子（按时间倒序）
        
        Args:
            days: 时间范围(最近多少天,默认7天)
            limit: 返回的最大帖子数(默认20)
            
        Returns:
            List[Dict]: 帖子列表 (不包含图片数据)
        """
        try:
            return PostManager.get_recent_posts(days, limit)
        except Exception :
            return []

    @staticmethod
    def get_post_image(post_id: int) -> Optional[bytes]:
        """
        获取帖子的图片数据
        
        Args:
            post_id: 帖子ID
            
        Returns:
            Optional[Dict]: 图片数据字典
        """
        try:
            # 获取帖子图片信息
            image_info = PostManager.get_post_image(post_id)
            if not image_info or 'image_data' not in image_info:
                return None
            
            # 返回图片字节数据
            image_bytes = image_info['image_data']
            if image_bytes:
                return image_bytes
        except Exception :
            return None

    @staticmethod
    def get_max_post_id() -> int:
        """
        获取当前最大的帖子ID
        
        Returns:
            int: 最大帖子ID，若无帖子则返回0
        """
        try:
            return PostManager.get_max_id()
        except Exception :
            return 0