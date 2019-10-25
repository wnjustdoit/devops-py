#!/usr/bin/env python3

import paramiko
from scp import SCPClient


def ssh_cmd(ip, passwd, cmd, username='root'):
    print('==================================================')
    print('==================================================')
    print('==================================================')
    print('==================================================')
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, passwd, timeout=5)
        for m in cmd:
            print('============start execute.........')
            stdin, stdout, stderr = ssh.exec_command(m)
            print('============get  execute result.........')
            # stdin.write("Y")  # 简单交互，输入 ‘Y’
            stdin.close()
            # out = stdout.readlines()
            # 屏幕输出
            # for o in out:
            #     print(o, )

            # for line in line_buffered(stdout):
            #     print(line)

            # for line in iter(stdout.readline, ""):
            #     print(line, end="")

            for line in iter(lambda: stdout.readline(2048), ""):
                print(line, end="")
            print('finished.')
        print('%s\tOK\n' % (ip))
        ssh.close()
    except Exception as e:
        print('%s\tSSH Error\n' % (ip), e)


def line_buffered(f):
    line_buf = ""
    while not f.channel.exit_status_ready():
        line_buf += str(f.read(1))
        print('line_buf--------', line_buf)
        if line_buf.endswith('\n'):
            yield line_buf
            line_buf = ''
    return line_buf


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
