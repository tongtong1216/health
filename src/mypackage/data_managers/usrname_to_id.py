from .auto_dbcontext import AutoDBContext

def get_user_id(username: str) -> int:
    """
    获取用户ID的公共服务
    
    Args:
        username: 用户名
        
    Returns:
        int: 用户ID
        
    Raises:
        ValueError: 用户不存在时
    """
    query = "SELECT id FROM usr WHERE usrname = %s"
    result = AutoDBContext.execute_query(query, (username,))
    
    if not result:
        raise ValueError(f"用户 '{username}' 不存在")
    return result[0]["id"]