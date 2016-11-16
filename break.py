command_list = ['start', 
                'process', 
                'process',
                'process', 
                'stop', 
                'start', 
                'process', 
                'stop']
while command_list:
    command = command_list.pop(0)
    if command == 'stop':
        break
    print(command)