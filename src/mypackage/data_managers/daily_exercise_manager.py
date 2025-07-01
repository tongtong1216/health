from typing import Dict, Any, List, Optional, Tuple
from datetime import date
from .auto_dbcontext import AutoDBContext
from .usrname_to_id import get_user_id
from .exercise_types_manager import ExerciseTypesManager

class DailyExerciseManager:
    
    @classmethod
    def create_exercise_record(cls, username: str, exercise_date: date, 
                              type_id: int, duration: int) -> int:
        """
        创建或更新用户每日运动记录(基于唯一索引：用户/日期/类型)
        
        Args:
            username: 关联的用户名
            exercise_date: 运动日期 (格式:YYYY-MM-DD)
            type_id: 运动类型ID (必须有效)
            duration: 运动时长 (分钟，范围 1-1440)
            
        Returns:
            int: 执行操作受影响的行数 (0表示失败)
            
        Note:
            - 使用ON DUPLICATE KEY UPDATE处理相同用户/日期/类型的重复记录
            - 自动计算消耗卡路里（基于运动类型系数）
        """
        # 获取用户ID
        user_id = get_user_id(username)
        if not user_id:
            return 0
            
        # 验证运动类型ID有效性（需实现get_calorie_factor方法）
        calorie_factor = cls.get_calorie_factor(type_id)
        if calorie_factor is None:
            return 0  # 无效的运动类型
            
        # 计算消耗卡路里 = 时长(分钟) * 卡路里系数
        calories = round(duration * calorie_factor)
        
        # 使用ON DUPLICATE KEY UPDATE处理唯一索引冲突
        query = """
        INSERT INTO daily_exercise 
            (usr_id, exercise_date, type_id, duration, calories)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            duration = VALUES(duration),
            calories = VALUES(calories)
        """
        params = (user_id, exercise_date, type_id, duration, calories)
        
        return AutoDBContext.execute_query(query, params, commit=True)

    @classmethod
    def update_exercise_record(cls, record_id: int, duration: Optional[int] = None) -> int:
        """
        更新运动记录(仅支持更新运动时长)
        
        Args:
            record_id: 要更新的记录ID
            duration: 新的运动时长 (分钟，范围 1-1440)
            
        Returns:
            int: 受影响的行数 (0表示失败)
            
        Note:
            - 更新后会自动重新计算消耗卡路里
        """
        if duration is None:
            return 0  # 无有效更新
            
        # 先获取原记录信息
        record = cls.get_exercise_record_by_id(record_id)
        if not record:
            return 0
            
        # 计算新的卡路里消耗值
        calorie_factor = cls.get_calorie_factor(record['type_id'])
        if calorie_factor is None:
            return 0
            
        new_calories = round(duration * calorie_factor)
        
        query = """
        UPDATE daily_exercise 
        SET duration = %s, calories = %s 
        WHERE record_id = %s
        """
        params = (duration, new_calories, record_id)
        
        return AutoDBContext.execute_query(query, params, commit=True)

    # @classmethod
    # def delete_exercise_record(cls, record_id: int) -> int:
    #     """
    #     删除指定的运动记录
        
    #     Args:
    #         record_id: 要删除的记录ID
            
    #     Returns:
    #         int: 受影响的行数 (0表示记录不存在)
    #     """
    #     query = "DELETE FROM daily_exercise WHERE record_id = %s"
    #     return AutoDBContext.execute_query(query, (record_id,), commit=True)

    # @classmethod
    # def get_exercise_record_by_id(cls, record_id: int) -> Optional[Dict[str, Any]]:
    #     """
    #     根据记录ID获取运动记录详情
        
    #     Args:
    #         record_id: 要查询的记录ID
            
    #     Returns:
    #         Optional[Dict]: 包含记录信息的字典,没有记录时返回None
    #     """
    #     query = "SELECT * FROM daily_exercise WHERE record_id = %s"
    #     result = AutoDBContext.execute_query(query, (record_id,))
    #     return result[0] if result else None

    @classmethod
    def get_user_exercise_records(cls, username: str, 
                                 start_date: Optional[date] = None,
                                 end_date: Optional[date] = None) -> List[Dict[str, Any]]:
        """
        获取用户在某时间段内的运动记录
        
        Args:
            username: 要查询的用户名
            start_date: 起始日期 (可选)
            end_date: 结束日期 (可选)
            
        Returns:
            List[Dict]: 运动记录列表，按日期倒序排序
        """
        user_id = get_user_id(username)
        if not user_id:
            return []
            
        # 构建查询条件
        conditions = ["usr_id = %s"]
        params = [user_id]
        
        if start_date and end_date:
            conditions.append("exercise_date BETWEEN %s AND %s")
            params.extend([start_date, end_date])
        elif start_date:
            conditions.append("exercise_date >= %s")
            params.append(start_date)
        elif end_date:
            conditions.append("exercise_date <= %s")
            params.append(end_date)
            
        query = f"""
        SELECT * FROM daily_exercise 
        WHERE {' AND '.join(conditions)}
        ORDER BY exercise_date DESC
        """
        return AutoDBContext.execute_query(query, tuple(params))

    @classmethod
    def get_calorie_factor(cls, type_id: int) -> Optional[float]:
        """
        获取运动类型的卡路里计算系数
        
        Args:
            type_id: 运动类型ID
            
        Returns:
            Optional[float]: 卡路里系数,类型无效时返回None
            
        Note:
            需要实现ExerciseTypesManager类或对应方法
        """
        # 假设从ExerciseTypesManager获取运动类型信息
        # 实际实现需根据项目结构调整

        type_info = ExerciseTypesManager.get_type_by_id(type_id)
        return type_info['calorie_factor'] if type_info else None
    
    @classmethod
    def get_user_records_by_type(cls, username: str, type_id: int,
                                start_date: Optional[date] = None,
                                end_date: Optional[date] = None) -> List[Dict[str, Any]]:
        """
        获取用户在指定运动类型和时间范围内的运动记录
        
        Args:
            username: 要查询的用户名
            type_id: 运动类型ID (必须有效)
            start_date: 起始日期 (可选)
            end_date: 结束日期 (可选)
            
        Returns:
            List[Dict]: 符合条件运动记录列表，按日期倒序排序
            
        Note:
            - 必须提供有效的type_id
            - 时间范围限定仅当同时提供start_date和end_date时生效
            - 如果未提供日期范围，则返回该类型所有记录
        """
        user_id = get_user_id(username)
        if not user_id or not cls.validate_type_id(type_id):
            return []
            
        # 基本条件：用户ID + 类型ID
        conditions = ["usr_id = %s", "type_id = %s"]
        params = [user_id, type_id]
        
        # 添加时间范围条件
        if start_date and end_date:
            conditions.append("exercise_date BETWEEN %s AND %s")
            params.extend([start_date, end_date])
        elif start_date:
            conditions.append("exercise_date >= %s")
            params.append(start_date)
        elif end_date:
            conditions.append("exercise_date <= %s")
            params.append(end_date)
            
        query = f"""
        SELECT * FROM daily_exercise 
        WHERE {' AND '.join(conditions)}
        ORDER BY exercise_date DESC
        """
        return AutoDBContext.execute_query(query, tuple(params))
    
    @classmethod
    def get_weekly_summary(cls, username: str, 
                          year_week: Optional[Tuple[int, int]] = None) -> List[Dict[str, Any]]:
        """
        获取用户周运动汇总数据
        
        Args:
            username: 用户名
            year_week: 可选 - 指定周数 (年份, 周数)，格式如：(2023, 42)
            
        Returns:
            List[Dict]: 周运动汇总列表，包含字段：
                year_week: 年份和周数组合字符串 (格式:202342)
                type_id: 运动类型ID
                total_duration: 该周总运动时长(分钟)
                total_calories: 该周总消耗卡路里
        """
        user_id = get_user_id(username)
        if not user_id:
            return []
            
        conditions = ["usr_id = %s"]
        params = [user_id]
        
        if year_week:
            year, week = year_week
            conditions.append("year_week = %s")
            params.append(f"{year}{week:02d}")
        
        query = f"""
        SELECT 
            year_week, 
            type_id, 
            total_duration, 
            total_calories
        FROM weekly_exercise
        WHERE {' AND '.join(conditions)}
        ORDER BY year_week DESC, type_id
        """
        return AutoDBContext.execute_query(query, tuple(params))
    
    @classmethod
    def get_monthly_summary(cls, username: str, 
                           month: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        获取用户月运动汇总数据
        
        Args:
            username: 用户名
            month: 可选 - 指定月份 (格式: '2023-10')
            
        Returns:
            List[Dict]: 月运动汇总列表，包含字段：
                date_month: 年月 (格式:2023-10)
                type_id: 运动类型ID
                total_duration: 该月总运动时长(分钟)
                total_calories: 该月总消耗卡路里
        """
        user_id = get_user_id(username)
        if not user_id:
            return []
            
        conditions = ["usr_id = %s"]
        params = [user_id]
        
        if month:
            # 验证月份格式 (YYYY-MM)
            if len(month) != 7 or month[4] != '-':
                raise ValueError("月份格式错误，应使用'YYYY-MM'格式")
            conditions.append("date_month = %s")
            params.append(month)
        
        query = f"""
        SELECT 
            date_month, 
            type_id, 
            total_duration, 
            total_calories
        FROM monthly_exercise
        WHERE {' AND '.join(conditions)}
        ORDER BY date_month DESC, type_id
        """
        return AutoDBContext.execute_query(query, tuple(params))