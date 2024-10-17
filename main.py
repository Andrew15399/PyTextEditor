class EditText:

    def __init__(self):  # constructor func
        file1 = open("list.txt", "r")  # opens text file to read
        self.items = file1.readlines()  # file1.readlines() is read and stored to items as a list
        file1.close()  # file is closed

    def write_text(self):  # func that reads input into text file
        task = input("Enter a task: ")  # takes keyboard input and stores in task
        task += "\n"  # adds new line for file formatting
        self.items.append(task)  # task is appended to items list
        file1 = open("list.txt", "w")  # opens text file for overwriting
        file1.writelines(self.items)  # overwrites current text with modified items list
        file1.close()  # closes file

    def read_text(self):  # reads items in text file to console
        for item in self.items:  # for each item in items print item
            item = item.rstrip("\n")  # removes new line for console formatting
            print(item)  # prints item to console

    def remove_text(self):
        num = int(input("Enter row of task to remove: "))  # sets num to int cast input
        num -= 1  # subtract one so the row number equals index value
        self.items.pop(num)  # remove item at num index
        file1 = open("list.txt", "w")  # opens text file for overwriting
        file1.writelines(self.items)  # overwrites current text with modified items list
        file1.close()  # closes file


et1 = EditText()  # obj edit text 1(et1) created
ans = '0'  # input answer value created and initialized

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
        print("bye for now")
