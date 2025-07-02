import os

def read_image(image_path: str) -> dict:
    """
    
    
    参数:
        image_path (str): 本地图片文件的完整路径
        
    返回:
        dict: 包含图片数据和MIME类型的字典
            - 'image_data': bytes类型的图片数据
            - 'mime_type': str类型的MIME类型
        
    异常:
        会抛出FileNotFoundError、IOError等异常
    """
    # 1. 验证文件存在性
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"图片文件不存在: {image_path}")
    
    # 2. 检查文件大小（示例限制为10MB）
    max_size = 10 * 1024 * 1024  # 10MB
    file_size = os.path.getsize(image_path)
    if file_size > max_size:
        raise ValueError(f"图片大小超过限制 ({file_size/1024/1024:.2f}MB > {max_size/1024/1024}MB)")
    
    # 3. 读取图片文件到二进制
    try:
        with open(image_path, 'rb') as file:
            image_data = file.read()
    except IOError as e:
        raise IOError(f"读取图片失败: {e}") from e
    
    # 4. 获取MIME类型（根据扩展名简单判断）
    mime_type = "application/octet-stream"
    ext = os.path.splitext(image_path)[1].lower()
    if ext == '.jpg' or ext == '.jpeg':
        mime_type = 'image/jpeg'
    elif ext == '.png':
        mime_type = 'image/png'
    elif ext == '.gif':
        mime_type = 'image/gif'
    
    return {'image_data': image_data, 'mime_type': mime_type}
