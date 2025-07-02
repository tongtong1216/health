from data_managers.profile_manager import UserProfileManager
from middle.visualization import Visualization
from data_managers.metrics_manager import MetricsManager
from datetime import date
import random

class Health_report:

    @staticmethod
    def health_analysis(username:str)->dict:
        """健康数据分析方法
        :param username: 用户名
        :return:
            dict: 包含用户健康数据分析结果的字典
            {
                'bmi': float, # 体重指数
                'bmi_eval': str, # BMI评估结果
                'exercise_data': int, # 最近一周运动时间总和（分钟）
                'exercise_eval': str, # 运动量评估结果
                'sleep_time': int, # 睡眠时长（分钟）
                'sleep_eval': str, # 睡眠质量评估结果
                'heart_rate': int, # 静息心率
                'heart_eval': str, # 心率状况评估结果
                'bp_data': str, # 血压值（收缩压/舒张压）
                'bp_eval': str, # 血压状况评估结果
                'blood_glucose': float, # 血糖值
                'glucose_eval': str # 血糖状况评估结果
            }
        """
        # 获取用户基本数据
        user_data = UserProfileManager.get_profile(username)
        weight_data = user_data['weight']
        height_data = user_data['height'] / 100 if user_data['height'] else None
        
        # 获取用户近一周运动数据
        exercise_data = Visualization.weekly_data(username)
        # 获取用户健康数据
        health_data = MetricsManager.get_health_metrics(username)
        sleep_time = health_data['sleep_duration']  # 睡眠时长
        heart_rate = health_data['heart_rate']  # 静息心率
        blood_pressure_data = health_data['blood_pressure']  # 血压值（收缩压/舒张压）
        blood_glucose = health_data['blood_glucose']  # 血糖值

        # 血压数据解析
        if blood_pressure_data:
            hbp_data, dbp_data = blood_pressure_data.split('/')
            hbp = int(hbp_data)
            dbp = int(dbp_data)
        else:
            hbp = dbp = None

        # 计算BMI
        if weight_data is None or height_data is None:
            bmi_eval = "无身高或体重记录"
            bmi_round = None
        else:
            bmi = weight_data / (height_data ** 2)
            if bmi < 18.5:
                bmi_eval = "偏瘦"
            elif bmi < 24:
                bmi_eval = "正常"
            elif bmi < 28:
                bmi_eval = "超重"
            else:
                bmi_eval = "肥胖"
            bmi_round = round(bmi, 2)
        
        # 运动量评估
        if exercise_data['total_duration'] < exercise_data['total_goal'] * 0.6:
            exercise_eval = "运动不足"
        elif exercise_data['total_duration'] < exercise_data['total_goal'] * 0.8:
            exercise_eval = "运动适度"
        else:
            exercise_eval = "运动充足"

        # 睡眠质量评估
        if sleep_time is None:
            sleep_eval = "无睡眠记录"
        elif sleep_time < 6 * 60:  # 转换为分钟
            sleep_eval = "睡眠时间不足"
        elif sleep_time <= 9 * 60:
            sleep_eval = "睡眠时间充足"
        else:
            sleep_eval = "睡眠时间过长"

        # 心率状况评估
        if heart_rate is None:
            heart_eval = "无心率数据记录"
        elif heart_rate < 60:
            heart_eval = "心率偏低"
        elif heart_rate <= 100:
            heart_eval = "心率正常"
        else:
            heart_eval = "心率偏高"
        
        # 血压状况评估
        if hbp is None or dbp is None:
            bp_eval = "无血压数据记录"
        elif hbp < 90 or dbp < 60:
            bp_eval = "低血压"
        elif hbp < 120 and dbp < 80:
            bp_eval = "正常"
        elif hbp < 130 and dbp < 80:
            bp_eval = "血压偏高"
        elif hbp < 140 or dbp < 90:
            bp_eval = "高血压1级"
        elif hbp < 180 or dbp < 120:
            bp_eval = "高血压2级"
        else:
            bp_eval = "高血压危象"

        # 血糖状况评估
        if blood_glucose is None:
            glucose_eval = "无血糖记录"
        elif blood_glucose < 3.9:
            glucose_eval = "血糖较低"
        elif blood_glucose <= 6.1:
            glucose_eval = "血糖正常"
        else:
            glucose_eval = "血糖偏高"

        return {
            'bmi': bmi_round,
            'bmi_eval': bmi_eval,
            'exercise_data': exercise_data['total_duration'],
            'exercise_eval': exercise_eval,
            'sleep_time': sleep_time,
            'sleep_eval': sleep_eval,
            'heart_rate': heart_rate,
            'heart_eval': heart_eval,
            'bp_data': blood_pressure_data,
            'bp_eval': bp_eval,
            'blood_glucose': blood_glucose,
            'glucose_eval': glucose_eval
        }

    @staticmethod
    def health_report(username:str)->dict:
        """生成健康报告
        :param username: 用户名
        :return: dict 包含格式化健康报告
        """
        # 获取用户基本数据
        user_data = UserProfileManager.get_profile(username)
        weight_data = user_data['weight']
        height_data = user_data['height']
        gender_data = user_data['gender']
        birthday = user_data['birthdate']
        
        # 处理身高体重数据
        weight = weight_data if weight_data is not None else "未录入"
        height = f"{height_data}厘米" if height_data is not None else "未录入"
        
        # 计算年龄
        if birthday:
            today = date.today()
            age = today.year - birthday.year
        else:
            age = "未录入"
        
        # 处理性别
        gender_map = {"male": "男性", "female": "女性"}
        gender = gender_map.get(gender_data, "未录入")
        
        # 获取健康分析数据
        health_data = Health_report.health_analysis(username)
        
        return {
            '标题': f"{username}健康报告",
            '个人信息': f"年龄: {age}, 性别: {gender}, 身高: {height}, 体重: {weight}千克",
            'bmi评估': f"BMI值 {health_data['bmi'] or '无数据'}, {health_data['bmi_eval']}",
            '运动量评估': f"最近一周锻炼时间: {health_data['exercise_data']}分钟, 运动量评估: {health_data['exercise_eval']}",
            '睡眠情况评估': f"睡眠时间: {health_data['sleep_time'] or '无数据'}分钟, 睡眠情况评估: {health_data['sleep_eval']}",
            '静息心率状况评估': f"静息心率: {health_data['heart_rate'] or '无数据'}, 心率状况评估: {health_data['heart_eval']}",
            '血压状况评估': f"血压值: {health_data['bp_data'] or '无数据'}, 血压状况评估: {health_data['bp_eval']}",
            '血糖状况评估': f"空腹血糖值: {health_data['blood_glucose'] or '无数据'}, 血糖状况评估: {health_data['glucose_eval']}"
        }

    @staticmethod
    def health_tips(username:str)->str:
        """健康建议方法
        :param username: 用户名
        :return: str 健康提示或运动完成状态
        """
        today_data = Visualization.today_data(username)
        duration_status = "未完成"
        
        # 根据目标完成进度设置完成状态
        if today_data['total_duration'] >= today_data['total_goal']:
            duration_status = "已完成"
        elif today_data['total_duration'] >= today_data['total_goal'] * 0.8:
            duration_status = "几乎完成"
        elif today_data['total_duration'] >= today_data['total_goal'] * 0.5:
            duration_status = "已完成一半"

        all_tips = [
            "早睡早起身体好",
            "避免久坐多运动",
            "多吃蔬菜水果，保持均衡饮食",
            "定期体检，及时了解身体状况",
            "保持心情愉悦，心理健康同样重要"
        ]
        
        return random.choice(all_tips) if duration_status == "已完成" else f"今日任务完成情况: {duration_status}"