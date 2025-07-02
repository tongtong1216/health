from middle.visualization import Visualization
from datetime import datetime

if __name__ == '__main__':
    username = "test3"
    today = datetime.today().date()
    #result = Visualization.get_week_exercise_records(username)
    result = Visualization.get_today_food_records(username)
    print(result)
