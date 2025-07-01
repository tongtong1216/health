from typing import Optional, Dict, Any, Union
from .auto_dbcontext import AutoDBContext
from .usrname_to_id import get_user_id

class UserHealthMetricsManager:
    
    @classmethod
    def create_health_metrics(cls, username: str, 
                             heart_rate: Optional[int] = None,
                             blood_pressure: Optional[str] = None,
                             blood_glucose: Optional[Union[float, int]] = None,
                             sleep_duration: Optional[Union[float, int]] = None) -> int:
        """
        创建或更新用户的健康指标记录(存在则更新)
        
        Args:
            username: 关联的用户名
            heart_rate: 心率 (单位：bpm，范围 30-250)
            blood_pressure: 血压 (格式：收缩压/舒张压，如'120/80')
            blood_glucose: 血糖 (单位：mmol/L，范围 0-33.3)
            sleep_duration: 睡眠时长 (单位：小时，范围 0-24)
            
        Returns:
            int: 执行操作受影响的行数
        """
        user_id = get_user_id(username)
        if not user_id:
            return 0  # 用户不存在
            
        # 使用ON DUPLICATE KEY UPDATE处理创建或更新
        query = """
        INSERT INTO user_health_metrics 
            (id, heart_rate, blood_pressure, blood_glucose, sleep_duration)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            heart_rate = VALUES(heart_rate),
            blood_pressure = VALUES(blood_pressure),
            blood_glucose = VALUES(blood_glucose),
            sleep_duration = VALUES(sleep_duration)
        """
        
        blood_glucose = float(blood_glucose) if blood_glucose is not None else None
        sleep_duration = float(sleep_duration) if sleep_duration is not None else None
        
        params = (
            user_id, heart_rate, blood_pressure, 
            blood_glucose, sleep_duration
        )
        
        return AutoDBContext.execute_query(query, params, commit=True)

    @classmethod
    def update_health_metrics(cls, username: str, **updates: Any) -> int:
        """
        更新用户健康指标(部分更新)
        
        Args:
            username: 要更新的用户名
            updates: 要更新的字段和值
                - heart_rate: 心率
                - blood_pressure: 血压
                - blood_glucose: 血糖
                - sleep_duration: 睡眠时长
                
        Returns:
            int: 执行更新操作受影响的行数
        """
        user_id = get_user_id(username)
        if not user_id or not updates:
            return 0
            
        # 动态生成SET子句
        set_clauses = []
        params = []
        valid_fields = {'heart_rate', 'blood_pressure', 'blood_glucose', 'sleep_duration'}
        
        for field, value in updates.items():
            if field in valid_fields:
                # 类型转换确保数据库兼容
                if field in ['blood_glucose', 'sleep_duration'] and value is not None:
                    value = float(value)
                set_clauses.append(f"{field} = %s")
                params.append(value)
        
        if not set_clauses:
            return 0  # 没有有效更新字段
            
        query = f"UPDATE user_health_metrics SET {', '.join(set_clauses)} WHERE id = %s"
        params.append(user_id)
        
        return AutoDBContext.execute_query(query, params, commit=True)

    @classmethod
    def get_health_metrics(cls, username: str) -> Optional[Dict[str, Any]]:
        """
        获取用户健康指标
        
        Args:
            username: 要查询的用户名
            
        Returns:
            Optional[Dict[str, Any]]: 包含健康指标信息的字典，没有记录时返回None
        """
        user_id = get_user_id(username)
        if not user_id:
            return None
            
        query = "SELECT * FROM user_health_metrics WHERE id = %s"
        result = AutoDBContext.execute_query(query, (user_id,))
        return result[0] if result else None