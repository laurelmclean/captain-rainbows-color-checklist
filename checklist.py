#Captain Rainbows Color Checklist

# empty list that will be added to
checklist = list()

# CREATE - add item to end of list
def create(item):
    checklist.append(item)

# READ
def read(index):
    if index <= len(checklist):
        print(checklist[index])
        return checklist[index] 
    else:
       print("This item does not exist. Please try again")

# UPDATE
def update(index, item):
    if index <= len(checklist):
        checklist[index] = item
        print("Item has been updated.")
    else:
       print("This item does not exist. Please try again")

# DESTROY
def destroy(index):
    if index <= len(checklist):
        checklist.pop(index)
        print("Item has been deleted.")
    else:
       print("This item does not exist. Please try again")

def list_all_items():
    print("CAPTAIN RAINBOWS COLORFUL CLOSET")
    index = 0
    for list_item in checklist:
        print(f"{index} {list_item}")
        index += 1

# Add checkmark beside item
def mark_completed(index):
    if index <= len(checklist):
        checked_item = checklist[index] + " √"
        update(index, checked_item)
        print("Item has been marked as complete.")
    else:
        print("This item does not exist. Please try again")

def user_input(prompt):
    #return copy of string converted to lowercase
    user_input = input(prompt).lower()
    return user_input

# User inputs selections

def select(function_code):
    # Create item
    if function_code == "c":
        input_item = user_input("Add item to list: ")
        create(input_item)

    # Read item
    elif function_code == "r":
            item_index = int(user_input("Which item number do you want to view? "))
            read(int(item_index))

    # Print all items
    elif function_code == "p":
        list_all_items()

    # Update an item 
    elif function_code == "u":
        item_index = int(user_input("Enter index of item you wish to update: "))
        replace_item = user_input("What item do you wish to replace it with? ")
        update(item_index, replace_item)

    # checkmark an item as completed 
    elif function_code == "m":
        item_index = int(input("Which index number do you want to mark as completed? "))
        mark_completed(item_index)

    # Delete an item 
    elif function_code == "d":
        item_index = int(input("Which index do you wish to delete? "))
        destroy(item_index)    

    #quit program and stop loop    
    elif function_code == "q":
        return False

    # If users inputs an unrecognized answer
    else:
        print("You have inputted an unrecognized option. Please try again.")
    return True


def test():
    # Created test items so there would be several in the closet when the program starts
  create("Blue jeans")
  create("Pink shirt")
  create("Orange Socks")
  create("Green hat")
  create("Yellow jacket")
  create("Brown shoes")

test()

# Run application using a while loop
running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, U to update item, M to mark item as complete, D to delete item, or Q to quit: ")
    running = select(selection)
  


