from tkinter import *
from random import randint
from tkinter import Label

root = Tk()
root.title("Random Winner Generator")
root.geometry("400x400")
root.resizable(0, 0)
root.config(bg="#262626")
winner_lb: Label = Label(root, text="? ? ? ?", font=("times new roman", 20), fg="white", bg="#262626")
winner_lb.place(x=155, y=260)


def main():

    def pick():
        global winner_lb
        winner_lb.destroy()
        entries = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
                   "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Alpha", "Bravo",
                   "Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel",
                   "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa",
                   "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-ray",
                   "Yankee", "Zulu", "Zulu", "Zulu"
                   ]
        # Convert the list into to prevent duplicates
        entries_set = set(entries)

        unique_entries = list(entries_set)

        size = len(unique_entries) - 1
        rand_var = randint(0, size)
        winner_lb = Label(root, text=unique_entries[rand_var], font=("times new roman", 20), fg="white", bg="#262626")
        winner_lb.place(x=140, y=260, width=110)
        win_lb = Label(root, text="♥ ☺☺☺ ☻☻☻ ♥ ", font=("times new roman", 16), fg="white", bg="#262626")
        win_lb.place(x=110, y=310)

    top_label = Label(root, text="Let's Find The Winner!", font=("Helvetica", 24), fg="white", bg="#262626")
    top_label.pack(pady=30)
    win_btn = Button(root, text="PICK A WINNER !", font=('Helvetica', 20),
                     command=pick, fg="white", bg="#262626", relief=GROOVE)
    win_btn.pack(pady=10)
    lb = Label(root, text="The Winner is : ", font=("times new roman", 16), fg="white", bg="#262626")
    lb.place(x=130, y=210)
    root.mainloop()


if __name__ == '__main__':
    main()

# Created by Malek1Dev
