from tkinter import *

b, count = None, None
visited, turn = None, None
win = None

def check(clicked):
    global turn, count, visited, b
    
    count += 1
    visited[clicked] = turn
    if b[clicked].cget('text') == "":
        b[clicked].configure(text = turn)
        turn = "O" if turn == "X" else "X"
        
    if count > 2:
        checkPattern()
        
def checkPattern():
    global turn, count
    ans = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
    flag = 0
    for i in ans:
        temp = i
        a1 = temp[0]
        a2 = temp[1]
        a3 = temp[2]
        
        if visited[a1] != "" and visited[a1] == visited[a2] and visited[a2] == visited[a3]:
            turn = "O" if turn == "X" else "X"
            flag = 1
            break
        
    global win
    if flag == 1:
        messagebox.showinfo(turn + " Won", "Restart the Game")
        win.destroy()
        gui()
    elif count == 9:
        messagebox.showinfo("None Won", "Restart the Game")
        win.destroy()
        
        gui()

def gui():
    global b, turn, count, visited, win
    
    win = Tk()
    win.title("Tic Tac Toe")
    win.resizable(False, False)
    win.geometry("450x350+480+180")
    
    b = [None for i in range(9)]
    turn = "X"
    count = 0
    visited = ["" for i in range(9)]
    
    b[0] = Button(win, text = '', height = 7, width = 20, command = lambda: check(0))
    b[1] = Button(win, text = '', height = 7, width = 20, command = lambda: check(1))
    b[2] = Button(win, text = '', height = 7, width = 20, command = lambda: check(2))
    b[3] = Button(win, text = '', height = 7, width = 20, command = lambda: check(3))
    b[4] = Button(win, text = '', height = 7, width = 20, command = lambda: check(4))
    b[5] = Button(win, text = '', height = 7, width = 20, command = lambda: check(5))
    b[6] = Button(win, text = '', height = 7, width = 20, command = lambda: check(6))
    b[7] = Button(win, text = '', height = 7, width = 20, command = lambda: check(7))
    b[8] = Button(win, text = '', height = 7, width = 20, command = lambda: check(8))
    
    b[0].grid(row = 0, column = 0)
    b[1].grid(row = 0, column = 1)
    b[2].grid(row = 0, column = 2)
    b[3].grid(row = 1, column = 0)
    b[4].grid(row = 1, column = 1)
    b[5].grid(row = 1, column = 2)
    b[6].grid(row = 2, column = 0)
    b[7].grid(row = 2, column = 1)
    b[8].grid(row = 2, column = 2)
    
    win.mainloop()    
gui()
