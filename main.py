from __init__ import RED, GREEN, BLUE, YELLOW, MAGENTA, CYAN, RESET 
#----------------------------------------------
from core.modules import findStudent, findCourse, findSubject, findTeacher, exportToFile # functions to return data from the database
#----------------------------------------------
import inquirer # for interface
#----------------------------------------------



#dictionary with the functions to be called
searches: dict = {
    'Find student': findStudent,
    'Find course': findCourse,
    'Find subject': findSubject,
    'Find teacher': findTeacher,
    'Export to file': exportToFile,
    'Exit': exit
}


#main function
if __name__ == "__main__":


    print(f"""{CYAN}
░  ░░░░  ░░   ░░░  ░░        ░░  ░░░░  ░░░░░░░      ░░░  ░░░░  ░░░      ░░
▒  ▒▒▒▒  ▒▒    ▒▒  ▒▒▒▒▒  ▒▒▒▒▒  ▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒  ▒▒  ▒▒▒  ▒▒▒▒▒▒▒
▓  ▓▓▓▓  ▓▓  ▓  ▓  ▓▓▓▓▓  ▓▓▓▓▓▓  ▓▓  ▓▓▓▓▓▓▓▓      ▓▓▓▓▓    ▓▓▓▓▓      ▓▓
█  ████  ██  ██    █████  ███████    ██████████████  █████  ███████████  █
██      ███  ███   ██        █████  ██████████      ██████  ██████      ██
                        Database Searching CLI{RESET}
""")
    

    #loop to keep the program running
    while True:
        #interface for the user to choose what to search	
        function = [
            inquirer.List(
                'choiceOfFunction',
                message="What do you want to do?",
                choices=['Find student', 'Find course', 'Find subject', 'Find teacher', 'Export to file', 'Exit'],
            ),
        ]

        answersList = inquirer.prompt(function)
        answer = answersList['choiceOfFunction']
        searches[answer]() #calls the function chosen by the user











