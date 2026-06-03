todo_list = []

while True:
    print("MY TASKS")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Total Tasks")
    print("5. Exit")

    option = input("Choose option: ")
    if option =="1":
        task = input("What work do you want to add? ")
        todo_list.append(task)
        print("Added successfully!")
    elif option =="2":
        if len(todo_list) == 0:
            print("Nothing added yet.")
        else:
            print("\nCurrent Tasks:")
            number = 1
            for item in todo_list:
                print(str(number) + ". " + item)
                number += 1
    elif option =="3":
        if len(todo_list) == 0:
            print("No tasks found.")
        else:
            count = 1
            for item in todo_list:
                print(str(count) + ". " + item)
                count += 1
            remove = int(input("Enter task number: "))
            if remove >= 1 and remove <= len(todo_list):
                deleted_task = todo_list.pop(remove - 1)
                print(deleted_task, "removed.")
            else:
                print("Wrong number entered.")
    elif option =="4":
        print("Total tasks =", len(todo_list))
    elif option =="5":
        print("Closing program...")
        break
    else:
        print("Please enter a valid option.")