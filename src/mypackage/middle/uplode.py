#上传运动数据
from data_managers.daily_exercise_manager import DailyExerciseManager
from data_managers.exercise_types_manager import ExerciseTypesManager
from  datetime import datetime

class Uplode:

    @staticmethod
    def uplode_exercise_data(username:str,typename:str,duration:int) ->int:

         #获取今天的日期
        today = datetime.today().date()
        
        #创建或更新运动记录,并根据返回值确定操作情况
        result = DailyExerciseManager.create_exercise_record(username,today,typename,duration)
        return result
