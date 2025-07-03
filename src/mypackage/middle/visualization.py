#可视化
#需实现获取今日运动时间和目标运动时间以及卡路里收支
#需获取一周内的总运动时间和目标运动时间以及总卡路里收支
from  datetime import datetime,timedelta
from ..data_managers.daily_exercise_manager import DailyExerciseManager
from ..data_managers.diet_records_manager import DietRecordsManager
from ..data_managers.profile_manager import UserProfileManager

class Visualization:

    @staticmethod
    def daily_data(username:str,day) -> dict:

        #获取一天运动记录
        daily_exercise_records = DailyExerciseManager.get_user_exercise_records(username,day,day)
        #获取一天的饮食记录
        daily_food_records = DietRecordsManager.get_user_diet_records(username,day,day)
        #获取用户基本信息
        user_data = UserProfileManager.get_profile(username)
        #没有运动记录时各项数据为0
        total_duration = 0
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
        total_goal = user_data['total_goal']

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
            date_str = str(current_date)
            result_list.append({"date":date_str,"total_duration":current_duration})
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
    
    @staticmethod
    def get_exercise_records(username,day):

        #获取一天运动记录
        exercise_records = DailyExerciseManager.get_user_exercise_records(username,day,day)
        
        result = [
            {"运动日期":d["exercise_date"],"运动类型":d["type_name"],"运动时间":d["duration"],"卡路里消耗":d['calories']}
            for d in exercise_records
        ]
        return result
    
    #获取今天的运动数据
    @staticmethod
    def get_today_exercise_records(username):
        
        today = datetime.today().date()

        result = Visualization.get_exercise_records(username,today)

        return result
    
    #获取最近一周的运动数据
    @staticmethod
    def get_week_exercise_records(username):
        
        today = datetime.today().date()
        start_date = today - timedelta(days=6)

        result = []
        current_date = start_date

        #获取最近一周内的运动记录
        while current_date <= today:
            current_data = Visualization.get_exercise_records(username,current_date)
            names = [d["运动类型"] for d in current_data]
            if names == []:
                result.append({"运动日期":current_date,"运动类型":"无","运动时间":0,"卡路里消耗":0})
            else:
                for name in names:
                    for item in current_data:
                        if item.get("运动类型") == name:
                            duration = item["运动时间"]
                            calories = item["卡路里消耗"]
                            result.append({"运动日期":current_date,"运动类型":name,"运动时间":duration,"卡路里消耗":calories})
                            break
            current_date += timedelta(days=1)
        
        return result

    @staticmethod
    def get_food_records(username,day):

        food_records = DietRecordsManager.get_user_diet_records(username,day,day)

        result = [
            {"摄入日期":d["intake_date"],"食物名称":d["food_name"],"摄入数量":d["quantity"],"卡路里摄入":d['calories']}
            for d in food_records
        ]

        return result
    
    #获取今天的饮食数据
    @staticmethod
    def get_today_food_records(username):
        
        today = datetime.today().date()

        result = Visualization.get_food_records(username,today)

        return result
    
    @staticmethod
    def get_week_food_records(username):

        today = datetime.today().date()
        start_date = today - timedelta(days=6)

        result = []
        current_date = start_date

        #获取最近一周内的饮食记录
        while current_date <= today:
            current_data = Visualization.get_food_records(username,current_date)
            names = [d["食物名称"] for d in current_data]
            if names == []:
                result.append({"摄入日期":current_date,"食物名称":"无","摄入数量":0,"卡路里摄入":0})
            else:
                for name in names:
                    for item in current_data:
                        if item.get("食物名称") == name:
                            quantity = item["摄入数量"]
                            calories = item["卡路里摄入"]
                            result.append({"摄入日期":current_date,"食物名称":name,"摄入数量":quantity,"卡路里摄入":calories})
                            break
            current_date += timedelta(days=1)
        
        return result