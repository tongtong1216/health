from typing import Optional, Dict, Any, List
from .auto_dbcontext import AutoDBContext
from .usrname_to_id import get_user_id

class UserProfileManager:
    
    @classmethod
    def create_profile(cls, username: str, nickname: str = "新用户", 
                      gender: str = "prefer_not_to_say", birthdate: Optional[str] = None,
                      height: Optional[float] = None, weight: Optional[float] = None,
                      avatar_mime_type: str = "image/jpeg", avatar_base64: Optional[str] = None) -> int:
        """
        创建用户资料记录
        
        Args:
            username: 关联的用户名
            nickname: 用户昵称 (默认: '新用户')
            gender: 性别 ('male', 'female', 'prefer_not_to_say')
            birthdate: 出生日期 (YYYY-MM-DD格式)
            height: 身高(cm)
            weight: 体重(kg)
            avatar_mime_type: 头像MIME类型 (默认: 'image/jpeg')
            avatar_base64: Base64编码的头像数据
            
        Returns:
            int: 执行插入操作受影响的行数(0或1)
        """
        user_id = get_user_id(username)
        if not user_id:
            return 0  # 用户不存在
            
        query = """
        INSERT INTO usr_profile (
            id, nickname, gender, birthdate, height, weight, 
            avatar_mime_type, avatar_base64
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        # 处理日期和数值类型
        params = (
            user_id, nickname, gender, birthdate, height, weight,
            avatar_mime_type, avatar_base64
        )
        
        return AutoDBContext.execute_query(query, params, commit=True)

    @classmethod
    def get_profile(cls, username: str) -> Optional[Dict[str, Any]]:
        """
        根据用户名获取用户资料
        
        Args:
            username: 要查询的用户名
            
        Returns:
            Optional[Dict[str, Any]]: 包含用户资料信息的字典，没有记录时返回None
        """
        user_id = get_user_id(username)
        if not user_id:
            return None
            
        query = "SELECT * FROM usr_profile WHERE id = %s"
        result = AutoDBContext.execute_query(query, (user_id,))
        return result[0] if result else None

    @classmethod
    def update_profile(cls, username: str, **updates: Any) -> int:
        """
        更新用户资料(支持部分更新)
        
        Args:
            username: 要更新的用户名
            updates: 要更新的字段和值 (键值对)
                - nickname: 昵称
                - gender: 性别
                - birthdate: 出生日期(YYYY-MM-DD)
                - height: 身高(cm)
                - weight: 体重(kg)
                - avatar_mime_type: 头像MIME类型
                - avatar_base64: Base64编码的头像数据
                
        Returns:
            int: 执行更新操作受影响的行数
        """
        user_id = get_user_id(username)
        if not user_id or not updates:
            return 0
            
        # 动态生成SET子句
        set_clauses = []
        params = []
        valid_fields = {
            'nickname', 'gender', 'birthdate', 'height', 
            'weight', 'avatar_mime_type', 'avatar_base64'
        }
        
        for field, value in updates.items():
            if field in valid_fields:
                set_clauses.append(f"{field} = %s")
                params.append(value)
        
        if not set_clauses:
            return 0  # 没有有效更新字段
            
        query = f"UPDATE usr_profile SET {', '.join(set_clauses)} WHERE id = %s"
        params.append(user_id)
        
        return AutoDBContext.execute_query(query, params, commit=True)