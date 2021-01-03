# Gong
# 录屏
import os
import shlex
import signal
import subprocess

import pytest

# scope="class"：设置他的级别为class，指每个类都能调用；autouse=True：表示主动调用，不用手动调用
# fixture：默认级别是function
# @pytest.fixture(scope="class", autouse=True)
def record():
    # dos窗口命令：scrcpy --record tmp.mp4
    cmd = shlex.split("scrcpy --record tmp.mp4")
    # subprocess：python的子程序，可以执行一段命令；
    # stdout=subprocess.PIPE:希望有标准的输出；stderr=subprocess.STDOUT：希望有错误的输出
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # yield 之前表示在运行之前执行，反之之后
    yield
    # 中断进程
    os.kill(p.pid, signal.CTRL_C_EVENT)