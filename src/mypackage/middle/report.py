
from data_managers.profile_manager import UserProfileManager
from middle.visualization import Visualization
from data_managers.metrics_manager import MetricsManager
from datetime import date
import random

class Health_report:

    @staticmethod
    def health_analysis(username:str)->dict:

        #获取用户基本数据
        user_data = UserProfileManager.get_profile(username)
        weight_data = user_data['weight']
        height_data = user_data['height'] / 100
        
        #获取用户近一周运动数据
        exercise_data = Visualization.weekly_data(username)
        #获取用户健康数据
        health_data = MetricsManager.get_health_metrics(username)
        sleep_time = health_data['sleep_duration']#睡眠时长
        heart_rate = health_data['heart_rate']#静息心率
        blood_pressure_data = health_data['blood_pressure']#血压值（收缩压/舒张压）
        blood_glucose = health_data['blood_glucose']#血糖值

        #血压数据解析
        hbp_data ,dbp_data = blood_pressure_data.split('/')
        hbp = int(hbp_data)
        dbp = int(dbp_data)

        #计算BMI
        if weight_data is None or height_data is None:
            bmi_eval = "无身高或体重记录"
        bmi = weight_data / (height_data ** 2)
        if bmi < 18.5:
            bmi_eval = "偏瘦"
        elif bmi < 24:
            bmi_eval = "正常"
        elif bmi < 28:
            bmi_eval = "超重"
        else:
            bmi_eval = "肥胖"
        bmi_round = round(bmi,2)
        #运动量评估
        if exercise_data['total_duration'] < exercise_data['total_goal'] *0.6:
            exercise_eval = "运动不足"
        elif exercise_data['total_duration'] < exercise_data['total_goal'] *0.8:
            exercise_eval = "运动适度"
        else:
            exercise_eval = "运动充足"

        #睡眠质量评估
        if sleep_time is None:
            sleep_eval = "无睡眠记录"
        elif sleep_time < 6:
            sleep_eval = "睡眠时间不足"
        elif sleep_time <= 9:
            sleep_eval = "睡眠时间充足"
        else:
            sleep_eval = "睡眠时间过长"

        #心率状况评估
        if heart_rate is None:
            heart_eval = "无心率数据记录"
        if heart_rate < 60:
            heart_eval =  "心率偏低"
        elif heart_rate <= 100:
            heart_eval =  "心率正常"
        else:
            heart_eval =  "心率偏高"
        
        #血压状况评估
        if hbp < 90 or dbp < 60:
            bp_eval = "低血压"
        elif hbp < 120 and dbp  < 80:
            bp_eval = "正常"
        elif hbp < 130 and dbp  < 80:
            bp_eval = "血压偏高"
        elif hbp < 140 or dbp  < 90:
            bp_eval = "高血压1级"
        elif hbp < 180 or dbp  < 120:
            bp_eval = "高血压2级"
        else:
            bp_eval = "高血压危象"

        #血糖状况评估
        if blood_glucose is None:
            glucose_eval = "无血糖记录"
        elif blood_glucose < 3.9:
            glucose_eval = "血糖较低"
        elif blood_glucose <= 6.1:
            glucose_eval = "血糖正常"
        else:
            glucose_eval = "血糖偏高"

        #健康报告生成
        return {
            'bmi':bmi_round,
            'bmi_eval':bmi_eval,
            'exercise_data':exercise_data['total_duration'],
            'exercise_eval':exercise_eval,
            'sleep_time':sleep_time,
            'sleep_eval':sleep_eval,
            'heart_rate':heart_rate,
            'heart_eval':heart_eval,
            'bp_data':blood_pressure_data,
            'bp_eval':bp_eval,
            'blood_glucose':blood_glucose,
            'glucose_eval':glucose_eval
        }
    
    @staticmethod
    def health_report(username:str):

        #获取用户基本数据
        user_data = UserProfileManager.get_profile(username)
        weight_data = user_data['weight']
        height_data = user_data['height'] / 100
        gender_data = user_data['gender']
        birthday = user_data['birthdate']
        #获取身高体重
        if weight_data is None:
            weight = "未录入"
        else:
            weight = weight_data
        if height_data is None:
            height = "未录入"
        else:
            height = height_data
        #计算年龄
        if birthday is None:
            age = "未录入"
        else:
            today = date.today()
            age = today.year - birthday.year

        #解析性别
        if gender_data == "male":
            gender = "男性"
        elif gender_data == "female":
            gender = "女性"
        else:
            gender = "未录入"

        health_data = Health_report.health_analysis(username)
        bmi_round = health_data['bmi']
        bmi_eval = health_data['bmi_eval']
        duration = health_data['exercise_data']
        exercise_eval = health_data['exercise_eval']
        sleep_time = health_data['sleep_time']
        sleep_eval = health_data['sleep_eval']
        heart_rate = health_data['heart_rate']
        heart_eval = health_data['heart_eval']
        blood_pressure_data = health_data['bp_data']
        bp_eval = health_data['bp_eval']
        blood_glucose = health_data['blood_glucose']
        glucose_eval = ['glucose_eval']

        return{
            '标题':f"{username}健康报告",
            '个人信息':f"年龄:{age},性别:{gender},身高:{height}米,体重:{weight}千克",
            'bmi评估':f"BMI值{bmi_round},{bmi_eval}",
            '运动量评估':f"最近一周锻炼时间:{duration},运动量评估:{exercise_eval}",
            '睡眠情况评估':f"睡眠时间:{sleep_time},睡眠情况评估:{sleep_eval}",
            '静息心率状况评估':f"静息心率:{heart_rate},心率状况评估:{heart_eval}",
            '血压状况评估':f"血压值（收缩压/舒张压）:{blood_pressure_data},血压状况评估:{bp_eval}",
            '血糖状况评估':f"空腹血糖值:{blood_glucose},血糖状况评估:{glucose_eval}"
        }

    @staticmethod
    def health_tips(username:str)->str:

        #获取今日的运动数据
        today_data = Visualization.today_data(username)
        #初始化运动时间目标完成状态
        duration_status = "未完成"
        tips = "今天还没开始运动，抓紧时间完成目标吧"
        #根据目标完成进度设置完成状态
        if today_data['total_duration'] >= today_data['total_goal']:
            duration_status = "已完成"
            tips = "恭喜你完成今日目标"
        elif today_data['total_duration'] >= today_data['total_goal'] * 0.8:
            duration_status = "几乎完成"
            tips = "今天目标就要完成了，终点就在眼前"
        elif today_data['total_duration'] >= today_data['total_goal'] * 0.5:
            duration_status = "已完成一半"
            tips = "今天目标已经完成一半了，继续努力"
        
        #获取健康数据
        health_data = Health_report.health_analysis(username)
        sleep_eval = health_data['sleep_eval']
        heart_eval = health_data['heart_eval']
        bp_eval = health_data['bp_eval']
        glucose_eval = ['glucose_eval']
        
        result = {'目标完成状况':f"今日目标{duration_status}。{tips}"}

        if sleep_eval == "睡眠时间不足" or sleep_eval == "睡眠时间过长":
            result['睡眠状况'] = f"今日睡眠状况:{sleep_eval}"
        
        if heart_eval == "心率偏低" or heart_eval == "心率偏高":
            result['心率状况'] = f"今日心率状况:{heart_eval}"
        
        if bp_eval != "正常":
            result['血压状况'] = f"今日血压状况:{bp_eval}"
        
        if glucose_eval == "血糖较低" or glucose_eval == "血糖偏高":
            result['空腹血糖状况'] = f"今日空腹血糖状况:{glucose_eval}"
        
        return result
 
            
        


