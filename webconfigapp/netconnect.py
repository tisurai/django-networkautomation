import os
from netmiko import ConnectHandler

ssh_uname = 'cisco'
ssh_pwd = 'strongsshpassword'
connection = None

device = {
    'device_type': 'cisco_ios',
    'host': '192.168.100.1',
    'username': ssh_uname,
    'password': ssh_pwd
}

connection = ConnectHandler(**device)

show_output = connection.send_command("show int descr")
print(show_output)

cfg_list = ["int e0/2", "ip address 192.168.200.1 255.255.255.0", "description Connection to Marketing Switch", "no shut", "do copy run start"]
cfg_output = connection.send_config_set(cfg_list)
print(show_output)