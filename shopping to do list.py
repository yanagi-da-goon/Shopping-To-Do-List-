#Giovanny Ceballos and Reem 
#1/11/24

todo = ["Eggs", "Milk", "Flour","Sugar","Bread", "Cheese","Ham"] #This is the list that the user starts with 
def replay(): #This function repeats the main function so that it doesn't end
    displaymenu()

def displaymenu(): #This function displays the option that the user is able to choose from
    print("Welcom to your Shopping List!")
    print("What would you like to do to your list? :\n 1. Add to List\n 2. View List\n 3. Mark Item Complete\n 4. Remove Item\n 5. Remove all Items\n 6. Sort Items Alphabetically\n 7. Total Number of Items\n 8. Exit")
    option = int(input("Option : "))
    if option == 1: #This adds an item to the users list and they get to choose where to insert it
        print ("What would you like to add?")
        add = input("Type in item : ")
        print("Where would you like to add it?")
        where = int(input("Type in a number between 0 and " + str(len(todo)) + " : ")) # The len(todo) shows the number of items in a list, which would also work as adding the item to the end of the list, since the list is "counted" starting from 0, the last number would a plus 1 to the counted list.
        todo.insert(where, add)
        replay()
    if option == 2: #This displays the list
        print(todo)
        replay()
    if option == 3: #This marks an item as complete by adding a [X] at the end of the item's name
        print("Which item would you like to mark as complete?")
        comp = input("Type in the item : ")
        x = todo.index(comp)
        todo[x] = comp + "[X]"
        replay()
    if option == 4: #This lets the user remove any item they want from the list
        print("Which item would you like to remove?")
        remove = input("Select which item to remove : ")
        y = todo.index(remove)
        todo.pop(y)
        replay()
#Everything past this is part 2
    if option == 5: #This clears all the items from the list
        todo.clear()
        replay()
    if option == 6: #This sorts the list alphabetically
        todo.sort()
        replay()
    if option == 7: #Prints the number of items in the list
        print("The Number of Items in the List is : " + str(len(todo)))
        replay()
    if option == 8: #Quits the whole program
        quit()



displaymenu()