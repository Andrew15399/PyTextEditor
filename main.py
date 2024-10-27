from tkinter import *  # import everything from gui package tkinter


class EditText:

    def __init__(self):  # constructor method
        file1 = open("list.txt", "r")  # opens text file to read
        self.items = file1.readlines()  # file1.readlines() is read and stored to items as a list
        file1.close()  # file is closed

        self.formatItems = ""  # initialize empty string called formatItems
        for item in self.items:  # for each item in items add item to listItems
            self.formatItems = self.formatItems + item

    def write_text(self):  # method that reads input into text file
        task = addE.get()  # gets input from addE entry widget
        task += "\n"  # adds new line for file formatting
        self.items.append(task)  # task is appended to items list
        file1 = open("list.txt", "w")  # opens text file for overwriting
        file1.writelines(self.items)  # overwrites current text with modified items list
        file1.close()  # closes file

    def read_text(self):  # method that reads items in text file to console
        for item in self.items:  # for each item in items print item
            item = item.rstrip("\n")  # removes new line for console formatting
            print(item)  # prints item to console

    def remove_text(self):  # method that will remove specific lines of text from text file
        num = int(delE.get())  # sets num to int cast input from delE widget
        num -= 1  # subtract one so the row number equals index value
        self.items.pop(num)  # remove item at num index
        file1 = open("list.txt", "w")  # opens text file for overwriting
        file1.writelines(self.items)  # overwrites current text with modified items list
        file1.close()  # closes file


'''Variables and Objects'''
root = Tk()  # creates instance of tkinter called root
et1 = EditText()  # obj edit text 1(et1) created


'''tkinter gui setup'''
listLabel = Label(root, text="TODO LIST:\n\n" + et1.formatItems)  # creates listLabel label widget that displays formatItems
addLabel = Label(root, text="Add items here:")
addE = Entry(root, width=30)  # creates addE input widget with width of 24
addButton = Button(root, text="Add Item", command=et1.write_text, width=10)  # creates addButton button widget with text "Add Items"
delButton = Button(root, text="Delete Item", command=et1.remove_text, width=10)  #
delE = Entry(root, width=30)  # creates delE input widget with width of 24

'''tkinter gui '''
listLabel.grid(row=0, column=0, columnspan=2)
addButton.grid(row=1, column=1)
addE.grid(row=1, column=0)
delButton.grid(row=2, column=1)
delE.grid(row=2, column=0)


root.mainloop()


'''
ans = '0'  # input answer char value created and initialized

while ans != 'q' and ans != 'Q':  # creates infinite loop until q/Q is submitted
    ans = input("A. Add Item to List, B. To Remove Item from List, C. to View List, Q. to Quit")  # sets answer to
    # keyboard input

    if ans == 'a' or ans == 'A':  # if answer value equals a/A call et1.writeText
        et1.write_text()

    elif ans == 'b' or ans == 'B':  # if answer value equals b/B call et1.removeText
        et1.remove_text()

    elif ans == 'c' or ans == 'C':  # if answer value equals c/C call et1.readText
        et1.read_text()

    elif ans == 'q' or ans == 'Q':  # if answer value equals q/Q print by and end while loop
        print("bye for now")'''

