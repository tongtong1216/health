import bcrypt
from data_managers.user_manager import UserManager

class Register:
    @staticmethod    
    def register(username,password):

        #验证输入
        if not username or not password:
            return 1

        if UserManager.get_user(username) is not None:
            return 2
    
        try:
        #使用bcrypt对密码加密
            password_byte = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(14))
            password_hash = password_byte.decode('utf-8')
        #将用户信息存入数据库
            UserManager.create_user(username, password_hash)
            return 4

        except Exception as e:
            return 3