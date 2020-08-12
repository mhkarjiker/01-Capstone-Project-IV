
#This program is a task manager for a small business and allows the user
#to add and assign tasks to users, as well as add new users


#=========Functions==============================================

        

#======== User Login ============================================

#read the use.txt
username_reg = []
password_reg = []
username_list = []
password_list = []

with open('user.txt', 'r+') as f:           #open user.txt
    for line in f:                          #Now we reading user.txt
        line = line.replace(" ", "")        #replace space before password with no space
        line = line.replace("\n", "")       #remove the next line character as this will take a space in the list
        line = line.split(",")              #separate user name and password
        username_reg = line[0]
        password_reg = line[1]
        username_list.append(username_reg)
        password_list.append(password_reg)

print(username_list)
print(password_list)
print(len(username_list))
username = input("Please enter username: ")
password = input("Please enter password: ")

#Create a function called Main_Menu() to help call when keystroke "-1" refer to VM

i = 0; login = 0 #Here login is like a flag. Which get the value 1 once the login is successful else stays 0.
while i < len(username_list):
    if username == str(username_list[i]) and password == str(password_list[i]):
        login = 1
        if username == "admin":
            selection = input('''Please select one of the following options:
                             r - register user
                             a - add task
                             va - view all tasks
                             vm - view my tasks
                             gr - generate reports
                             ds - display statistics
                             e - exit\n''')
        else:
            selection = input('''Please select one of the following options:
                             a - add task
                             va - view all tasks
                             vm - view my tasks
                             e - exit\n''')
            
        break
    i+=1
    if i==len(username_list) and login == 0:
        print("invalid username or password")   
        username = input("Please enter username: ")
        password = input("Please enter password: ")
        i = 0

#=============FUNCTIONS========================================

##============Register User Function===========================
def reg_user():
        if username == "admin":
            print("Register User")
            new_user = input("Please enter username: ")
            i = 0
            while i < len(username_list):
                while new_user == str(username_list[i]):
                    print("Username already exists")
                    new_user = input("Please enter username: ")
                i+=1
            password = input("Please enter password: ")
            cpassword = input("Please confirm password: ")
            while password != cpassword:
                print("passwords do not match")
                password = input("Please enter password: ")
                cpassword = input("Please confirm password: ")
            if password == cpassword:
                with open ('user.txt', 'a') as f:
                    f.write("\n" + new_user + ", "+ password)      #append user name and password to user.txt
                    print(f"User '{new_user}' successfully added")
        else:
            print("You do not have adminstrative rights")

##===========Add New Task Function===============================
def add_task():
        from datetime import datetime
        username = input("Enter username to be assigned to task: ")
        task_title = input("Task title: ")
        task_descr = input("Task description: ")
        ddate = input("Due date: ")
        #today = datetime.now()
        today = str(datetime.now().strftime("%d %b %Y")) #How do I get the date in the correct format of 30 Apr 2020?
        task_status = "no"
        with open ('tasks.txt', 'a') as f:
            f.write("\n" + username + ", " + task_title + ", " + task_descr + ", " + ddate + ", " + today + ", " + task_status)

##====================View All Tasks Function====================
def view_all():
        f = open('tasks.txt', 'r+')
        lines = f.readlines()
        for i in lines:
            task = i.replace(" ", "")
            task = i.replace("\n","")
            task = i.split(",")
            sentence = f'''
                            Task assigned to: {task[0]}
                            Task title      : {task[1]}
                            Task descrition : {task[2]}
                            Due Date        : {task[3]}
                            Date Assigned   : {task[4]}
                            Completed       : {task[5]}\n'''
            print(sentence)
            f.close()
##=====================View My Tasks Function====================
import os
from pprint import pprint

