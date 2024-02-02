from datetime import datetime
from os import system
from backstage import loadLoop
from time import sleep
from classes import Pochita

pochita = Pochita

# List of Commands
commandList = ['exit', 'cls', 'clear', 'status', 'help']

# Terminal Prompt
def terminalPrompt():
    command = input(str('>>> '))

    if (command == 'cls' or command == 'clear'):
        system('cls')
        terminalPrompt()
    elif (command == 'status'):
        # Printing Pochita's state
        print(f'Pochita has {pochita.age} years, {pochita.lifeMonths} months and {pochita.lifeDays} days of age.')
        print(f'''
[*] Hungry    = {pochita.hungry}/{pochita.maxLimit}
[*] Thirst    = {pochita.thirst}/{pochita.maxLimit}
[*] Energy    = {pochita.energy}/{pochita.maxLimit}
[*] Happiness = {pochita.happiness}/{pochita.maxLimit}
''')
        print(f'Pochita is {pochita.state}')
        terminalPrompt()
    elif (command not in commandList):
        print(f'"{command}" isnt in command list')
        terminalPrompt()
    elif (command == 'help'):
        print(f'{commandList}')
        terminalPrompt()
    elif (command == 'exit'):
        system('cls')

# Clearing the Terminal
system('cls')

if (datetime.now().hour >= 22 and datetime.now().hour <= 6):
    pochita.state = 'awake'
else:
    pochita.state = 'sleeping'

# The code begin here:

loadLoop(4)
sleep(1.5)
print('''
*********************************************
*  ____   ___   ____ _   _ ___ _____  _     *
* |  _ \ / _ \ / ___| | | |_ _|_   _|/ \    *
* | |_) | | | | |   | |_| || |  | | / _ \   *
* |  __/| |_| | |___|  _  || |  | |/ ___ \  *
* |_|    \___/ \____|_| |_|___| |_/_/   \_\ *
*                                           *
* Pochita v0.0.1                            *
*                                           *
*********************************************
''')
sleep(1.5)
terminalPrompt()

#(\___/)
#(=•.•=)
#(")_(")
