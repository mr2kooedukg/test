import os

def print_environment_variables():
    """
    采集并打印当前进程的所有环境变量
    """
    print("=" * 60)
    print("当前进程的环境变量：")
    print("=" * 60)
    
    # 获取所有环境变量
    env_vars = os.environ
    
    # 按字母顺序排序并打印
    for key in sorted(env_vars.keys()):
        print(f"{key}: {env_vars[key]}")
    
    print("=" * 60)
    print(f"总共有 {len(env_vars)} 个环境变量")
    print("=" * 60)

def get_specific_env_vars():
    """
    获取一些常用的环境变量
    """
    print("\n常用环境变量：")
    print("=" * 60)
    
    common_vars = [
        'PATH',
        'HOME',
        'USER',
        'SHELL',
        'LANG',
        'PWD',
        'JAVA_HOME',
        'PYTHON_HOME',
        'GOPATH',
        'GOROOT'
    ]
    
    for var in common_vars:
        value = os.environ.get(var, '未设置')
        print(f"{var}: {value}")
    
    print("=" * 60)

if __name__ == "__main__":
    # 打印所有环境变量
    print_environment_variables()
    
    # 打印常用环境变量
    get_specific_env_vars()