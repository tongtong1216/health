#可视化
#需实现获取今日运动时间和目标运动时间以及卡路里收支
#需获取一周内的总运动时间和目标运动时间以及总卡路里收支
from  datetime import datetime,timedelta
from data_managers.daily_exercise_manager import DailyExerciseManager
from data_managers.exercise_types_manager import ExerciseTypesManager
from data_managers.diet_records_manager import DietRecordsManager

class Visualization:

    @staticmethod
    def daily_data(username:str,day:datetime.date) -> dict:

        #获取一天运动记录
        daily_exercise_records = DailyExerciseManager.get_user_exercise_records(username,day,day)
        #获取一天的饮食记录
        daily_food_records = DietRecordsManager.get_user_diet_records(username,day,day)
        #没有运动记录时各项数据为0
        total_duration = 0
        total_goal = 0
        total_calories_consumption = 0
        total_calories_intake = 0
        #获取总运动时间
        duration = [d["duration"] for d in daily_exercise_records]
        total_duration = sum(duration)
        #获取总消耗卡路里
        calories_consumption = [d["calories"] for d in daily_exercise_records]   
        total_calories_consumption = sum(calories_consumption)
        #获取总摄入卡路里
        calories_intake = [d["calories"] for d in daily_food_records] 
        total_calories_intake = sum(calories_intake)

        #获取总目标运动时间
        names = [d["type_name"] for d in daily_exercise_records] 
        for name in names:
            type_data = ExerciseTypesManager.get_type_by_name(name)
            total_goal += type_data['type_goal']

        return {
            'total_duration':total_duration,
            'total_goal':total_goal,
            'total_calories_consumption':total_calories_consumption,
            'total_calories_intake':total_calories_intake
        }
    
    @staticmethod
    def today_data(username:str)->dict:
        today = datetime.today().date()
        today_records = Visualization.daily_data(username,today)
        return today_records


    @staticmethod
    def weekly_changes(username:str) ->list:

        #获取查询的日期范围
        today = datetime.today().date()
        start_date = today - timedelta(days=6)
        
        result_list = []
        current_date = start_date
        #获取最近一周内的运动记录
        while current_date <= today:
            current_data = Visualization.daily_data(username,current_date)
            current_duration = current_data['total_duration']
            result_list.append({"date":current_date,"total_duration":current_duration})
            current_date += timedelta(days=1)
        
        return result_list
    
    @staticmethod
    def weekly_data(username:str)->dict:

         #获取查询的日期范围
        today = datetime.today().date()
        start_date = today - timedelta(days=6)

        current_date = start_date
        total_duration = 0
        total_goal = 0
        #获取最近一周内的运动记录
        while current_date <= today:
            current_data = Visualization.daily_data(username,current_date)
            total_duration += current_data['total_duration']
            total_goal += current_data['total_goal']
            current_date += timedelta(days=1)
        
        return {
            'total_duration':total_duration,
            'total_goal':total_goal
        }
       
