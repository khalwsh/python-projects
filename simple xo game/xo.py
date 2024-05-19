from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("TIC-Tac-Toe ")
window.geometry("500x400")

lbl = Label(window, text="Game", font=("Helvetica", '15'))
lbl.grid(row=0, column=0)
lbl = Label(window, text="player 1: X", font=('Helvetica', 10))
lbl.grid(row=1, column=0)
lbl = Label(window, text="player 2: O", font=('Helvetica', 10))
lbl.grid(row=2, column=0)

turn = True

def clicked1():
    """
    Handles the click event for the first button.
    Updates the button text based on the current player's turn.
    """
    global turn
    if btn1["text"] == " ":
        if turn:
            btn1["text"] = "X"
        else:
            btn1["text"] = "O"
        turn = not turn
        check()

def clicked2():
    """
    Handles the click event for the second button.
    Updates the button text based on the current player's turn.
    """
    global turn
    if btn2["text"] == " ":
        if turn:
            btn2["text"] = "X"
        else:
            btn2["text"] = "O"
        turn = not turn
        check()

def clicked3():
    """
    Handles the click event for the third button.
    Updates the button text based on the current player's turn.
    """
    global turn
    if btn3["text"] == " ":
        if turn:
            btn3["text"] = "X"
        else:
            btn3["text"] = "O"
        turn = not turn
        check()

def clicked4():
    """
    Handles the click event for the fourth button.
    Updates the button text based on the current player's turn.
    """
    global turn
    if btn4["text"] == " ":
        if turn:
            btn4["text"] = "X"
        else:
            btn4["text"] = "O"
        turn = not turn
        check()

def clicked5():
    """
    Handles the click event for the fifth button.
    Updates the button text based on the current player's turn.
    """
    global turn
    if btn5["text"] == " ":
        if turn:
            btn5["text"] = "X"
        else:
            btn5["text"] = "O"
        turn = not turn
        check()

def clicked6():
    """
    Handles the click event for the sixth button.
    Updates the button text based on the current player's turn.
    """
    global turn
    if btn6["text"] == " ":
        if turn:
            btn6["text"] = "X"
        else:
            btn6["text"] = "O"
        turn = not turn
        check()

def clicked7():
    """
    Handles the click event for the seventh button.
    Updates the button text based on the current player's turn.
    """
    global turn
    if btn7["text"] == " ":
        if turn:
            btn7["text"] = "X"
        else:
            btn7["text"] = "O"
        turn = not turn
        check()

def clicked8():
    """
    Handles the click event for the eighth button.
    Updates the button text based on the current player's turn.
    """
    global turn
    if btn8["text"] == " ":
        if turn:
            btn8["text"] = "X"
        else:
            btn8["text"] = "O"
        turn = not turn
        check()

def clicked9():
    """
    Handles the click event for the ninth button.
    Updates the button text based on the current player's turn.
    """
    global turn
    if btn9["text"] == " ":
        if turn:
            btn9["text"] = "X"
        else:
            btn9["text"] = "O"
        turn = not turn
        check()

def empty(b):
    """
    Checks if a button text is empty.

    Parameters:
    b (str): The text of the button to check.

    Returns:
    bool: True if the button text is empty, False otherwise.
    """
    return b == " "

def check():
    """
    Checks the current state of the board to determine if there's a winner or if the game is a draw.
    """
    b1 = btn1["text"]
    b2 = btn2["text"]
    b3 = btn3["text"]
    b4 = btn4["text"]
    b5 = btn5["text"]
    b6 = btn6["text"]
    b7 = btn7["text"]
    b8 = btn8["text"]
    b9 = btn9["text"]

    if not empty(b1) or not empty(b2) or not empty(b3) or not empty(b4) or not empty(b5) or not empty(b6) or not empty(b7) or not empty(b8) or not empty(b9):
        if b1 == b2 and b2 == b3:
            win(btn1["text"])
        if b4 == b5 and b5 == b6:
            win(btn4["text"])
        if b7 == b8 and b8 == b9:
            win(btn7["text"])
        if b1 == b4 and b4 == b7:
            win(btn1["text"])
        if b2 == b5 and b5 == b8:
            win(btn2["text"])
        if b3 == b6 and b6 == b9:
            win(btn3["text"])

        if b1 == b5 and b5 == b9:
            win(btn1["text"])

        if b3 == b5 and b5 == b7:
            win(btn3["text"])
    else:
        messagebox.showinfo("draw", "Try again")
        window.destroy()

def win(player):
    """
    Displays a message indicating the winner and terminates the game.

    Parameters:
    player (str): The player who won the game.
    """
    if player != " ":
        ans = player + " wins"
        messagebox.showinfo("", ans)
        window.destroy()

btn1 = Button(window, text=" ", bg="white", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked1)
btn1.grid(column=1, row=1)

btn2 = Button(window, text=" ", bg="white", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked2)
btn2.grid(column=2, row=1)

btn3 = Button(window, text=" ", bg="white", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked3)
btn3.grid(column=3, row=1)

btn4 = Button(window, text=" ", bg="white", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked4)
btn4.grid(column=1, row=2)

btn5 = Button(window, text=" ", bg="white", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked5)
btn5.grid(column=2, row=2)

btn6 = Button(window, text=" ", bg="white", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked6)
btn6.grid(column=3, row=2)

btn7 = Button(window, text=" ", bg="white", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked7)
btn7.grid(column=1, row=3)

btn8 = Button(window, text=" ", bg="white", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked8)
btn8.grid(column=2, row=3)

btn9 = Button(window, text=" ", bg="white", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked9)
btn9.grid(column=3, row=3)

window.mainloop()
