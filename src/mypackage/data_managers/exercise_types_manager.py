from typing import Dict, List, Any, Optional
from .auto_dbcontext import AutoDBContext

class ExerciseTypesManager:
    
    @classmethod
    def get_all_types(cls) -> List[Dict[str, Any]]:
        """
        获取所有运动类型信息（完整字典表）
        
        Returns:
            List[Dict[str, Any]]: 运动类型列表，每个元素包含字段：
                type_id, type_name, type_goal, calorie_factor
        """
        query = "SELECT * FROM exercise_types"
        return AutoDBContext.execute_query(query)
    
    @classmethod
    def get_type_by_id(cls, type_id: int) -> Optional[Dict[str, Any]]:
        """
        根据运动类型ID获取单一运动类型的详细信息
        
        Args:
            type_id: 要查询的运动类型ID(0-255)
                
        Returns:
            Optional[Dict[str, Any]]: 
                - 成功找到记录时返回包含以下键的字典:
                    type_id: 运动类型ID
                    type_name: 运动名称
                    type_goal: 目标运动时长(分钟)
                    calorie_factor: 卡路里计算系数
                - 未找到匹配记录时返回None
        """
            
        query = "SELECT * FROM exercise_types WHERE type_id = %s"
        result = AutoDBContext.execute_query(query, (type_id,))
        return result[0] if result else None


    @classmethod
    def update_type_goal(cls, type_id: int, new_goal: int) -> int:
        """
        更新指定运动类型的目标时长
        
        Args:
            type_id: 要修改的运动类型ID
            new_goal: 新的每日目标运动时长（分钟）
            
        Returns:
            int: 受影响的行数(0表示更新失败)
        """
        
        query = "UPDATE exercise_types SET type_goal = %s WHERE type_id = %s"
        params = (new_goal, type_id)
        
        return AutoDBContext.execute_query(query, params, commit=True)