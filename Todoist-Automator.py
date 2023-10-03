from todoist_api_python.api import TodoistAPI
import webbrowser

# Todoist API token
api = TodoistAPI("Your_Api_Token")

def task():
    print("Welcome to Todoist task automation! ")
    print("What do you want to do? ") 
    print("1. Add new Task")
    print("2. Get Today tasks")
    action = input("> ")
    if action == "1":
        while True:
            try:
                task_title = input("Task Title (type 'exit' to finish adding tasks: ")
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
    elif action == "2":
        try:
            todoist_url = "https://todoist.com/app/today"
            webbrowser.open(todoist_url)
        except Exception as error:
            print(error)
    else:
        print("Invalid input. Please enter 1 or 2 to perform the corresponding action.")

if __name__ == "__main__":
    task()