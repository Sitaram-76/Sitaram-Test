host = "192.168.50.92"
port = 22
username = "vivint"
password = "p@ssw0rd"
command = "ls"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
print(lines)
