from  datetime import datetime
from middle.visualization import Visualization
from middle.upload import Upload
from middle.register import Register
from data_managers.daily_exercise_manager import DailyExerciseManager
from middle.Information import ProfileEditor
from data_managers.metrics_manager import MetricsManager
from middle.report import Health_report
import random
if __name__ == "__main__":
    username = "test3"
    password = "123456"
    today = datetime.today().date()
    type_name = "足球"
    duration = 30
    foodname = "谷薯类"
    quantity = 100
    gender = "male"
    birthdate = "2005-1-1"
    height = 172
    weight = 65
    profile_data = {'nickname':"x",'gender':gender,'birthdate':birthdate,'height':height,'weight':weight}
    #result = Register.register(username,password)
    result = Upload.upload_exercise_data(username,type_name,duration)
    #result = Upload.upload_food_data(username,foodname,quantity)
    #result = Visualization.today_data(username)
    #result = DailyExerciseManager.get_user_exercise_records(username)
    #result = Visualization.weekly_changes(username)
    #result = Visualization.weekly_data(username)
    #result = UserProfileManager.get_profile(username)
    #result = ProfileEditor._create_profile(username,profile_data)
    #result = ProfileEditor.get_user_profile(username)
    #result = MetricsManagerUserHealth.create_health_metrics(username,70,"123/65",4.2,8)
    #result = MetricsManagerUserHealth.get_health_metrics(username)
    #result = Health_report.health_report(username)
    #result = Health_report.health_tips(username)
    print(result)
