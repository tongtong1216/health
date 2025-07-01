from  datetime import datetime
from middle.visualization import Visualization
from middle.uplode import Uplode
from middle.register import Register
from data_managers.daily_exercise_manager import DailyExerciseManager

if __name__ == "__main__":
    username = "test2"
    password = "123456"
    today = datetime.today().date()
    type_name = "跑步"
    duration = 30
    foodname = "苹果"
    quantity = 100
    #result = Uplode.uplode_exercise_data(username,type_name,duration)
    #result = Register.register(username,password)
    result = Visualization.today_data(username)
    #result = DailyExerciseManager.get_user_exercise_records(username)
    #result = Uplode.uplode_food_data(username,today,foodname,quantity)
    print(result)