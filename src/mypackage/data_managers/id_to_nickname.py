from .auto_dbcontext import AutoDBContext

def id_to_nickname(user_id: int) -> str:
    """
    获取用户名的公共服务
    
    Args:
        user_id: 用户ID
        
    Returns:
        str: 用户名
        
    Raises:
        ValueError: 用户不存在时
    """
    query = "SELECT nickname FROM usr_profile WHERE id = %s"
    result = AutoDBContext.execute_query(query, (user_id,))
    
    if not result:
        raise ValueError(f"用户ID '{user_id}' 不存在")
    return result[0]["nickname"]