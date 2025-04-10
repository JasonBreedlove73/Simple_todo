
# shows main menu to the user
def show_menu():
    print("\n=== TO-DO LIST MENU ===")    # \n to create a blank line above the menu for better readability
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Quit")

    
# lets user add a task  
def add_task(tasks):
    task = input("Enter a new task: ") # asking user for the task
    if task.strip() != "":             # making sure the task isnt empty
        tasks.append(task)             # add task to the list
        print("Task added!")
    else:
        print("You can't add an empty task.")

        
# shows all tasks in the list        
def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks to show.")
    else:
        print("\nYour tasks:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")   # shows each task with a number
 
            
 # delete a task by its number           
def delete_task(tasks):
    if len(tasks) == 0:
        print("There are no tasks to delete.")
        return
    
    
    view_tasks(tasks)             # shows tasks so the user can choose
    
    try:
        task_num = int(input("Enter the number of the task to delete:"))  # asking which one to delete
        if task_num >= 1 and task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)                        # remove the task
            print(f"Deleted: {removed_task}")
        else:
            print("That task number doesn't exist.")
    except ValueError:
        print("Please enter a valid number.")
  
        
 # main function where everything runs       
def main():
    tasks = []    # task list (enpty at first)
    
    while True:
        show_menu()    # show the menu options
        try:
            choice = input("Choose an option (1-4): ")
            
            # if/elif checks what the user chose
            if choice == "1":
                add_task(tasks)
            elif choice == "2":
                view_tasks(tasks)
            elif choice == "3":
                delete_task(tasks)
            elif choice == "4":
                print("Goodbye!")
                break    # ends the loop and exits the program
            else:
                print("That's not a valid option. Please enter 1, 2, 3, or 4.")
        except Exception as e:
            print("Something went wrong:", e)
        finally:
            # runs no matter what (even if there was an error)
            print("-" * 30)  # prints a divider line for readability


# makes sure the main() function runs when we start the program            
if __name__ == "__main__":
    main()