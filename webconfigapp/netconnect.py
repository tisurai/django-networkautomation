import environ
import os
from netmiko import ConnectHandler

class nodeconnect:
    env = environ.Env()
    env.read_env(env.str('ENV_PATH', '.env'))
    __username = env('SSH_USERNAME')
    __password = env('SSH_PASSWORD')

    def __init__(self, command):
        self.command = command
        self.connection = None
        self.data = {}

    def get_connect(self):
        device = {
            'device_type': 'cisco_ios',
            'host': '192.168.100.1',
            'username': self.__username,
            'password': self.__password
        }

        self.connection = ConnectHandler(**device)

        show_output = self.connection.send_command(self.command, expect_string=r"#")
        split_output = show_output.splitlines()
        size = len(split_output)
        temp = {}

        for i in range(size):
            if i >= 1:
                linestrip = split_output[i].strip()
                break_line = linestrip.split()
                temp[break_line[0]] = {}
                temp[break_line[0]]['line'] = break_line[1]
                temp[break_line[0]]['protocol'] = break_line[2]
                temp[break_line[0]]['description'] = ' '.join(break_line[3:])
                self.data = temp
                
        return self.data


    def send_config(self, conf_command):

        cfg_list = ["int e0/2", "ip address 192.168.200.1 255.255.255.0", "description Connection to Marketing Switch", "no shut", "do copy run start"]
        cfg_output = connection.send_config_set(cfg_list)
        print(show_output)