def view_mine(username):


    tasks = []
    
    i=0
    with open ('tasks.txt') as f:
        lines  = f.read().splitlines()
    for db_row, line in enumerate(lines):
        assigned_to, *rest = line.split(', ')
        if username == assigned_to:

            data = {k: v for k, v in zip(
                ('number', 'db_row', 'assigned_to', 'title', 'description',
                 'due_date', 'date_assigned', 'completed'),
                (i + 1, db_row, assigned_to, *rest))}
            tasks.append(data)
            
            i+=1
    pprint(tasks)

    
        
    task_num = int(input("Please select Task Number you would like to edit: "))
    task = tasks[task_num-1]
    edit_option = input ('''Would you like to:
                            e - edit task
                            c - mark complete
                            -1 - return to main menu\n''')
    while edit_option != "-1":
        
        if edit_option == "e":
            
            if task['completed'] == "No":
                edit = input(''' what would you like to edit:
                                    u - username
                                    d - due date\n''')
                if edit == "u":

                    task['assigned_to'] = input("Please input new user: ")

                if edit == "d":

                        task['due_date'] = input("Please input new due date(dd MMM yyyy): ")

        if edit_option == "c":

            task['completed'] = input("Please type 'Yes' if task is completed: ")

            # Actual file update part
            fetched_rows = [task['db_row'] for task in tasks]
            with open('tasks.txt') as f, open('temp.txt', 'w') as t:
                for db_row, line in enumerate(f):
                    if db_row in fetched_rows:
                        fetched_rows.remove(db_row)
                        print(', '.join(v for k, v in list(tasks.pop(0).items())[2:]), file=t)
                    else:
                        print(line.strip(), file=t)
            os.remove('tasks.txt')
            os.rename('temp.txt', 'tasks.txt')

    #return to main menu                    
    selection = input('''Please select one of the following options:
                             r - register user
                             a - add task
                             va - view all tasks
                             vm - view my tasks
                             gr - generate reports
                             ds - display statistics
                             e - exit\n''')

      
    
    
    
            
    
    


            
#========= Register User (r) ==================================

if selection == "r":
    reg_user()

 
    

#========Add Task (a) =========================================
elif selection == "a":
    add_task()
    


#============view all tasks (va)===============================

elif selection == "va":
    view_all()
    
#===============view my tasks (vm)=============================
        
elif selection == "vm":
    view_mine(username)
      
#================Generate Report (gr)==========================


elif selection == "gr":
    from datetime import datetime
    completed_tasks = 0
    incompleted_tasks = 0
    overdue_and_incomplete = 0
    percentage_completed = 0
    overdue = 0
    
    total_num_tasks = len('tasks')
    if 'completed' == "Yes":
        completed_tasks += 1
    else:
        incompleted_tasks =+ 1

    if str(datetime.now().strftime("%d %b %Y")) > 'due_date' and 'completed' == "No":
        overdue_and_incomplete += 1

    if str(datetime.now().strftime("%d %b %Y")) > 'due_date':
        overdue += 1
    percentage_completed = (completed_tasks/total_num_tasks)*100
    percentage_overdue = (overdue/total_num_tasks)*100
    print(total_num_tasks)
    print(f"Completed Tasks: {completed_tasks}")
    print(f"Incomplete Tasks: {incompleted_tasks}")
    print(f"Overdue & Incomplete: {overdue_and_incomplete}")
    print(f"% Completed: {percentage_completed}")
    print(f"% overdue: {overdue}")

    with open ('task_overview.txt', 'w') as f:
            f.write( f'''   Total numbert of tasks: {str(total_num_tasks)}
                        Total number of completed tasks: {str(completed_tasks)}
                        Total Number of incomplete tasks: {str(incompleted_tasks)}
                        Total number of overdue and incomplete tasks: {str(overdue_and_incomplete)}
                        % of tasks incomplete: {str(percentage_completed)}
                        % of tasks overdue: {str(overdue)}''')
    
    
#===============display statistics (ds)========================
        
elif selection == "ds":
    if username == "admin":

        f = open('tasks.txt', 'r+')
        lines = f.readlines()
        for i in lines:
            task = i.replace(" ", "")
            task = i.replace("\n","")
            task = i.split(",")
            statistics = (f'''
                    Number of users : {len(username_list)}
                    Number of tasks : {len(lines)}''')
        print(statistics)
        f.close()
    else:
        print("You do not have administrative rights") 

#================exit (e)======================================
        
else:
    selection == "e"
    print("Goodbye")
    



