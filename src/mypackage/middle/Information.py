from typing import Dict, Any, Optional
from ..data_managers.profile_manager import UserProfileManager
from ..data_managers.usrname_to_id import get_user_id
from middle.read_image import read_image

class ProfileEditor:
    @staticmethod
    def edit_profile(username: str, profile_data: Dict[str, Any]) -> bool:
        """
        编辑用户个人信息
        如果用户已有资料则更新，没有则创建新资料
        
        Args:
            username: 用户名
            profile_data: 包含用户资料数据的字典
                - nickname: 昵称 (可选)
                - gender: 性别 ('male', 'female', 'prefer_not_to_say') (可选)
                - birthdate: 出生日期 (YYYY-MM-DD格式) (可选)
                - height: 身高(cm) (可选)
                - weight: 体重(kg) (可选)
                
        Returns:
            bool: 操作是否成功
        """
        # 1. 检查用户是否存在
        user_id = get_user_id(username)
        if not user_id:
            return False
        
        # 2. 检查用户是否已有资料
        existing_profile = UserProfileManager.get_profile(username)
        
        if existing_profile:
            # 3. 已有资料则更新
            return ProfileEditor._update_profile(username, profile_data)
        else:
            # 4. 没有资料则创建
            return ProfileEditor._create_profile(username, profile_data)
    
    
    @staticmethod
    def _create_profile(username: str, profile_data: Dict[str, Any]) -> bool:
        """
        创建新的用户资料
        
        Args:
            username: 用户名
            profile_data: 用户资料数据
            
        Returns:
            bool: 操作是否成功
        """
        # 设置默认值
        nickname = profile_data.get('nickname', "新用户")
        gender = profile_data.get('gender', "prefer_not_to_say")
        birthdate = profile_data.get('birthdate')
        height = profile_data.get('height')
        weight = profile_data.get('weight')
        
        # 处理空字符串为None
        if nickname == "": nickname = "新用户" 
        if gender == "": gender = "prefer_not_to_say"
        if birthdate == "": birthdate = None
        if height == "": height = None
        if weight == "": weight = None
        
        # 调用UserProfileManager创建资料
        result = UserProfileManager.create_profile(
            username=username,
            nickname=nickname,
            gender=gender,
            birthdate=birthdate,
            height=height,
            weight=weight
        )
        
        # 返回值处理：1表示成功，0表示失败
        return result > 0
    
    @staticmethod
    def _update_profile(username: str, updates: Dict[str, Any]) -> bool:
        """
        更新用户资料
        
        Args:
            username: 用户名
            updates: 需要更新的字段
            
        Returns:
            bool: 操作是否成功
        """
        # 过滤有效字段
        valid_updates = {}
        valid_fields = {'nickname', 'gender', 'birthdate', 'height', 'weight', 'avatar_data', 'avatar_mime_type'}
        
        for field, value in updates.items():
            if field in valid_fields and value is not "":
                valid_updates[field] = value
        
        # 如果没有有效更新字段，直接返回成功
        if not valid_updates:
            return True
        
        # 调用UserProfileManager更新资料
        result = UserProfileManager.update_profile(username,**valid_updates)
        
        # 返回值处理：1表示成功，0表示失败
        return result > 0

    @staticmethod
    def get_user_profile(username: str) -> Optional[Dict[str, Any]]:
        """
        获取用户资料信息
        
        Args:
            username: 用户名
            
        Returns:
            Optional[Dict]: 用户资料字典,用户不存在或没有资料时返回None
        """
        profile= UserProfileManager.get_profile(username)
        if profile:
            #将birthdate,weight,height转换为字符串
            profile['birthdate'] = profile['birthdate'].strftime('%Y-%m-%d') if profile['birthdate'] else None
            profile['weight'] = str(profile['weight']) if profile['weight'] is not None else None   
            profile['height'] = str(profile['height']) if profile['height'] is not None else None    
            
    @staticmethod
    def upload_avatar(username: str, image_path: str) -> bool:
        """
        上传用户头像
        
        Args:
            username: 用户名
            image_path: 头像的本地地址
            
        Returns:
            bool: 操作是否成功
        """
        user_id = get_user_id(username)
        if not user_id:
            return False
        
        image = read_image(image_path)
        avatar_data = image['image_data']
        mime_type = image['mime_type']

        return ProfileEditor.edit_profile(
            username,
            {'avatar_data': avatar_data, 'avatar_mime_type': mime_type}
        ) > 0