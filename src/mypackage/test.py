import bcrypt
from data_managers.user_manager import UserManager
from middle.login import Login

username1 = "test123"
password_str = "123456"
password_byte = password_str.encode('utf-8')
password1 = bcrypt.hashpw(password_byte,bcrypt.gensalt(14))
# UserManager.create_user(username1,password1.decode('utf-8'))

if __name__ == "__main__":
    username = input("请输入用户名")
    password = input("请输入密码")
    result = Login.login(username,password)
    print(result)