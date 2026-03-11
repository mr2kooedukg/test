#!/bin/bash
# 静态编译 C 程序
# 编译命令：gcc -static env_vars.c -o env_vars
gcc -static env_vars.c -o env_vars

if [ $? -eq 0 ]; then
    echo "编译成功！"
    ls -lh env_vars
else
    echo "编译失败！"
    exit 1
fi