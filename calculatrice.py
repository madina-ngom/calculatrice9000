import tkinter as tk

root = tk.Tk()
root.title('Calculatrice')
root.geometry("300x400")

def btn_click(number):
    entry.insert(tk.END, number)

def bt_clear(): 
    entry.delete(0, tk.END)

def bt_equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo ("Error", "Syntax Error")

 
entry= tk.Entry(root)
entry.pack(padx = 5, pady = 5)

frame = tk.Frame(root)
frame.pack(pady =10, padx = 10)



# liste des chiffres 7, 8, 9, 4, 5, 6, 1, 2, 3, 0

b7 =tk.Button(frame, text = "7", relief="groove", height= 2, width = 3, command= lambda :btn_click (7))
b7.grid(row = 0, column = 0, padx = 5, pady = 5)
 
b8 =tk.Button(frame, text = "8", relief="groove", height= 2, width = 3, command= lambda :btn_click (8))
b8.grid(row = 0, column = 1, padx = 5, pady = 5)
 
b9 =tk.Button(frame, text = "9", relief="groove", height= 2, width = 3, command= lambda :btn_click (9))
b9.grid(row = 0, column = 2, padx = 5, pady = 5)
 
b4 =tk.Button(frame, text = "4", relief="groove", height= 2, width = 3, command= lambda :btn_click (4))
b4.grid(row = 1, column = 0, padx = 5, pady = 5)

b5 =tk.Button(frame, text = "5", relief="groove", height= 2, width = 3, command= lambda :btn_click (5))
b5.grid(row = 1, column = 1, padx = 5, pady = 5)

b6 =tk.Button(frame, text = "6", relief="groove", height= 2, width = 3, command= lambda :btn_click (6))
b6.grid(row = 1, column = 2, padx = 5, pady = 5)
 
b1 =tk.Button(frame, text = "1", relief="groove", height= 2, width = 3, command= lambda :btn_click (1))
b1.grid(row = 2, column = 0, padx = 5, pady = 5)
 
b2 =tk.Button(frame, text = "2", relief="groove", height= 2, width = 3, command= lambda :btn_click (2))
b2.grid(row = 2, column = 1, padx = 5, pady = 5)

b3 =tk.Button(frame, text = "3", relief="groove", height= 2, width = 3, command= lambda :btn_click (3))
b3.grid(row = 2, column = 2, padx = 5, pady = 5)

b0 =tk.Button(frame, text = "0", relief="groove", height= 2, width = 3, command= lambda :btn_click (0))
b0.grid(row = 3, column = 1, padx = 5, pady = 5)

# opérateurs de bases 

bx =tk.Button(frame, text ="⌫", relief="groove", height= 2, width = 3, command= lambda :bt_clear())
bx.grid(row = 3, column = 0, padx = 5, pady = 5,)

bxx =tk.Button(frame, text ="=", relief="groove", height= 2, width = 3, command= lambda :bt_equal())
bxx.grid(row = 3, column = 2, padx = 5, pady = 5)

bp =tk.Button(frame, text = "+", relief="groove", height= 2, width = 3, command= lambda :btn_click ("+"))
bp.grid(row = 0, column = 3, padx = 5, pady = 5)

bm =tk.Button(frame, text = "-", relief="groove", height= 2, width = 3, command= lambda :btn_click ("-"))
bm.grid(row = 1, column = 3, padx = 5, pady = 5)

bf =tk.Button(frame, text ="*", relief="groove", height= 2, width = 3, command= lambda :btn_click ("*"))
bf.grid(row = 2, column = 3, padx = 5, pady = 5)

bd =tk.Button(frame, text ="/", relief="groove", height= 2, width = 3, command= lambda :btn_click ("/"))
bd.grid(row = 3, column = 3, padx = 5, pady = 5)

# opérateurs spéciaux

bc =tk.Button(frame, text ="%", relief="groove", height= 2, width = 3, command= lambda :btn_click ("%"))
bc.grid(row = 0, column = 4, padx = 5, pady = 5)

bc =tk.Button(frame, text ="√x", relief="groove", height= 2, width = 3, command= lambda :btn_click ("√x"))
bc.grid(row = 1, column = 4, padx = 5, pady = 5)

bc =tk.Button(frame, text ="1/x", relief="groove", height= 2, width = 3, command= lambda :btn_click ("1/x"))
bc.grid(row = 2, column = 4, padx = 5, pady = 5)

bc =tk.Button(frame, text ="2/x", relief="groove", height= 2, width = 3, command= lambda :btn_click ("2/x"))
bc.grid(row = 3, column = 4, padx = 5, pady = 5)


root.mainloop()