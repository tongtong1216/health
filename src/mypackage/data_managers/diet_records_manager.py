from typing import Dict, Any, List, Optional
from datetime import date
from .auto_dbcontext import AutoDBContext
from .food_manager import FoodManager
from .usrname_to_id import get_user_id

class DietRecordsManager:
    
    @classmethod
    def create_diet_record(cls, username: str, intake_date: date, 
                          food_name: str, quantity: float) -> int:
        """
        创建或更新用户饮食记录(基于唯一索引：用户/日期/食物)
        
        Args:
            username: 用户名
            intake_date: 摄入日期 (YYYY-MM-DD)
            food_name: 食物名称 (必须有效)
            quantity: 摄入数量 (范围: 0.1-2000)
            
        Returns:
            int: 执行操作受影响的行数 (0表示失败)
            
        Note:
            - 自动计算卡路里（基于食物单位热量）
            - 处理唯一约束冲突 (用户+日期+食物)
        """
        user_id = get_user_id(username)
        if not user_id:
            return 0  # 用户不存在
            
        # 获取食物信息（含单位热量）
        food_info = cls.get_food_info(food_name)
        if not food_info:
            return 0  # 食物ID无效
            
        # 计算总卡路里 = 摄入量 * 单位热量
        calories = round(quantity * food_info['calories_per_unit'], 1)
        
        # 使用ON DUPLICATE KEY UPDATE处理唯一索引冲突
        query = """
        INSERT INTO diet_records 
            (usr_id, intake_date, food_name, quantity, calories)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            quantity = VALUES(quantity),
            calories = VALUES(calories)
        """
        params = (user_id, intake_date, food_name, quantity, calories)
        
        return AutoDBContext.execute_query(query, params, commit=True)

    @classmethod
    def update_diet_record(cls, record_id: int, quantity: Optional[float] = None) -> int:
        """
        更新饮食记录(仅支持更新摄入量)
        
        Args:
            record_id: 记录ID
            quantity: 新的摄入量 (范围: 0.1-2000)
            
        Returns:
            int: 受影响的行数 (0表示更新失败)
            
        Note:
            - 更新后会自动重新计算卡路里
        """
        if quantity is None:
            return 0  # 无有效更新
            
        # 获取原记录信息
        record = cls.get_record_by_id(record_id)
        if not record:
            return 0
            
        # 获取食物信息（含单位热量）
        food_info = cls.get_food_info(record['food_name'])
        if not food_info:
            return 0
            
        # 重新计算卡路里
        calories = round(quantity * food_info['calories_per_unit'], 1)
        
        query = "UPDATE diet_records SET quantity = %s, calories = %s WHERE record_id = %s"
        params = (quantity, calories, record_id)
        
        return AutoDBContext.execute_query(query, params, commit=True)

    @classmethod
    def get_record_by_id(cls, record_id: int) -> Optional[Dict[str, Any]]:
        """
        根据记录ID获取饮食记录详情
        
        Args:
            record_id: 记录ID
            
        Returns:
            Optional[Dict]: 包含记录信息的字典，没有记录时返回None
        """
        query = "SELECT * FROM diet_records WHERE record_id = %s"
        result = AutoDBContext.execute_query(query, (record_id,))
        return result[0] if result else None

    @classmethod
    def get_user_diet_records(cls, username: str, 
                            start_date: Optional[date] = None,
                            end_date: Optional[date] = None) -> List[Dict[str, Any]]:
        """
        获取用户在某时间段内的饮食记录
        
        Args:
            username: 用户名
            start_date: 起始日期 (可选)
            end_date: 结束日期 (可选)
            
        Returns:
            List[Dict]: 饮食记录列表，按日期倒序排序
        """
        user_id = get_user_id(username)
        if not user_id:
            return []
            
        conditions = ["usr_id = %s"]
        params = [user_id]
        
        if start_date and end_date:
            conditions.append("intake_date BETWEEN %s AND %s")
            params.extend([start_date, end_date])
        elif start_date:
            conditions.append("intake_date >= %s")
            params.append(start_date)
        elif end_date:
            conditions.append("intake_date <= %s")
            params.append(end_date)
            
        query = f"""
        SELECT 
            dr.*, 
            f.food_name,
            f.unit
        FROM diet_records dr
        JOIN foods f ON dr.food_name = f.food_name
        WHERE {' AND '.join(conditions)}
        ORDER BY intake_date DESC
        """
        return AutoDBContext.execute_query(query, tuple(params))

    @classmethod
    def get_food_info(cls, food_name: str) -> Optional[Dict[str, Any]]:
        """
        获取食物详细信息(包含单位热量)
        
        Args:
            food_name: 食物名称
            
        Returns:
            Optional[Dict]: 包含食物信息的字典
                food_id, food_name, calories_per_unit, unit
        """
        
        return FoodManager.get_food_by_name(food_name)