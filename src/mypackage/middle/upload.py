#上传运动数据
from ..data_managers.daily_exercise_manager import DailyExerciseManager
from ..data_managers.diet_records_manager import DietRecordsManager
from  datetime import datetime

class Upload:

    @staticmethod
    def upload_exercise_data(username:str,typename:str,duration:int) ->int:

        #获取今天日期
        today = datetime.today().date()
        #获取今日的运动记录
        today_exercise_records = DailyExerciseManager.get_user_exercise_records(username,today,today)

        #判断运动时间是否超过一天的时间，超过则返回3
        if duration > 1440:
            return 3
        
        #获取该项运动的总时长
        old_duration = 0
        for item in today_exercise_records:
            if item.get("type_name") == typename:
                old_duration = item["duration"]
                break
        
        now_duration = old_duration + duration
        #创建或更新运动记录,并根据返回值确定操作情况
        result = DailyExerciseManager.create_exercise_record(username,today,typename,now_duration)
        #返回0表示操作失败，返回1表示成功插入新记录，返回2表示成功更新已有记录
        return result
    
    @staticmethod
    def upload_food_data(username:str,foodname:str,quantity: float)->int:

        #获取今天的日期
        today = datetime.today().date()
        #获取今日的饮食记录
        today_food_records = DietRecordsManager.get_user_diet_records(username,today,today)
        #获取该种食物的总摄入量
        old_quantity = 0
        for item in today_food_records:
            if item.get("food_name") == foodname:
                old_quantity = item["quantity"]
                break

        now_quantity = old_quantity + quantity
        #创建或更新饮食记录,并根据返回值确定操作情况
        result = DietRecordsManager.create_diet_record(username,today,foodname,now_quantity)
        #返回0表示操作失败，返回1表示成功插入新记录，返回2表示成功更新已有记录
        return result

