from tkinter import *  # import everything from gui package tkinter


class EditText:

    fileName = "list.txt"  # name of file to be written and read from

    def __init__(self):  # constructor method
        file1 = open(self.fileName, "r")  # opens text file to read
        self.items = file1.readlines()  # file1.readlines() is read and stored to items as a list
        file1.close()  # file is closed

        self.formatItems = ""  # initialize empty string called formatItems to make label format and modification easier
        for item in self.items:  # for each item in items add item to listItems
            self.formatItems = self.formatItems + item

    def write_text(self):  # method that reads input into text file
        task = addE.get()  # gets input from addE entry widget
        addE.delete(0, END)  # removes text from addE input field
        task += "\n"  # adds new line for file formatting
        self.items.append(task)  # task is appended to items list
        file1 = open(self.fileName, "w")  # opens text file for overwriting or makes one if it doesn't exist
        file1.writelines(self.items)  # overwrites current text with modified items list
        file1.close()  # closes file
        self.formatItems = self.formatItems + self.items[len(self.items) - 1]
        listLabel.config(text="TODO LIST:\n\n" + et1.formatItems)

    def read_text(self):  # method that reads items in text file to console
        for item in self.items:  # for each item in items print item
            item = item.rstrip("\n")  # removes new line for console formatting
            print(item)  # prints item to console

    def remove_text(self):  # method that will remove specific lines of text from text file
        num = int(delE.get()) - 1  # sets num to int cast input(minus one to match index) from delE widget
        delE.delete(0, END)  # removes text from delE input field
        self.items.pop(num)  # remove item at num index
        file1 = open(self.fileName, "w")  # opens text file for overwriting
        file1.writelines(self.items)  # overwrites current text with modified items list
        file1.close()  # closes file
        self.formatItems = ""  # clears formatItems to be updated to remove deleted items
        for item in self.items:  # for each item in items add item to listItems
            self.formatItems = self.formatItems + item
        listLabel.config(text="TODO LIST:\n\n" + et1.formatItems)


'''Variables and Objects'''
root = Tk()  # creates instance of tkinter called root
et1 = EditText()  # obj edit text 1(et1) created


'''tkinter gui setup'''
listLabel = Label(root, text="TODO LIST:\n\n" + et1.formatItems)  # creates listLabel label widget that displays formatItems
addLabel = Label(root, text="Add Items Here:")  # instruction label with text "Add items here:"
addButton = Button(root, text="Add Item", command=et1.write_text, width=10)  # creates addButton button widget with text "Add Items"
addE = Entry(root, width=24)  # creates addE input widget with width of 24
delLabel = Label(root, text="Input Task Number:")  # instruction label with text "Input Task Number:"
delButton = Button(root, text="Delete Item", command=et1.remove_text, width=10)  #
delE = Entry(root, width=24)  # creates delE input widget with width of 24

'''tkinter gui '''
listLabel.grid(row=0, column=0, columnspan=2)
addLabel.grid(row=1, column=0)
addButton.grid(row=2, column=1)
addE.grid(row=2, column=0)
delLabel.grid(row=3, column=0)
delButton.grid(row=4, column=1)
delE.grid(row=4, column=0)


root.mainloop()