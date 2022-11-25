VALID_ACTIONS = ["ADD", "VIEW","EDIT", "DELETE", "TOGGLE", "FILTER", "HELP", "EXIT"]

# ADDING AN ITEM INTO THE LIST
def create_item(task, id):
    return {"id": id+1, "task": task, "completed": False}

def append_to_todolist(todo_list, item):
    return {"list": todo_list["list"] + [item], "id": todo_list["id"] + 1 }

# VIEWING THE ITEM IN THE LIST
def display_item(item):
    checkbox = "[x]" if item["completed"] else "[  ]"
    print(f"- {checkbox} {item['id']}: {item['task']}")

def display_list(todo_list):
    if not todo_list:
        return

    display_item(todo_list[0])
    return display_list(todo_list[1:])

# EDITING AN ITEM IN THE LIST
def edit_item(item, found_item, new_item):
    return {**item, "task": new_item} if item["id"] == found_item["id"] else item

def edit_with_id(item_list, item_id):
    new_item = input("Edit Todo Item: ")
    found_item = find_with_id(item_list, item_id)
    return [edit_item(item, found_item, new_item) for item in item_list]

# DELETING AN ITEM IN THE LIST
def remove_with_id(item_list, item_id):
    found_item = find_with_id(item_list, item_id)
    return [item for item in item_list if item["id"] != found_item["id"]]

# TOGGLING AND ITEM IN THE LIST
def toggle_item(item, found_item):
    return {**item, "completed": not item["completed"]} if item["id"] == found_item["id"] else item

def toggle_list(item_list, item_id):
    found_item = find_with_id(item_list, item_id)
    return [toggle_item(item, found_item) for item in item_list]

# PRINTING THE COMPLETE/INCOMPLETE TODOLIST
def completed_task(item):
    checkbox = "[x]" if item["completed"] else "[  ]"
    if checkbox == "[x]":
        print(f"- {checkbox} {item['id']}: {item['task']}")

def incomplete_task(item):
    checkbox = "[x]" if item["completed"] else "[  ]"
    if checkbox == "[  ]":
        print(f"- {checkbox} {item['id']}: {item['task']}")

def filter_complete(todo_list):
    if not todo_list:
        return
    completed_task(todo_list[0])
    return filter_complete(todo_list[1:])
    
def filter_incomplete(todo_list):
    if not todo_list:
        return
    incomplete_task(todo_list[0])
    return filter_incomplete(todo_list[1:])

# LOCATING THE ITEM ID
def find_with_id(item_list, item_id):
    return next(item for item in item_list if item["id"] == item_id)

# HANDLERS
def handle_add(todo_list):
    item = input("New Todo Item: ")
    item = create_item(item, todo_list["id"])
    new_todo_list = append_to_todolist(todo_list, item)
    display_list(new_todo_list["list"])
    return new_todo_list

def handle_view(todo_list):
    if not todo_list:
        return
    else:
        display_list(todo_list["list"])
        return todo_list

def handle_edit(todo_list):
    item_id = int(input("Item ID: "))
    new_todo_list = {**todo_list,
                    "list": edit_with_id(todo_list["list"], item_id)}
    display_list(new_todo_list["list"])
    return new_todo_list

def handle_delete(todo_list):
    item_id = int(input("Item ID: "))
    new_todo_list = {**todo_list,
                     "list": remove_with_id(todo_list["list"], item_id)}
    display_list(new_todo_list["list"])
    return new_todo_list

def handle_toggle(todo_list):
    item_id = int(input("Input ID: "))
    new_todo_list = {**todo_list,
                     "list": toggle_list(todo_list["list"], item_id)}
    display_list(new_todo_list["list"])
    return new_todo_list

def handle_filter(todo_list):
    if len(todo_list["list"]) == 0:
        print("No To Do Items")
    else:
        print("Completed Tasks")
        filter_complete(todo_list["list"])
        print("Incomplete Tasks")
        filter_incomplete(todo_list["list"])
    return todo_list

def handle_help(todo_list):
    print("Commands: [ADD][VIEW][EDIT][DELETE][TOGGLE][HELP][EXIT]")

# USER ACTION
def get_action():
    action = input("What would you like to do?  - ")

    if action.upper() not in VALID_ACTIONS:
        raise ValueError(f"Action {action} is invalid.")

    return action

def perform_action(action, todo_list):
    if action.upper() not in VALID_ACTIONS:
        raise ValueError(f"Action {action} is invalid.")

    action_handlers = {"ADD": handle_add,
                       "VIEW": handle_view,
                       "EDIT": handle_edit,
                       "DELETE": handle_delete,
                       "TOGGLE": handle_toggle,
                       "FILTER": handle_filter,
                       "HELP": handle_help}
    handle_action = action_handlers.get(action.upper(), lambda x: x)

    return handle_action(todo_list)

# INITIALIZE TODOLIST
def activate_todolist(todo_list):
    try:
        action = get_action()

        if action.upper() == "EXIT":
            return 0

        todo_list = perform_action(action, todo_list)
        return activate_todolist(todo_list)
    except ValueError as value_error:
        print(value_error)
        return activate_todolist(todo_list)

def main():
    todo_list = {"list": [], "id": 0}
    activate_todolist(todo_list)
    
    return 0

if __name__ == '__main__':
    main()