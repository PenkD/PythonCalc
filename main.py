
import tkinter as tk
# vars
root = tk.Tk()
operation = "none"


def changeEntryText(num):
    entry.configure(state="normal",)
    entry.insert(tk.END, str(num))
    entry.configure(state="readonly")

def set_operation(op):
    global firstUnits, operation
    entry.configure(state="normal")
    if entry.get() == "":
        firstUnits = 0
    else:
        firstUnits = int(entry.get())
    operation = op
    entry.delete(0, tk.END)
    entry.configure(state="readonly")


# clear Entry (textbox)

def clear():
    entry.configure(state="normal")
    entry.delete(0, tk.END)
    entry.configure(state="readonly")



# button 0 def
def zero():
    entry.configure(state="normal")
    entry.insert(tk.END, "0")
    entry.configure(state="readonly")




# equals variable
def equals():
    global secondUnits, firstUnits, operation
    entry.configure(state="normal")
    secondUnits = int(entry.get())

    answer = 0

    if operation == "add":
        answer = firstUnits + secondUnits

    elif operation == "subtract":
        answer = firstUnits - secondUnits
    elif operation =="multiply":
        answer = firstUnits * secondUnits
    elif operation == "divide":
        if secondUnits != 0:
            answer = firstUnits / secondUnits
        else:
            answer = "cant divide by 0"

    entry.delete(0, tk.END)
    entry.insert(0, answer)
    entry.configure(state="readonly")

root.title("Calculator Open Source")
root.configure(background="white")
root.minsize(400, 380)
root.maxsize(400, 380)
root.geometry("400x300+450+130")
# frame
Frame1 = tk.Frame(root, width=400, height=400)
Frame1.pack(padx=30, pady=30)

entry = tk.Entry(root, state="readonly", width=32, font=("Arial", 14))
entry.pack()

# numbers 1 - 9
for i in range(10):

    button = tk.Button(Frame1,

            text=str(i),
            width=8,
            height=4,
            command=lambda x = i : changeEntryText(x),


    )
    if i == 0:
        button.place(x= 400, y=34, width=50, height=50)
    else:
        row = 1 + (i - 1) // 3
        col = (i - 1) % 3
        button.grid(row=row, column=col)


# Clear

button0 = tk.Button(root,
        text="C",
        width=4,
        height=2,
        command=lambda: clear()
                    )




button0.pack()
button0.place(x=  60, y=31,)

# add button
addition = tk.Button(root,
                     text="+",
                     width=4,
                     height=2,
                     command=lambda: set_operation("add"),

                     )
addition.pack()
addition.place(x=  60, y=75)
# subtract button
subtract = tk.Button(root,
                     text="-",
                     width=4,
                     height=2,
                     command=lambda: set_operation("subtract"),

                     )
subtract.pack()
subtract.place(x=  60, y=120)
#divide button


divideButton = tk.Button(root,
                     text="÷",
                     width=4,
                     height=2,
                     command=lambda: set_operation("divide"),

                     )
divideButton.pack()
divideButton.place(x=  60, y=165)
# multiply button
multiplyButton = tk.Button(root,
                     text="x",
                     width=4,
                     height=2,
                     command=lambda: set_operation("multiply"),

                     )
multiplyButton.pack()
multiplyButton.place(x=  60, y=210)

# equals button
equals1 = tk.Button(
    root,
    text="=",
    width=20,
    height=2,
    command=lambda: equals()

)
equals1.pack()
equals1.place(x=228, y=330)


Zero = tk.Button(
    text="0",
    width=20,
    height=2,
    command=lambda: zero()
)
Zero.pack()
Zero.place(x=20, y=330)



root.mainloop()
# global secondUnits
# entry.configure(state="normal")
# secondUnits = int(entry.get())
# answer = firstUnits + secondUnits
# entry.delete(0, tk.END)
# entry.insert(0, answer)
# entry.configure(state="readonly")
