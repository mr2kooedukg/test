import os
import platform
import subprocess
import sys

def get_system_info():
    """获取系统信息"""
    info = {
        'os_name': platform.system(),
        'os_version': platform.release(),
        'os_details': platform.platform(),
        'cpu_model': platform.processor(),
        'architecture': platform.architecture()[0],
        'python_version': platform.python_version()
    }
    return info

def print_system_info():
    """打印系统信息"""
    info = get_system_info()
    print("\n" + "=" * 70)
    print("【系统信息】")
    print("=" * 70)
    print(f"操作系统: {info['os_name']}")
    print(f"OS 版本: {info['os_version']}")
    print(f"OS 详情: {info['os_details']}")
    print(f"CPU 型号: {info['cpu_model']}")
    print(f"CPU 架构: {info['architecture']}")
    print(f"Python 版本: {info['python_version']}")
    print("=" * 70)

def print_environment_variables():
    """打印所有环境变量"""
    print("\n" + "=" * 70)
    print("【环境变量】")
    print("=" * 70)
    env_vars = os.environ
    for key in sorted(env_vars.keys()):
        print(f"{key}: {env_vars[key]}")
    print("=" * 70)
    print(f"总共有 {len(env_vars)} 个环境变量")
    print("=" * 70)

def find_wechat_process():
    """查找 WeChat 进程"""
    os_name = platform.system()
    
    try:
        if os_name == "Windows":
            # Windows 系统使用 tasklist 命令
            result = subprocess.run(['tasklist'], capture_output=True, text=True, timeout=5)
            lines = result.stdout.split('\n')
            for line in lines:
                if 'wechat' in line.lower():
                    return line.strip()
        
        elif os_name == "Darwin":
            # macOS 系统使用 ps 命令
            result = subprocess.run(['ps', 'aux'], capture_output=True, text=True, timeout=5)
            lines = result.stdout.split('\n')
            for line in lines:
                if 'wechat' in line.lower() and 'grep' not in line:
                    return line.strip()
        
        elif os_name == "Linux":
            # Linux 系统使用 ps 命令
            result = subprocess.run(['ps', 'aux'], capture_output=True, text=True, timeout=5)
            lines = result.stdout.split('\n')
            for line in lines:
                if 'wechat' in line.lower() and 'grep' not in line:
                    return line.strip()
    
    except Exception as e:
        print(f"执行命令时出错: {e}")
    
    return None

def print_process_list():
    """打印所有进程列表"""
    os_name = platform.system()
    
    print("\n" + "=" * 70)
    print("【当前运行的进程列表】")
    print("=" * 70)
    
    try:
        if os_name == "Windows":
            result = subprocess.run(['tasklist'], capture_output=True, text=True, timeout=5)
            print(result.stdout)
        else:
            result = subprocess.run(['ps', 'aux'], capture_output=True, text=True, timeout=5)
            print(result.stdout)
    except Exception as e:
        print(f"无法列出进程: {e}")
    
    print("=" * 70)

def main():
    """主函数"""
    process_name = "wechat"
    
    print(f"\n正在查找进程: {process_name}")
    proc = find_wechat_process()
    
    if proc:
        # 找到进程，显示详细信息
        print("\n" + "=" * 70)
        print("【WeChat 进程信息】")
        print("=" * 70)
        print(proc)
        print("=" * 70)
    else:
        # 未找到进程，显示错误信息和系统详情
        print("\n" + "=" * 70)
        print("【错误信息】")
        print("=" * 70)
        print(f"❌ 错误: 未找到名叫 '{process_name}' 的进程!")
        print("=" * 70)
        
        # 显示系统信息
        print_system_info()
        
        # 显示环境变量
        print_environment_variables()
        
        # 显示所有正在运行的进程
        print_process_list()
        
        sys.exit(1)

if __name__ == "__main__":
    main()