#上传运动数据
from data_managers.daily_exercise_manager import DailyExerciseManager
from data_managers.diet_records_manager import DietRecordsManager
from  datetime import datetime

class Uplode:

    @staticmethod
    def uplode_exercise_data(username:str,typename:str,duration:int) ->int:

        #获取今天的日期
        today = datetime.today().date()
        
        #创建或更新运动记录,并根据返回值确定操作情况
        result = DailyExerciseManager.create_exercise_record(username,today,typename,duration)
        return result
    
    @staticmethod
    def uplode_food_data(username:str,intake_date:datetime.date,foodname:str,quantity: float)->int:

        #获取今天的日期
        today = datetime.today().date()

        #创建或更新饮食记录,并根据返回值确定操作情况
        result = DietRecordsManager.create_diet_record(username,today,foodname,quantity)
        return result

