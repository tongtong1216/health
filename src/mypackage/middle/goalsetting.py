from typing import Dict, Optional,Any
from data_managers import *

class GoalManager:
    @staticmethod
    def set_exercise_goal(username: str, exercise_type: str, new_goal: int) -> bool:
        """
        设置或更新用户的运动目标
        
        Args:
            username: 用户名
            exercise_type: 运动类型名称
            new_goal: 新的目标时长（分钟）
            
        Returns:
            bool:操作是否成功
               #tungtungtungsahur   
                     
        """
        
        
        # 3. 验证目标时长有效性 (1-1440分钟)
        if not (1 <= new_goal <= 1440):
            return False
        
        # 4. 更新目标 (使用现有函数)
        result = ExerciseTypesManager.update_type_goal(exercise_type, new_goal)
        
        if result == 1:
            return True
        else:
            return False
    
    @staticmethod
    def get_current_goal(exercise_type: str) -> Dict[str, Any]:
        """
        获取特定运动类型的当前目标
        
        Args:
            exercise_type: 运动类型名称
            
        Returns:
            包含目标信息的字典或错误消息
        """
        exercise_info = ExerciseTypesManager.get_type_by_name(exercise_type)
        if not exercise_info:
            return {'success': False, 'message': f"目标不存在"}
        
        return {
            'exercise_type': exercise_info['type_name'],
            'current_goal': exercise_info['type_goal']
        }
    
    @staticmethod
    def get_all_goals() -> Dict[str, Any]:
        """
        获取所有运动类型的当前目标
        
        Returns:
            包含所有目标信息的字典
        """
        all_types = ExerciseTypesManager.get_all_types()
        goals = {}
        
        for exercise in all_types:
            goals[exercise['type_name']] = {
                'goal': exercise['type_goal']
            }
        
        return {'goals': goals}
    
    @staticmethod
    def update_goal(username: str, new_goal:int) -> int:
        """
        更新用户的总运动目标
        
        Args:
            username: 用户名
            new_goal: 新的总运动目标时长（分钟）
            
        Returns:
            int: 执行更新操作受影响的行数
        """
        return UserProfileManager.update_profile(username=username, total_goal=new_goal)
    