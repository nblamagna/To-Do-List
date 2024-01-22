#To-Do List
#1/11/2024
#Nico and Bobo 

to_do = []

#allows user to edit the to do list
#no parameters 
#contains if statement depending on input
def to_do_actions():

    action = input('''What would you like to do? 
                \n1. Add task to the to-do list 
                \n2. View the current to-do list 
                \n3. Mark a task as completed 
                \n4. Remove a task from the to-do list
                \n5. Exit the program
                \n''')

    if int(action) == 1:
        task = input('What task would you like to add? ')
        to_do.append(task)
        print('\n')
        to_do_actions()
        print(to_do)
    elif int(action) == 2:
        print(to_do)
        print('\n')
        to_do_actions()
    elif int(action) == 3:
        print(to_do)
        num = int(input('Which task would you like to cross out? Please type the position of the task. '))
        for num in range(len(to_do)):
            to_do[num-1] = to_do[num-1] + ' [X]'
        print('\n')
        to_do_actions()
    elif int(action) == 4:
        delete = input('Which task would you like to remove? Please type the task exactly as it is. ')
        to_do.remove(delete)
        print('\n')
        to_do_actions()
    else:
        quit()

    
to_do_actions()