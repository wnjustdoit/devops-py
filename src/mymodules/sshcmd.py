#!/usr/bin/env python3

import paramiko
from scp import SCPClient
import sys


def output(*args, sep=' ', end='\n', file=None):
    print(*args, sep=sep, end=end, file=file)
    sys.stdout.flush()


def ssh_cmd(ip, passwd, cmd, username='root'):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, 22, username, passwd, timeout=5)
        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m, bufsize=1)
            # stdin.close()
            for line in iter(stdout.readline, ''):
                # print('line', line.strip())
                output(line, end="")
        # output('%s\tOK\n' % ip)
        return 'OK'
    except Exception as e:
        output('%s\tSSH Error\n' % ip, e)
        return 'FAILED'
    finally:
        ssh.close()


def scp_cmd(ip, passwd, local_path, remote_path, username='root'):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, 22, username, passwd, timeout=5)
        scp = SCPClient(ssh.get_transport(), socket_timeout=15)
        scp.put(local_path, remote_path, recursive=True)
        # output('%s\tOK\n' % ip)
        return 'OK'
    except Exception as e:
        output('%s\tSCP Error\n' % ip, e)
        return 'FAILED'
    finally:
        ssh.close()
