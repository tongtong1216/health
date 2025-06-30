import threading
from mysql.connector import pooling, Error, errorcode
from typing import Any, Dict, Optional, List, Tuple
from .config import DB_CONFIG  # 确保导入路径正确

class AutoDBContext:
    """自动化的数据库连接管理，按需初始化连接池"""
    
    _pool = None
    _lock = threading.Lock()
    _config = None
    
    @classmethod
    def _ensure_initialized(cls, config: Dict[str, Any] = None) -> None:
        """确保连接池已初始化（线程安全）"""
        with cls._lock:
            # 修正连接池健康检查逻辑
            if cls._pool:
                return
            
            pool_config = {
                'pool_name': 'auto_db_pool',
                'pool_size': config.get('pool_size', 5),
                **{k: v for k, v in config.items() if k != 'pool_size'}
            }
            try:
                cls._pool = pooling.MySQLConnectionPool(**pool_config)
            except Error as e:
                cls._pool = None  # 确保失败后状态一致
                raise DatabaseError(f"Connection pool initialization failed: {e}") from e
            cls._config = config
    
    @classmethod
    def execute_query(
        cls,
        query: str,
        params: Tuple[Any, ...] = None,
        commit: bool = False
    ) -> Optional[List[Dict[str, Any]]]:
        """执行SQL查询(按需初始化连接池)"""
        conn, cursor = None, None
        try:
            # 确保连接池已初始化
            cls._ensure_initialized(DB_CONFIG)
            
            conn = cls._pool.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, params or ())
            
            if commit:
                conn.commit()
            
            # 返回查询结果或影响行数
            return cursor.fetchall() if cursor.description else cursor.rowcount
        
        except Error as e:
            raise DatabaseError(f"Query failed: {e}") from e
        finally:
            # 安全释放资源
            if cursor:
                cursor.close()
            if conn:
                conn.close()  # 实际归还连接到连接池

class DatabaseError(Exception):
    """数据库操作异常"""
    pass