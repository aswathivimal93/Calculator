from tkinter import *

window = Tk()
# window.geometry("500x500")
window.title("Calculator")
window.geometry("500x500")


# num=StringVar()
def number_entry(num):
    x = str(disp.get())

    expression = str(disp.get()) + str(num)
    if  not inputvar:
        input_text.set(expression)
    else:
        input_text.set("")
        input_text.set(str(num))
        inputvar.clear()





def operator_entry(ope):
    print(result_text)
    if result_text and not operator_text:
        result_text.append(input_text.get())
        print(result_text)
        operator_text.append(ope)
        inputvar.append(1)
    elif result_text:
        
        print("in if")
        #temp = input_text.get()
        #print(temp)
        math = str(result_text[0]) + operator_text[0] + str(input_text.get())
        print(eval(math))
        result_text[0] = eval(math)
        input_text.set(eval(math))
        inputvar.append(1)

        print(result_text)
        operator_text[0] = ope
    else:
        result_text.append(int(input_text.get()))
        print(result_text)
        operator_text.append(ope)
        inputvar.append(1)

def equal_entry(ope):
    math = str(result_text[0]) + operator_text[0] + str(input_text.get())
    result_text[0] = eval(math)
    input_text.set(eval(math))
    operator_text.clear()
    inputvar.append(1)
    print(result_text)
    print(operator_text)
    print(input_text.get())
def clear_entry():
    input_text.set("")
    result_text.clear()
    operator_text.clear()
    inputvar.clear()
inputvar = []
result_text = []
input_text = StringVar()
operator_text = []
disp = Entry(window, state='readonly', readonlybackground="white", width=40, textvariable=input_text)
disp.grid(row=0, column=0, columnspan=4)

clear_btn = Button(window, text="C", width=16, height=5,command=lambda: clear_entry())
clear_btn.grid(row=1, column=0)
division_btn = Button(window, text="/", width=16, height=5, command=lambda: operator_entry('/'))
division_btn.grid(row=1, column=1)
mul_btn = Button(window, text="*", width=16, height=5, command=lambda: operator_entry('*'))
mul_btn.grid(row=1, column=2)
sub_btn = Button(window, text="-", width=16, height=5, command=lambda: operator_entry('-'))
sub_btn.grid(row=1, column=3)

seven_btn = Button(window, text="7", width=16, height=5, command=lambda: number_entry(7))
seven_btn.grid(row=2, column=0)
eight_btn = Button(window, text="8", width=16, height=5, command=lambda: number_entry(8))
eight_btn.grid(row=2, column=1)
nine_btn = Button(window, text="9", width=16, height=5, command=lambda: number_entry(9))
nine_btn.grid(row=2, column=2)
add_btn = Button(window, text="+", width=16, height=11, command=lambda: operator_entry('+'))
add_btn.grid(row=2, column=3, rowspan=2)

four_btn = Button(window, text="4", width=16, height=5, command=lambda: number_entry(4))
four_btn.grid(row=3, column=0)
five_btn = Button(window, text="5", width=16, height=5, command=lambda: number_entry(5))
five_btn.grid(row=3, column=1)
six_btn = Button(window, text="6", width=16, height=5, command=lambda: number_entry(6))
six_btn.grid(row=3, column=2)

one_btn = Button(window, text="1", width=16, height=5, command=lambda: number_entry(1))
one_btn.grid(row=4, column=0)
two_btn = Button(window, text="2", width=16, height=5, command=lambda: number_entry(2))
two_btn.grid(row=4, column=1)
three_btn = Button(window, text="3", width=16, height=5, command=lambda: number_entry(3))
three_btn.grid(row=4, column=2)
equal_btn = Button(window, text="=", width=16, height=11,command=lambda:equal_entry('='))
equal_btn.grid(row=4, column=3, rowspan=2)

zero_btn = Button(window, text="0", width=33, height=5, command=lambda: number_entry(0))
zero_btn.grid(row=5, column=0, columnspan=2)
dot_btn = Button(window, text=".", width=16, height=5)
dot_btn.grid(row=5, column=2)

window.mainloop()
