from typing import Optional, Dict, Any
from .auto_dbcontext import AutoDBContext

class UserManager:
    
    @classmethod
    def create_user(cls, username: str, password_hash: str) -> int:
        """
        在数据库中创建新用户(用户名和密码哈希)
        
        Args:
            username: 要创建的用户名(唯一标识)
            password_hash: 用户密码的哈希值(使用bcrypt加密得到)
            
        Returns:
            int: 数据库执行插入操作受影响的行数(成功时通常返回1,失败时返回None)
        """
        query = """
        INSERT INTO usr (usrname, password_hash)
        VALUES  (%s, %s)        
        """
        params = (username, password_hash)
        return AutoDBContext.execute_query(query, params, commit=True)

    @classmethod
    def get_user(cls, username: str) -> Optional[Dict[str, Any]]:
        """
        根据用户名查询用户信息
        
        Args:
            username: 要查询的用户名
            
        Returns:
            Optional[Dict[str, Any]]: 若用户存在,返回包含用户信息的字典(键为数据库字段名,值为对应字段值);
                                    若用户不存在,返回None
        """
        query = "SELECT * FROM usr WHERE usrname = %s"
        result = AutoDBContext.execute_query(query, (username,))
        return result[0] if result else None
    
    @classmethod
    def update_login(cls, user_name: str, success: bool = True) -> int:
        """
        更新用户登录状态(成功/失败)
        
        Args:
            user_name: 要更新登录状态的用户名
            success: 登录是否成功(True表示成功,False表示失败)
            
        Returns:
            int: 数据库执行更新操作受影响的行数(成功时通常返回1,失败时返回None)
            
        Note:
            - 登录成功时会重置失败次数并更新最后登录时间
            - 登录失败时会增加失败次数,当失败次数≥5时设置锁定过期时间为1小时后
        """
        if success:
            query = "UPDATE usr SET last_login = NOW(), failed_attempts = 0 , lock_expires = NULL WHERE usrname = %s"
        else:
            query = """
            UPDATE usr
            SET failed_attempts = failed_attempts + 1,
            lock_expires = IF(failed_attempts >= 5, DATE_ADD(NOW(), INTERVAL  1 HOUR), NULL)
            WHERE usrname = %s  
            """
        return AutoDBContext.execute_query(query, (user_name,), commit=True)
    

    @classmethod
    def update_status(cls, user_name: str, status: str) -> int:
        """
        更新用户状态(如正常/禁用等)
        
        Args:
            user_name: 要更新状态的用户
            status: 新的用户状态 "active" 为活动,"suspended"为暂时封禁中(由于多次登录失败)
            
        Returns:
            int: 数据库执行更新操作受影响的行数(成功时通常返回1,失败时返回None)
        """
        query = "UPDATE usr SET status = %s WHERE usrname = %s"
        return AutoDBContext.execute_query(query, (status, user_name), commit=True)