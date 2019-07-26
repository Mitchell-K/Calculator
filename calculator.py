from tkinter import *

class Calculator():

    def __init__(self, master):
        self.master = master

        self.equation = StringVar() 
        self.equation.set("")
        #self.equation.trace("w", self.validate) #Possibly use trace, need to return corrected version though

        vcmd = master.register(self.validate) # we have to wrap the command
        self.expression_field = Entry(master, validate="key", validatecommand=(vcmd, '%d', '%i', '%s', '%S'), textvariable=self.equation)

        # create and set label for previous expression total
        #self.total_label_text = IntVar()
        #self.total_label_text.set(self.total)
        #self.total_label = Label(master, textvariable=self.total_label_text)

        # LAYOUT

        # set the title of GUI window 
        master.title("Calculator") 
        # set the configuration size of GUI window 
        master.geometry("530x250") 

        self.expression_field.grid(columnspan=4, ipadx=140) 

        self.history = Label(master, text="History:")
        self.history.grid(row=0, column=4, sticky=W+E)


        # Number buttons
        self.one_button = Button(master, text=' 1 ', fg='black', bg='red', 
                     command=lambda: self.press(1), height=1, width=7) 
        self.one_button.grid(row=2, column=0) 
    
        self.two_button = Button(master, text=' 2 ', fg='black', bg='red', 
                         command=lambda: self.press(2), height=1, width=7) 
        self.two_button.grid(row=2, column=1) 
    
        self.three_button = Button(master, text=' 3 ', fg='black', bg='red', 
                         command=lambda: self.press(3), height=1, width=7) 
        self.three_button.grid(row=2, column=2) 
    
        self.four_button = Button(master, text=' 4 ', fg='black', bg='red', 
                         command=lambda: self.press(4), height=1, width=7) 
        self.four_button.grid(row=3, column=0) 
    
        self.five_button = Button(master, text=' 5 ', fg='black', bg='red', 
                         command=lambda: self.press(5), height=1, width=7) 
        self.five_button.grid(row=3, column=1) 
    
        self.six_button = Button(master, text=' 6 ', fg='black', bg='red', 
                         command=lambda: self.press(6), height=1, width=7) 
        self.six_button.grid(row=3, column=2) 
    
        self.seven_button = Button(master, text=' 7 ', fg='black', bg='red', 
                         command=lambda: self.press(7), height=1, width=7) 
        self.seven_button.grid(row=4, column=0) 
    
        self.eight_button = Button(master, text=' 8 ', fg='black', bg='red', 
                         command=lambda: self.press(8), height=1, width=7) 
        self.eight_button.grid(row=4, column=1) 
    
        self.nine_button = Button(master, text=' 9 ', fg='black', bg='red', 
                         command=lambda: self.press(9), height=1, width=7) 
        self.nine_button.grid(row=4, column=2) 
    
        self.zero_button = Button(master, text=' 0 ', fg='black', bg='red', 
                         command=lambda: self.press(0), height=1, width=7) 
        self.zero_button.grid(row=5, column=0) 
    
        # Expression buttons
        self.plus_button = Button(master, text=' + ', fg='black', bg='red', 
                      command=lambda: self.press("+"), height=1, width=7) 
        self.plus_button.grid(row=2, column=3) 
    
        self.minus_button = Button(master, text=' - ', fg='black', bg='red', 
                       command=lambda: self.press("-"), height=1, width=7) 
        self.minus_button.grid(row=3, column=3) 
    
        self.multiply_button = Button(master, text=' * ', fg='black', bg='red', 
                          command=lambda: self.press("*"), height=1, width=7) 
        self.multiply_button.grid(row=4, column=3) 
    
        self.divide_button = Button(master, text=' / ', fg='black', bg='red', 
                        command=lambda: self.press("/"), height=1, width=7) 
        self.divide_button.grid(row=5, column=3) 
    
        self.equal_button = Button(master, text=' = ', fg='black', bg='red', 
                       command=self.equalpress, height=1, width=7) 
        self.equal_button.grid(row=5, column=2) 
  
        self.clear_button = Button(master, text='Clear', fg='black', bg='red', 
                       command=self.clear, height=1, width=7) 
        self.clear_button.grid(row=5, column='1')

    def validate(self, d, i, s, S):
        insertion, index, old_text, new_text = bool(int(d)), int(i), s, S
        # print(not insertion, index, old_text, new_text) # Debugging
        
        if insertion:
            allowed_chars = "1234567890()-=+/* ="
            # Insure input is in valid format, including from copy/paste
            for char in new_text:
                if char not in allowed_chars:
                    return False
            return True
        else:
            if old_text[-5:] == " error ":
                self.expression = ""
            elif index == len(old_text)-1:
                self.expression = self.expression[:-1]
            else:
                self.expression = self.expression[:index] + self.expression[index + len(new_text):]
            return True # Allow deletion of validated text 
        
        return True

    # Function to update expressiom 
    # in the text entry box 
    def press(self, num):   
        # concatenation of string 
        self.expression = self.expression + str(num) 
    
        # update the expression by using set method 
        self.equation.set(self.expression)

    # Function to evaluate the final expression 
    def equalpress(self): 
        # Try and except statement is used 
        # for handling the errors like zero 
        # division error etc. 
        try:     
            # eval function evaluate the expression 
            print(self.equation.get())
            self.expression = str(eval(self.equation.get())) 
            self.equation.set(self.expression) 
        # if error is generate then handle 
        # by the except block 
        except ZeroDivisionError:
            self.equation.set(" Divide by zero error ")
            self.expression = ""
        except: 
        
            self.equation.set(" error ") 
            self.expression = "" 
    
    
    # Function to clear the contents 
    # of text entry box 
    def clear(self): 
        self.expression = "" 
        self.equation.set("") 


# create a GUI window 
root = Tk()

# create calculator app object with root
calculatorApp = Calculator(root)

# Start the calculator app
root.mainloop()