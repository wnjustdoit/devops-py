#!/usr/bin/env python3
import paramiko
from scp import SCPClient


def ssh_cmd(ip, passwd, cmd, username='root'):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, passwd, timeout=5)
        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
            # stdin.write("Y")  # 简单交互，输入 ‘Y’
            out = stdout.readlines()
            # 屏幕输出
            for o in out:
                print(o, )
        print('%s\tOK\n' % (ip))
        ssh.close()
    except:
        print('%s\tSSH Error\n' % (ip))


def scp_cmd(ip, passwd, local_path, remote_path, username='root'):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, passwd, timeout=5)
        scp = SCPClient(ssh.get_transport(), socket_timeout=15)
        scp.put(local_path, remote_path)
        print('%s\tOK\n' % (ip))
        ssh.close()
    except Exception as e:
        print('%s\tSCP Error\n' % (ip), e)
