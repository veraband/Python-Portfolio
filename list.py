#vera
#list.py
# The program should utilize lists in Python to store and manipulate the tasks. By completing this assignment,
# you will strengthen your understanding of lists, user input, and basic control structures in Python.

#init
#functions
list = []
def lists():
    print("Welcome to your personalized Book Nook!")
    while True:
        menu = input("What would you like to do with your book list? [add, remove, clear, mark as done, exit] ").strip().lower()
        #Add books to list
        if menu =="":
             print("Error. Please try again.")
        if menu == "add":
                add = input("Which book would you like to add to you list? ").strip().lower()
                if add == "":
                     print("Error. Please try again.")
                elif add in list:
                     print("This book is already in you list!")
                     continue
                else:
                     list.append(add)
                     print(list)
        #Mark books as done
        if menu == "mark as done":
             done = input("What book would you like to mark as done? ").strip().lower()
             if done == "":
                  print("Error. Please try again.")
             elif done in list:
                  list.remove(done)
                  print(list)
             else:
                  print("This book is not in your list.")
                  continue

        #Remove books from list
        if menu == "remove": #remove items from list
            remove = input("What would you like to remove? ").strip().lower()
            if remove == "":
                 print("Error. Please try again.")
            elif remove in list:
                list.remove(remove)
                print(list)
            else:
                print("This item is not in your list")
                continue
        #exit the list
        if menu == "exit":
             break

#main

lists()
