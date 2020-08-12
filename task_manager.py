
#This program is a task manager for a small business and allows the user
#to add and assign tasks to users, as well as add new users


#======== User Login ====================

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
username = input("Please enter username: ")
password = input("Please enter password: ")


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
                             s - statistics
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


#========= Register User (r) ============

if selection == "r":
    if username == "admin":
        print("Register User")
        username = input("Please enter username: ")
        password = input("Please enter password: ")
        cpassword = input("Please confirm password: ")
        while password != cpassword:
            print("passwords do not match")
            password = input("Please enter password: ")
            cpassword = input("Please confirm password: ")
        if password == cpassword:
            with open ('user.txt', 'a') as f:
                f.write("\n" + username + ", "+ password)      #append user name and password to user.txt
                print(f"User '{username}' successfully added")
    else:
        print("You do not have adminstrative rights")

#========Add Task (a) ===================

elif selection == "a":
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


#============view all tasks (va)========

elif selection == "va":
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
#===============view my tasks (vm)======
        
elif selection == "vm":
    f = open('tasks.txt', 'r+')
    lines = f.readlines()
    for i in lines:
        task = i.replace(" ", "")
        task = i.replace("\n","")
        task = i.split(",")
        i = 0  #Here login is like a flag. Which get the value 1 once the login is successful else stays 0.
        while i < len(username_list):
            if username == str(username_list[i]):
                sentence = (f'''
                        Task assigned to: {task[0]}
                        Task title      : {task[1]}
                        Task descrition : {task[2]}
                        Due Date        : {task[3]}
                        Date Assigned   : {task[4]}
                        Completed       : {task[5]}\n''')
                print(sentence)
            i+=1
        f.close()    

#===============statistics (s)==========
        
elif selection == "s":
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

#================exit (e)===============
        
else:
    selection == "e"
    print("Goodbye")
    
