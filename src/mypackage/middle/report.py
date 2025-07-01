
from data_managers.profile_manager import UserProfileManager
from middle.visualization import Visualization
from data_managers.metrics_manager import MetricsManagerUserHealth

class Health_report:

    @staticmethod
    def health_report(username:str)->str:

        #获取用户基本数据
        user_data = UserProfileManager.get_profile(username)
        #获取用户近一周运动数据
        exercise_data = Visualization.weekly_data(username)
        #获取用户健康数据
        health_data = MetricsManagerUserHealth.get_health_metrics(username)
        sleep_time = health_data['sleep_duration']#睡眠时长
        heart_rate = health_data['heart_rate']#静息心率
        blood_pressure_data = health_data['blood_pressure']#血压值（收缩压/舒张压）
        blood_glucose = health_data['blood_glucose']#血糖值

        #血压数据解析
        hbp_data ,dbp_data = blood_pressure_data.split('/')
        hbp = int(hbp_data)
        dbp = int(dbp_data)

        #计算BMI
        if user_data['weight'] is None or user_data['height'] is None:
            bmi_eval = "无身高或体重记录"
        bmi = user_data['weight'] / (user_data['height'] ** 2)
        if bmi < 18.5:
            bmi_eval = "偏瘦"
        elif bmi < 24:
            bmi_eval = "正常"
        elif bmi < 28:
            bmi_eval = "超重"
        else:
            bmi_eval = "肥胖"

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
        report = f"{username}健康报告\n"
        report += f"BMI指数:{bmi},{bmi_eval}\n"
        report += f"运动量评估:近一周运动时间为{exercise_data['total_duration']},{exercise_eval}\n"
        report += f"睡眠质量评估:睡眠时间为:{sleep_time},{sleep_eval}\n"
        report += f"心率状况评估:静息心率为:{heart_rate},{heart_eval}\n"
