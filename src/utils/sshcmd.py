#!/usr/bin/env python3

import paramiko
from scp import SCPClient


def output(*args, sep=' ', end='\n', file=None, flush=True):
    print(*args, sep=sep, end=end, file=file, flush=flush)


def ssh_cmd(ip: str, passwd: str, cmds: list, username: str = 'root', port: int = 22, timeout: int = 5,
            bufsize: int = 1, exec_timeout: int = 120):
    ssh = paramiko.SSHClient()
    try:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port, username, passwd, timeout=timeout)
        for cmd in cmds:
            stdin, stdout, stderr = ssh.exec_command(cmd, bufsize, exec_timeout)
            stdin.close()
            for line in iter(stdout.readline, ''):
                output(line, end="")
            if stdout.channel.recv_exit_status() != 0:
                return stdout.channel.recv_exit_status()
        return 0
    except Exception as e:
        output('%s\tSSH Error\n' % ip, e)
        return -1
    finally:
        ssh.close()


def ssh_cmd_one(ip, passwd, cmd, username='root', port=22, timeout=5, bufsize=1, exec_timeout=120):
    ssh = paramiko.SSHClient()
    try:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port, username, passwd, timeout=timeout)
        stdin, stdout, stderr = ssh.exec_command(cmd, bufsize, exec_timeout)
        stdin.close()
        result_msg = ''
        for line in iter(stdout.readline, ''):
            output(line, end="")
            result_msg += line
        return stdout.channel.recv_exit_status(), result_msg
    except Exception as e:
        output('%s\tSSH Error\n' % ip, e)
        return -1, None
    finally:
        ssh.close()


def scp_cmd(ip, passwd, local_path, remote_path, username='root', port=22, timeout=5, socket_timeout=60,
            recursive=True):
    ssh = paramiko.SSHClient()
    scp = None
    try:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port, username, passwd, timeout=timeout)
        scp = SCPClient(ssh.get_transport(), socket_timeout=socket_timeout)
        scp.put(local_path, remote_path, recursive)
        scp.close()
        return 0
    except Exception as e:
        output('%s\tSCP Error\n' % ip, e)
        return -1
    finally:
        if scp is not None:
            scp.close()
        ssh.close()
