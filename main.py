from config.__init__ import RED, GREEN, BLUE, YELLOW, MAGENTA, CYAN, RESET 
#----------------------------------------------
from src.core.modules import findStudent, findCourse, findSubject, findTeacher, exportToFile # functions to return data from the database
#----------------------------------------------
import inquirer # for interface
#----------------------------------------------

#comentario pra testar

#mais alteracoes
print("merging?")

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
    
try:
    #loop to keep the program running
    while True:
        #interface for the user to choose what to search	
        function = [
            inquirer.List(
                'choiceOfFunction',
                message="What do you wanna do?",
                choices=['Find student', 'Find course', 'Find subject', 'Find teacher', 'Export to file', 'Exit'],
            ),
        ]

        answersList = inquirer.prompt(function)
        answer = answersList['choiceOfFunction']
        try:
            searches[answer]() #calls the function chosen by the user
        except IndexError as e:
            errorHandling: dict = {
                'Find student': 'No student with that registration number was found',
                'Find course': 'No course with that ID was found',
                'Find subject': 'No subject with that ID was found',
                'Find teacher': 'No teacher with that ID was found'
            }
            print(f"{RED}{errorHandling[answer]} {RESET}")
            continue
        except Exception as e:
            print(f"{RED}Error: {e} {RESET}")
            continue
except Exception as e:
    print(f"{RED}An error has occurred. Please try again. {RESET}")
    exit()

print("merging?")








