from tkinter import *
from tkinter import font as font
from tkinter import ttk
from re import compile, search
from verticalScrolledFrame import *
import decimal


class Calculator():

    # Precompile object used for refrence for valid input
    # Only accepts: numers '0-9', operations '+ * / -', parathesis '()', decimal '.', 
    invalid_input = re.compile('[^0-9*/+\-().e ]')
    # Holds previous equations and answers
    history_buttons = []

    def __init__(self, master):
        """
            Calculator constructor

            Inputs:
                @ master(TK Frame): Root TKinter Frame
        """
        self.master = master
        # set the title of GUI window 
        self.master.title("Calculator") 
        # set the minimum size of app
        self.master.minsize(242, 250)

        # Main calculator frame (equation and buttons)
        self.calculator_frame=Frame(self.master, borderwidth=5, relief="sunken")
        self.calculator_frame.pack(side=LEFT, fill=BOTH, expand=True)
        
        # Frame used to hold equation entry box
        self.equation_frame = Frame(self.calculator_frame)
        self.equation_frame.pack(side=TOP, fill=X)
        # Entry box for calculator input and string variable to holds its value
        self.equation = StringVar("")
        vcmd = master.register(self.validate) # wrapper for validation function to insure clean input
        self.equation_field = Entry(self.equation_frame, textvariable=self.equation, borderwidth=5, relief="sunken", font=10,
            validate="key", validatecommand=(vcmd, '%d', '%S'))
        self.equation_field.focus_set() # Puts entry box in focus for easier input from keyboard
        self.equation_field.pack(fill=X) # Stretch input box to size of calculator frame

        # frame to hold all number and expression buttons
        self.buttons_frame = Frame(self.calculator_frame, borderwidth=5)
        self.buttons_frame.pack(side=TOP, fill=BOTH, expand=True) # Fill and scale for resizing
        # Number buttons
        # Lambda functions used to pass variable for number pressed
        self.one_button = Button(self.buttons_frame, text=' 1 ', fg='black', bg='red', activebackground='green',
            borderwidth=3, relief='raised', font=5, padx=10, pady=10,
                command=lambda: self.press('1')) 
        self.one_button.grid(row=0, column=0, sticky='NESW') 
        self.two_button = Button(self.buttons_frame, text=' 2 ', fg='black', bg='red', activebackground='green',
            borderwidth=3, relief='raised', font=5, padx=10, pady=10,
                command=lambda: self.press('2')) 
        self.two_button.grid(row=0, column=1, sticky='NESW') 
        self.three_button = Button(self.buttons_frame, text=' 3 ', fg='black', bg='red', activebackground='green',
            borderwidth=3, relief='raised', font=5, padx=10, pady=10,
                command=lambda: self.press('3')) 
        self.three_button.grid(row=0, column=2, sticky='NESW') 
        self.four_button = Button(self.buttons_frame, text=' 4 ', fg='black', bg='red', activebackground='green',
            borderwidth=3, relief='raised', font=5, padx=10, pady=10,
                command=lambda: self.press('4')) 
        self.four_button.grid(row=1, column=0, sticky='NESW') 
        self.five_button = Button(self.buttons_frame, text=' 5 ', fg='black', bg='red', activebackground='green',
            borderwidth=3, relief='raised', font=5, padx=10, pady=10,
                command=lambda: self.press('5')) 
        self.five_button.grid(row=1, column=1, sticky='NESW') 
        self.six_button = Button(self.buttons_frame, text=' 6 ', fg='black', bg='red', activebackground='green',
            borderwidth=3, relief='raised', font=5, padx=10, pady=10,
                command=lambda: self.press('6')) 
        self.six_button.grid(row=1, column=2, sticky='NESW') 
        self.seven_button = Button(self.buttons_frame, text=' 7 ', fg='black', bg='red', activebackground='green',
            borderwidth=3, relief='raised', font=5, padx=10, pady=10,
                command=lambda: self.press('7')) 
        self.seven_button.grid(row=2, column=0, sticky='NESW') 
        self.eight_button = Button(self.buttons_frame, text=' 8 ', fg='black', bg='red', activebackground='green',
            borderwidth=3, relief='raised', font=5, padx=10, pady=10,
                command=lambda: self.press('8')) 
        self.eight_button.grid(row=2, column=1, sticky='NESW') 
        self.nine_button = Button(self.buttons_frame, text=' 9 ', fg='black', bg='red', activebackground='green',
            borderwidth=3, relief='raised', font=5, padx=10, pady=10,
                command=lambda: self.press('9')) 
        self.nine_button.grid(row=2, column=2, sticky='NESW') 
        self.zero_button = Button(self.buttons_frame, text=' 0 ', fg='black', bg='red', activebackground='green',
            borderwidth=3, relief='raised', font=5, padx=10, pady=10,
                command=lambda: self.press('0')) 
        self.zero_button.grid(row=3, column=0, sticky='NESW') 
        # Expression buttons
        self.plus_button = Button(self.buttons_frame, text=' + ', fg='black', bg='red', activebackground='green',
            borderwidth=3, relief='raised', font=5, padx=10, pady=10,
                command=lambda: self.press("+")) 
        self.plus_button.grid(row=0, column=3, sticky='NESW') 
        self.minus_button = Button(self.buttons_frame, text=' - ', fg='black', bg='red', activebackground='green',
            borderwidth=3, relief='raised', font=5, padx=10, pady=10,
                command=lambda: self.press("-")) 
        self.minus_button.grid(row=1, column=3, sticky='NESW') 
        self.multiply_button = Button(self.buttons_frame, text=' * ', fg='black', bg='red', activebackground='green',
            borderwidth=3, relief='raised', font=5, padx=10, pady=10,
                command=lambda: self.press("*")) 
        self.multiply_button.grid(row=2, column=3, sticky='NESW') 
        self.divide_button = Button(self.buttons_frame, text=' / ', fg='black', bg='red', activebackground='green',
            borderwidth=3, relief='raised', font=5, padx=10, pady=10,
                         command=lambda: self.press("/")) 
        self.divide_button.grid(row=3, column=3, sticky='NESW')  
        self.clear_button = Button(self.buttons_frame, text='Clr', fg='black', bg='red', activebackground='green',
            borderwidth=3, relief='raised', font=5, padx=10, pady=10,
                         command=self.clear) 
        self.clear_button.grid(row=3, column='1', sticky='NESW')
        self.equal_button = Button(self.buttons_frame, text=' = ', fg='black', bg='red', activebackground='green',
            borderwidth=3, relief='raised', font=5, padx=10, pady=10,
                command=self.equalpress)
        self.equal_button.grid(row=3, column=2, sticky='NESW')
        # Bind enter press to same function as equal_button
        self.master.bind('<Return>', lambda event: self.equalpress()) 
        # Configure grid of buttons to scale to size of containing frame
        self.buttons_frame.rowconfigure(0, weight=1)
        self.buttons_frame.columnconfigure(0, weight=1)
        self.buttons_frame.rowconfigure(1, weight=1)
        self.buttons_frame.columnconfigure(1, weight=1)
        self.buttons_frame.rowconfigure(2, weight=1)
        self.buttons_frame.columnconfigure(2, weight=1)
        self.buttons_frame.rowconfigure(3, weight=1)
        self.buttons_frame.columnconfigure(3, weight=1)

        # Frame for history of calculations
        # Clear history button and labels for previous equation and answer columns
        self.history_frame = Frame(self.master)
        self.history_frame.pack(side=RIGHT, fill=BOTH)
        self.clear_history_button = Button(self.history_frame, text='Clear History', fg='black', bg='red', activebackground='green', relief='raised', font=5,
            command=self.clear_history)
        self.clear_history_button.pack(side=TOP, anchor=W)

        self.history_list_frame = VerticalScrolledFrame(self.history_frame, bg='pink')
        self.history_list_frame.pack(fill=BOTH, expand=1)
        
    # Validate user input for equation
    # Checks on per character insertion or deletion
    # Allows for multi character insertion or deletion
    # input:
    #   @addition(str): 1 for addition, 0 for deletion, -1 for neither
    #   @modified_text(str): string user either added or removed
    # return:
    #   Returns True if input in valid, else false
    def validate(self, addition, modified_text):
        if addition == '1':
            # Check if inputed text contains invalid characters
            if self.invalid_input.search(modified_text):
                return False
        return True

    # Function that handles when user pressed button
    # Adds value to equation entry field
    # input:
    #   @num(str): Number or expression (+-*/) from button user pressed
    def press(self, num):   
        self.equation_field.insert(END, str(num))

    # Function to evaluate the final expression 
    def equalpress(self): 
        # Try and except statement is used 
        # for handling the errors like zero 
        # division error etc. 
        try:   
            # equation to be evaluated  
            equation = self.equation.get().replace(" ", "")
            # Return if equation entry is empty, avoid error
            if equation == "":
                self.equation.set("") # Reset equation entry box (incase spaces)
                return
            else: 
                # evaluate equation and save to variable
                total_num = eval(equation)
                if total_num > 999999999999:
                    total = str(format(decimal.Decimal(total_num), '.6e'))
                else:
                    total = str(total_num)
                # Add the equation and answer to history list
                self.add_to_history(equation, total) 
                self.equation.set("") # Reset equation entry box
                
        # Divide by zero error
        except ZeroDivisionError:
            self.equation.set(" Divide by zero error")
        except:       
            self.equation.set("error")

        # Set cursor to after last value
        self.equation_field.icursor("end")
    
    
    # Adds an equation and answer to history list
    def add_to_history(self, equation, answer):
        # Frame to hold equation and answer in history
        history_input_frame = Frame(self.history_list_frame.interior, borderwidth=5, highlightbackground='green', highlightthickness=2)
        history_input_frame.pack(anchor=E, fill=X, expand=True)
        # Add to history, change color to mark as last addition
        #self.history_buttons[-1].Configure(borderwidth=10)
        if len(self.history_buttons) > 1:
            self.history_buttons[-2].configure(highlightthickness=0)
        # Equation Button (left)
        button1 = Button(history_input_frame, text=equation+'=', relief='flat', anchor=E,
            command=lambda: self.equation_field.insert(END, equation))
        button1['font'] = font.Font(family='Helvetica', size=10)
        button1.pack(side=TOP, anchor=E, fill=X)
        # Answer Button (right)
        button2 = Button(history_input_frame, text=answer, relief='flat', anchor=E,
            command=lambda: self.equation_field.insert(END, answer))
        button2['font'] = font.Font(family='Helvetica', size=15, weight='bold')
        button2.pack(side=BOTTOM, anchor=E)
        # Add equation and answer to history
        # Inserting new entries at top
        self.history_buttons.append(history_input_frame)
        for frame in reversed(self.history_buttons):
            frame.pack_forget() # Forget frame to re-order
            frame.pack(anchor=E)
        
        #self.history_buttons[-1].Configure(borderwidth=10)
        if len(self.history_buttons) > 1:
            self.history_buttons[-2].configure(highlightthickness=0)

        
                  
    # Function to clear the contents 
    # of text entry box 
    def clear(self): 
        self.equation.set("") 

    # Function to clear history of previous answers
    def clear_history(self):
        hist_list = self.history_list_frame.interior.pack_slaves()
        # Already empty
        if hist_list == None:
            return
        for frame in hist_list:
            frame.destroy()
        self.history_buttons = []

# create a GUI window 
root = Tk()

# create calculator app object with root
calculatorApp = Calculator(root)

# Start the calculator app
root.mainloop()