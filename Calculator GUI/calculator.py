from tkinter import *
expression = ""


# Function to update expressiom 
def input(exp):
    global expression
    
    expression += str(exp)
    equation.set(expression)

# Function to evaluate the final expression 
def evaluate():
    try:
        global expression
        total = str(eval(expression))
        equation.set(expression)   
            
    except:
        equation.set("ERROR")
        expression = "" 

# Function to clear the expression
def clear():
    global expression
    expression ="" 
    equation.set("")
    
# The main code

if __name__ == "__main__":
    
    cal = Tk()
    
    cal.configure(background = "green")
    cal.title("Calculator")
    cal.geometry("1080x720")
    
    equation  = StringVar()
    
    exp_field = Entry( cal, textvariable = equation)
    exp_field.grid( columnspan = 4, ipadx = 70) 
    equation.set('enter your expression') 
    button1 = Button( cal, text = ' 1 ', fg = 'black', bg = 'red', command = lambda: input(1), height = 1, width = 7) 
    button1.grid(row = 4, column = 0) 
    
    
    button2 = Button( cal, text = ' 2 ', fg = 'black', bg = 'red', command = lambda: input(1), height = 1, width = 7) 
    button2.grid(row = 4, column = 1) 
    
    
    button3 = Button( cal, text = ' 3 ', fg = 'black', bg = 'red', command = lambda: input(1), height = 1, width = 7) 
    button3.grid(row = 4, column = 2) 
    
    
    button_div = Button( cal, text = '/', fg = 'black', bg = 'red', command = lambda: input(1), height = 1, width = 7) 
    button_div.grid(row = 4, column = 3 )
    
    button4 = Button( cal, text = ' 4 ', fg = 'black', bg = 'red', command = lambda: input(1), height = 1, width = 7) 
    button4.grid(row = 3, column = 0) 
    
    
    button5 = Button( cal, text = ' 5 ', fg = 'black', bg = 'red', command = lambda: input(1), height = 1, width = 7) 
    button5.grid(row = 3, column = 1) 
    
    
    button6 = Button( cal, text = ' 6', fg = 'black', bg = 'red', command = lambda: input(1), height = 1, width = 7) 
    button6.grid(row = 3, column = 2) 
    
    
    button_mul = Button( cal, text = '*', fg = 'black', bg = 'red', command = lambda: input(1), height = 1, width = 7) 
    button_mul.grid(row = 3, column = 3 )
    
    button7 = Button( cal, text = ' 7 ', fg = 'black', bg = 'red', command = lambda: input(1), height = 1, width = 7) 
    button7.grid(row = 2, column = 0) 
    
    button8 = Button( cal, text = ' 8 ', fg = 'black', bg = 'red', command = lambda: input(1), height = 1, width = 7) 
    button8.grid(row = 2 , column = 1) 
    
    
    button9 = Button( cal, text = ' 9 ', fg = 'black', bg = 'red', command = lambda: input(1), height = 1, width = 7) 
    button9.grid(row = 2, column = 2) 
    
    
    button_sub = Button( cal, text = ' - ', fg = 'black', bg = 'red', command = lambda: input(1), height = 1, width = 7) 
    button_sub.grid(row = 2, column = 3 )
    

    button0 = Button( cal, text = ' 0 ', fg = 'black', bg = 'red', command = lambda: input(1), height = 1, width = 7) 
    button0.grid(row = 5, column = 0) 
    
    
    buttondot = Button( cal, text = '.', fg = 'black', bg = 'red', command = lambda: input(1), height = 1, width = 7) 
    buttondot.grid(row = 5, column = 1 )
    
    
    button_add = Button( cal, text = ' + ', fg = 'black', bg = 'red', command = lambda: input(1), height = 1, width = 7) 
    button_add.grid(row = 5, column = 3 )
    
    cal.mainloop()
    
    