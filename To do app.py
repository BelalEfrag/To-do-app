#1-Add a task to the list
from pydoc import cli
import colorama
import random
def Main_loob():
    global tasks
    tasks=[]
    while True:
        print(message)
        choice= input("Enter your choice\n:")
        if choice=="1":
            Add_a_task()
        elif choice=="2":
            Mark_a_task()
                
        elif choice=='3':
            View_Tasks()
        elif choice== '4':
            print("Keep finishing your tasks👍❤")    
            break    
        else:
            print("Invalid input pls choose a number from 1 and 4")
            continue
def Add_a_task(): 
        task=input("Enter your task\n:")
        task_info={'task':task,"completed":False}
        tasks.append(task_info)
        print("Your task has been added successfully")
message="""1-Add a task to the list
    2-Mark a task as completed
    3-View tasks
    4-quit""" 
#2-Mark a task as completed
def Mark_a_task():
    while True:
            try:
                incomplete_tasks= [task for task in tasks if task["completed"]==False]
                if len(incomplete_tasks)== 0:
                        print("No tasks to mark or,All task is already marked")
                        return    
                for i, task in enumerate(incomplete_tasks):  
                    print(f"{i+1}- {task['task']}")
                print("-"*30)
                task_number=int(input("Choose a task number to mark:\n"))
                if task_number <=0:
                    print("please choose a positive number")
                incomplete_tasks[task_number - 1]["completed"]=True
                print("Task has been Marked successfuly")
                break
            except  ValueError:
                print("invalid input pls enter a number ")
            except IndexError:
                print("please choose from Available tasks")
            #3-View Tasks
def View_Tasks():
    if len (tasks)==0:
            print("There is no tasks,Try adding a task")
            return
    for i, task in enumerate(tasks):
        if task["completed"]:
            status ='✔'
        else:
            status='❌'
        print(f"{i+1}. {task['task']} {status} ")
        print('-'*30)
Main_loob()
        
            
        
                    
