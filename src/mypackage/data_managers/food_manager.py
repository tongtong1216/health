from typing import List, Dict, Optional, Any
from .auto_dbcontext import AutoDBContext

class FoodManager:
    
    @classmethod
    def get_food_by_name(cls, food_name: str) -> Optional[Dict[str, Any]]:
        """
        根据食物ID获取食物详细信息
        
        Args:
            food_name: 食物名称
            
        Returns:
            Optional[Dict]: 食物信息字典，键包括:
                food_id, food_name, calories_per_unit, unit
        """
        query = "SELECT * FROM foods WHERE food_name = %s"
        result = AutoDBContext.execute_query(query, (food_name,))
        return result[0] if result else None

    @classmethod
    def get_food_by_exact_name(cls, food_name: str) -> Optional[Dict[str, Any]]:
        """
        根据完整食物名称获取食物信息
        
        Args:
            food_name: 完整的食物名称
            
        Returns:
            Optional[Dict]: 食物信息字典，未找到返回None
        """
        query = "SELECT * FROM foods WHERE food_name = %s"
        result = AutoDBContext.execute_query(query, (food_name,))
        return result[0] if result else None

    @classmethod
    def get_all_foods(cls) -> List[Dict[str, Any]]:
        """
        获取食品表中所有食物信息
        
        Returns:
            List[Dict]: 包含所有食物信息的列表，每个元素为一个食物字典
                        [
                            {
                                "food_id": 1,
                                "food_name": "苹果",
                                "calories_per_unit": 52.00,
                                "unit": "g"
                            },
                            {
                                "food_id": 2,
                                "food_name": "牛奶",
                                "calories_per_unit": 61.00,
                                "unit": "ml"
                            },
                            ...
                        ]
        """
        query = "SELECT * FROM foods ORDER BY food_name"
        return AutoDBContext.execute_query(query)