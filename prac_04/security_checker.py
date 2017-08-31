user_names = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole',
'InterpreterInterface', 'StartServer', 'bob']
valid_input = True
while valid_input:
    user_input = input("Enter your username: ")
    if user_input in user_names:
        print("Access grated")
        valid_input = False
    else:
        print("Access denied")
