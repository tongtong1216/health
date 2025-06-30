import bcrypt
from data_managers.user_manager import UserManager
from datetime import datetime
class Login:
    
    @staticmethod
    def login(username:str,password:str):

        #输入验证
        if not username or not password:
            return 1

        try:
            #获取用户信息
            user_data = UserManager.get_user(username)

            if user_data is None:
                return 2
            
            db_password = user_data['password_hash']
            
            #检查登录锁定状态
            now = datetime.now()
            lock_time = user_data['lock_expires']
            if lock_time is not None and now < lock_time:
                return 3

            else:
                if bcrypt.checkpw(password.encode('utf-8'), db_password.encode('utf-8')):
                    UserManager.update_login(username,True)
                    return 6
            
                else:
                    UserManager.update_login(username,False)
                    return 4

        except Exception as e:
            return 5
        
  