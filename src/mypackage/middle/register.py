import bcrypt
from data_managers import UserManager

class Register:
    @staticmethod    
    def register(username: str,password: str) -> int:
        """        注册新用户
        Args:
            username (str): 用户名
            password (str): 密码
        Returns:
            int: 返回值指示注册结果
                1 - 输入为空
                2 - 用户已存在
                3 - 注册失败（其他错误）
                4 - 注册成功
        """

        #验证输入，输入为空时返回1
        if not username or not password:
            return 1
        
        #验证用户是否存在，存在时返回2
        if UserManager.get_user(username) is not None:
            return 2
    
        try:
            #使用bcrypt对密码加密
            password_byte = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(14))
            password_hash = password_byte.decode('utf-8')
            #将用户信息存入数据库，表明注册成功，返回4
            UserManager.create_user(username, password_hash)
            return 4
        #出现其他错误时返回3
        except Exception as e:
            return 3