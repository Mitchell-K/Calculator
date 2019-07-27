from tkinter import *
from re import compile, search

class Calculator():

    # Precompile object used for refrence for valid input
    # Only accepts: numers '0-9', operations '+ * / -', parathesis '()', decimal '.'
    invalid_input = re.compile('[^0-9*/+\-().]')

    history_buttons = []

    def __init__(self, master):
        self.master = master
        # set the title of GUI window 
        self.master.title("Calculator") 
        # set the configuration size of GUI window 
        #self.master.geometry("600x400")
        self.master.minsize(242, 250)

        # Main calculator frame (equation and buttons)
        self.calculator_frame=Frame(self.master, borderwidth=5, relief="sunken", width=400, height=400)
        self.calculator_frame.pack(side=LEFT, fill=BOTH, expand=True)

        self.equation_frame = Frame(self.calculator_frame)
        self.equation_frame.pack(side=TOP, fill=X)

        self.equation = StringVar("")
        vcmd = master.register(self.validate) # we have to wrap the command
        self.equation_field = Entry(self.equation_frame, textvariable=self.equation, borderwidth=5, relief="sunken", font=10,
            validate="key", validatecommand=(vcmd, '%d', '%S'))
        self.equation_field.focus_set()
        self.equation_field.pack(fill=X)

        # Frame for history of calculations
        self.history_frame = Frame(self.master)
        self.history_frame.pack(side=RIGHT, fill=BOTH)
        #self.history_frame.columnconfigure(0, weight=1)
        #self.history_frame.columnconfigure(1, weight=1)

        self.clear_history_button = Button(self.history_frame, text='Clear History', fg='black', bg='red', relief='raised', font=5,
            command=self.clear_history) 
        self.clear_history_button.grid(row=0, column=0, columnspan=2)
        self.equation_label = Label(self.history_frame, text="Equation:", font=5, borderwidth=5)
        self.equation_label.grid(row=1, column=0, sticky='WE')
        self.answer_label = Label(self.history_frame, text="Answer:", font=5, borderwidth=5)
        self.answer_label.grid(row=1, column=1, sticky='WE')


        self.buttons_frame = Frame(self.calculator_frame, borderwidth=5)
        self.buttons_frame.pack(side=TOP, fill=BOTH, expand=True)

        # Number buttons
        self.one_button = Button(self.buttons_frame, text=' 1 ', fg='black', bg='red', borderwidth=3, relief='raised', font=5,
                         command=lambda: self.press(1)) 
        self.one_button.grid(row=0, column=0, sticky='NESW') 
        self.two_button = Button(self.buttons_frame, text=' 2 ', fg='black', bg='red', borderwidth=3, relief='raised', font=5,
                         command=lambda: self.press(2)) 
        self.two_button.grid(row=0, column=1, sticky='NESW') 
        self.three_button = Button(self.buttons_frame, text=' 3 ', fg='black', bg='red', borderwidth=3, relief='raised', font=5,
                         command=lambda: self.press(3)) 
        self.three_button.grid(row=0, column=2, sticky='NESW') 
        self.four_button = Button(self.buttons_frame, text=' 4 ', fg='black', bg='red', borderwidth=3, relief='raised', font=5,
                         command=lambda: self.press(4)) 
        self.four_button.grid(row=1, column=0, sticky='NESW') 
        self.five_button = Button(self.buttons_frame, text=' 5 ', fg='black', bg='red', borderwidth=3, relief='raised', font=5,
                         command=lambda: self.press(5)) 
        self.five_button.grid(row=1, column=1, sticky='NESW') 
        self.six_button = Button(self.buttons_frame, text=' 6 ', fg='black', bg='red', borderwidth=3, relief='raised', font=5,
                         command=lambda: self.press(6)) 
        self.six_button.grid(row=1, column=2, sticky='NESW') 
        self.seven_button = Button(self.buttons_frame, text=' 7 ', fg='black', bg='red', borderwidth=3, relief='raised', font=5,
                         command=lambda: self.press(7)) 
        self.seven_button.grid(row=2, column=0, sticky='NESW') 
        self.eight_button = Button(self.buttons_frame, text=' 8 ', fg='black', bg='red', borderwidth=3, relief='raised', font=5,
                         command=lambda: self.press(8)) 
        self.eight_button.grid(row=2, column=1, sticky='NESW') 
        self.nine_button = Button(self.buttons_frame, text=' 9 ', fg='black', bg='red', borderwidth=3, relief='raised', font=5,
                         command=lambda: self.press(9)) 
        self.nine_button.grid(row=2, column=2, sticky='NESW') 
        self.zero_button = Button(self.buttons_frame, text=' 0 ', fg='black', bg='red', borderwidth=3, relief='raised', font=5,
                         command=lambda: self.press(0)) 
        self.zero_button.grid(row=3, column=0, sticky='NESW') 
        # Expression buttons
        self.plus_button = Button(self.buttons_frame, text=' + ', fg='black', bg='red', borderwidth=3, relief='raised', font=5,
                         command=lambda: self.press("+")) 
        self.plus_button.grid(row=0, column=3, sticky='NESW') 
        self.minus_button = Button(self.buttons_frame, text=' - ', fg='black', bg='red', borderwidth=3, relief='raised', font=5,
                         command=lambda: self.press("-")) 
        self.minus_button.grid(row=1, column=3, sticky='NESW') 
        self.multiply_button = Button(self.buttons_frame, text=' * ', fg='black', bg='red', borderwidth=3, relief='raised', font=5,
                         command=lambda: self.press("*")) 
        self.multiply_button.grid(row=2, column=3, sticky='NESW') 
        self.divide_button = Button(self.buttons_frame, text=' / ', fg='black', bg='red', borderwidth=3, relief='raised', font=5,
                         command=lambda: self.press("/")) 
        self.divide_button.grid(row=3, column=3, sticky='NESW') 
        self.equal_button = Button(self.buttons_frame, text=' = ', fg='black', bg='red', borderwidth=3, relief='raised', font=5,
                         command=self.equalpress)
        self.equal_button.grid(row=3, column=2, sticky='NESW') 
        self.clear_button = Button(self.buttons_frame, text='Clear', fg='black', bg='red', borderwidth=3, relief='raised', font=5,
                         command=self.clear) 
        self.clear_button.grid(row=3, column='1', sticky='NESW')
        # Bind enter press to same function as equal_button
        master.bind('<Return>', lambda event: self.equalpress()) 

        self.buttons_frame.rowconfigure(0, weight=1)
        self.buttons_frame.columnconfigure(0, weight=1)
        self.buttons_frame.rowconfigure(1, weight=1)
        self.buttons_frame.columnconfigure(1, weight=1)
        self.buttons_frame.rowconfigure(2, weight=1)
        self.buttons_frame.columnconfigure(2, weight=1)
        self.buttons_frame.rowconfigure(3, weight=1)
        self.buttons_frame.columnconfigure(3, weight=1)

    def validate(self, addition, modified_text):
        if addition == '1':
            # Check if inputed text contains invalid characters
            if self.invalid_input.search(modified_text):
                return False
        return True

    # Function to update expression 
    # in the text entry box 
    def press(self, num):   
        self.equation_field.insert(END, str(num))

    # Function to evaluate the final expression 
    def equalpress(self): 
        # Try and except statement is used 
        # for handling the errors like zero 
        # division error etc. 
        try:     
            # eval function evaluate the expression 
            #print(self.equation.get()) # For debugging
            if self.equation.get() == "":
                self.equation.set("0")
            else: 
                equation = self.equation.get()
                total = str(eval(equation))
                self.equation.set("")
                history_length = len(self.history_buttons)
                butt1 = Button(self.history_frame, text=equation+'=', bg='teal', borderwidth=3, relief='groove', font=5, anchor=E,
                    command=lambda: self.equation_field.insert(END, equation))
                butt1.grid(row=(history_length%4 +2), sticky='WE')
                butt2 = Button(self.history_frame, text=total, bg='teal', borderwidth=3, relief='groove', font=5, anchor=W,
                    command=lambda: self.equation_field.insert(END, str(total)))
                butt2.grid(row=(history_length%4 +2), column=1, sticky='WE')
                self.history_buttons.append([butt1, butt2])
                if history_length >= 1:
                    self.history_buttons[history_length-1][0].configure(bg="SystemButtonFace")
                    self.history_buttons[history_length-1][1].configure(bg="SystemButtonFace")
                
        # if error is generate then handle 
        # by the except block 
        except ZeroDivisionError:
            self.equation.set(" Divide by zero error")
        except:       
            self.equation.set("error")

        # Set cursor to after last value
        self.equation_field.icursor("end")
    
    
    # Function to clear the contents 
    # of text entry box 
    def clear(self): 
        self.equation.set("") 

    def clear_history(self):
        if self.history_buttons == []:
            return
        for but in self.history_buttons:
            but[0].destroy()
            but[1].destroy()
        self.history_buttons = []


# create a GUI window 
root = Tk()

# create calculator app object with root
calculatorApp = Calculator(root)

# Start the calculator app
root.mainloop()