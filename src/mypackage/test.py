from  datetime import datetime
from middle.visualization import Visualization
from middle.upload import Upload
from middle.register import Register
from data_managers.daily_exercise_manager import DailyExerciseManager

if __name__ == "__main__":
    username = "test3"
    password = "123456"
    today = datetime.today().date()
    type_name = ""
    duration = 20
    foodname = "苹果"
    quantity = 100
    #result = Upload.upload_exercise_data(username,type_name,duration)
    #result = Register.register(username,password)
    #result = Visualization.today_data(username)
    #result = DailyExerciseManager.get_user_exercise_records(username)
    #result = Upload.uplode_exercise_data(username,today,foodname,quantity)
    result = DailyExerciseManager.create_exercise_record(username,today,type_name,duration)
    print(result)
