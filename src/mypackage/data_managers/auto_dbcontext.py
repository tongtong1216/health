import threading
from mysql.connector import pooling, Error
from typing import Any, Dict, Optional, List, Tuple
from .config import DB_CONFIG

class AutoDBContext:
    """自动化的数据库连接管理，按需初始化连接池"""
    
    # 类级变量存储连接池和配置
    _pool = None
    _lock = threading.Lock()
    _config = None
    
    @classmethod
    def _ensure_initialized(cls, config: Dict[str, Any] = None) -> None:
        """确保连接池已初始化（线程安全）"""
        with cls._lock:
            if cls._pool and cls._pool.pool_is_running():
                return
            
            # 创建连接池
            pool_config = {
                'pool_name': 'auto_db_pool',
                'pool_size': config.get('pool_size', 5),
                **{k: v for k, v in config.items() if k != 'pool_size'}
            }
            cls._pool = pooling.MySQLConnectionPool(**pool_config)
            cls._config = config
    
    @classmethod
    def execute_query(
        cls,
        query: str,
        params: Tuple[Any, ...] = None,
        commit: bool = False
    ) -> Optional[List[Dict[str, Any]]]:
        """执行SQL查询(按需初始化连接池)"""
        try:
            # 确保连接池已初始化
            cls._ensure_initialized(DB_CONFIG)
            
            # 获取连接并执行查询
            conn = cls._pool.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, params or ())
            
            if commit:
                conn.commit()
            
            # 处理结果
            if cursor.description:
                result = cursor.fetchall()
            else:
                result = cursor.rowcount
            
            return result
        
        except Error as e:
            raise DatabaseError(f"Query failed: {e}") from e
        finally:
            # 释放资源
            cursor.close()
            conn.close()  # 实际是归还连接给连接池

class DatabaseError(Exception):
    """数据库操作异常"""
    pass