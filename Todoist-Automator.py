# Made By Ranim
from todoist_api_python.api import TodoistAPI
import webbrowser
import inquirer
import pyfiglet 
from colorama import Fore

# Todoist API token
api = TodoistAPI("1f4f4e71f0f9586533c81e42cf3ada217ddc4222")

def display_ascii_art():
    ascii_art = pyfiglet.figlet_format("Todoist Automator")
    print(Fore.RED + ascii_art)
 
def task():
    display_ascii_art()
    questions = [
        inquirer.List('choice',
                      message="Welcome to Todoist task automation!",
                      choices=[
                          ("1. Add new Task", "1"),
                          ("2. Get Today Tasks", "2")
                      ],
                      ), 
    ] 
    answers = inquirer.prompt(questions)
    choice = answers['choice'] 
    if choice == "1":
        while True:
            try:
                task_title = input("Task Title (type 'exit' to finish adding tasks): ")
                if task_title.lower() == "exit":
                    break
                else:
                    due_date= input("Date ('today', 'tomorrow'): ")
                    task_priority = input("Priority('4: Higher --> '1: lower'): ")
                    try:
                        api.add_task(
                            content=task_title,
                            due_string=due_date,
                            due_lang="en",
                            priority=task_priority)
                        print("Task Added successfully!")
                    except Exception as error:
                        print(error)
            except Exception as error:
                print(error)
    elif choice == "2":
        try:
            todoist_url = "https://todoist.com/app/today"
            webbrowser.open(todoist_url)
        except Exception as error:
            print(error)
    else:
        print("Invalid input. Please enter 1 or 2 to perform the corresponding action.")

if __name__ == "__main__":
    task()