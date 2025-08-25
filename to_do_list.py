def task(): 
    tasks = []
    
    print("Hey Moheez! Welcome to the Management App")

    total_task = int(input("enter total number of tasks to be added = "))
    for i in range(1, total_task + 1):
        name_of_task = input(f"enter task number {i} = ")
        priority = input("enter priority of task (high/medium/low or 1/2/3) = ")
        tasks.append({"task": name_of_task, "priority": priority})
    
    print("\n your today tasks are:")
    for t in tasks:
        print(f"- {t['task']} (Priority: {t['priority']})")
    
    while True:
        input_from_user = int(input("\nEnter:\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit = "))
        
        if input_from_user == 1:
            add = input("add your task = ")
            priority = input("enter priority (high/medium/low or 1/2/3) = ")
            tasks.append({"task": add, "priority": priority})
            print(f"Task '{add}' (Priority: {priority}) has been successfully added.")
        
        elif input_from_user == 2:
            update = input("enter task you want to update = ")
            found = False
            for t in tasks:
                if t["task"] == update:
                    new_task = input("enter new task name = ")
                    new_priority = input("enter new priority (high/medium/low or 1/2/3) = ")
                    t["task"] = new_task
                    t["priority"] = new_priority
                    print(f"the updated task to '{new_task}' (Priority: {new_priority})")
                    found = True
                    break
            if not found:
                print(f"task name '{update}' you added is not found")
        
        elif input_from_user == 3:
            del_val = input("enter task you want to delete = ")
            for t in tasks:
                if t["task"] == del_val:
                    tasks.remove(t)
                    print(f"Task '{del_val}' deleted.")
                    break
            else:
                print(f"task '{del_val}' not found!")
        
        elif input_from_user == 4:
            if not tasks:
                print("no tasks available!")
            else:
                print("\nyour tasks:")
                for t in tasks:
                    print(f"- {t['task']} (Priority: {t['priority']})")
        
        elif input_from_user == 5:
            print("closing the program...")
            break
        else:
            print("Please enter a valid input")
task()
