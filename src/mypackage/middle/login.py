import bcrypt
from data_managers import UserManager
from datetime import datetime
class Login:
    
    @staticmethod
    def login(username:str,password:str) -> int:
        """        用户登录方法
        :param username: 用户名
        :param password: 密码
        :return: 
            1: 输入验证失败（用户名或密码为空）
            2: 用户不存在
            3: 用户被锁定
            4: 密码错误
            5: 其他错误
            6: 登录成功
        """

        #输入验证,当输入用户名或密码为空时返回1
        if not username or not password:
            return 1

        try:
            #获取用户信息
            user_data = UserManager.get_user(username)

            #验证用户是否存在，不存在时返回2
            if user_data is None:
                return 2
            
            #获取用户储存的密码
            db_password = user_data['password_hash']
            
            #检查登录锁定状态，若存在锁定结束时间且没到锁定结束时间则返回3
            now = datetime.now()
            lock_time = user_data['lock_expires']
            if lock_time is not None and now < lock_time:
                return 3

            else:
                #对比输入密码和储存的密码，一致时返回6，不一致时返回4
                if bcrypt.checkpw(password.encode('utf-8'), db_password.encode('utf-8')):
                    UserManager.update_login(username,True)
                    return 6
            
                else:
                    UserManager.update_login(username,False)
                    return 4
        #出现其他错误时返回5
        except Exception as e:
            return 5
        
  