import tkinter as tk
import webbrowser
import ctypes
from math import *


# backend:
def github(n):
    webbrowser.open_new('https://github.com/Yue3448')

def copy_x1():
    root.clipboard_clear()
    root.clipboard_append(entry_x1.get())

def copy_x2():
    root.clipboard_clear()
    root.clipboard_append(entry_x2.get())

def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
    except ValueError:
        entry_x1.config(state='normal')
        entry_x1.delete(0, tk.END)
        entry_x1.insert(0, 'None')
        entry_x1.config(state='readonly')

        entry_x2.config(state='normal')
        entry_x2.delete(0, tk.END)
        entry_x2.insert(0, 'None')
        entry_x2.config(state='readonly')

        output_sq.config(state='normal')
        output_sq.delete(0, tk.END)
        output_sq.insert(0, 'No root')
        output_sq.config(state='readonly')

        output_d.config(state='normal')
        output_d.delete(0, tk.END)
        output_d.insert(0, 'None')
        output_d.config(state='readonly')

    discriminant = b ** 2 - 4 * a * c

    output_d.config(state='normal')
    output_d.delete(0, tk.END)
    output_d.insert(0, discriminant)
    output_d.config(state='readonly')

    if discriminant < 0:
        output_d.config(state='normal')
        output_d.delete(0, tk.END)
        output_d.insert(0, 'd < 0')
        output_d.config(state='readonly')

        output_sq.config(state='normal')
        output_sq.delete(0, tk.END)
        output_sq.insert(0, 'No root')
        output_sq.config(state='readonly')

        entry_x1.config(state='normal')
        entry_x1.delete(0, tk.END)
        entry_x1.insert(0, 'None')
        entry_x1.config(state='readonly')

        entry_x2.config(state='normal')
        entry_x2.delete(0, tk.END)
        entry_x2.insert(0, 'None')
        entry_x2.config(state='readonly')

    elif discriminant > 0 and a != 0:
        sq_val = sqrt(discriminant)
        x1 = (-b + sq_val) / (2 * a)
        x2 = (-b - sq_val) / (2 * a)

        output_d.config(state='normal')
        output_d.delete(0, tk.END)
        output_d.insert(0, discriminant)
        output_d.config(state='readonly')

        output_sq.config(state='normal')
        output_sq.delete(0, tk.END)
        output_sq.insert(0, sq_val)
        output_sq.config(state='readonly')

        entry_x1.config(state='normal')
        entry_x1.delete(0, tk.END)
        entry_x1.insert(0, x1)
        entry_x1.config(state='readonly')

        entry_x2.config(state='normal')
        entry_x2.delete(0, tk.END)
        entry_x2.insert(0, x2)
        entry_x2.config(state='readonly')


    elif discriminant == 0 and a != 0:
        sq_val = sqrt(discriminant)
        x1 = -b / (2 * a)

        output_sq.config(state='normal')
        output_sq.delete(0, tk.END)
        output_sq.insert(0, sq_val)
        output_sq.config(state='readonly')

        entry_x1.config(state='normal')
        entry_x1.delete(0, tk.END)
        entry_x1.insert(0, x1)
        entry_x1.config(state='readonly')

        entry_x2.config(state='normal')
        entry_x2.delete(0, tk.END)
        entry_x2.insert(0, 'None')
        entry_x2.config(state='readonly')

    else:
        entry_x1.config(state='normal')
        entry_x1.delete(0, tk.END)
        entry_x1.insert(0, 'None')
        entry_x1.config(state='readonly')

        entry_x2.config(state='normal')
        entry_x2.delete(0, tk.END)
        entry_x2.insert(0, 'None')
        entry_x2.config(state='readonly')

        output_sq.config(state='normal')
        output_sq.delete(0, tk.END)
        output_sq.insert(0, 'No root')
        output_sq.config(state='readonly')


try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass

# window start:
root = tk.Tk()
root.title('QuadSolve')
root.geometry('940x650')
root.resizable(width=False, height=False)

logo_img = tk.PhotoImage(file='QSI.png')

root.iconbitmap('favicon.ico')

logo_label = tk.Label(root, image=logo_img)
logo_label.img = logo_img

# widgets:
formula_box = tk.Label(root, text='d = b² - 4ac', relief='solid', borderwidth=4, padx=10, pady=15, font=('Arial', 35))
info_box = tk.Label(root, text='Info', relief='solid', borderwidth=4, padx=10, pady=15, font=('Arial', 35))

input_frame = tk.Frame(root)

label_a = tk.Label(input_frame, text='Enter a:', font=('Arial', 18))
entry_a = tk.Entry(input_frame, width=25)

label_b = tk.Label(input_frame, text='Enter b:', font=('Arial', 18))
entry_b = tk.Entry(input_frame, width=25)

label_c = tk.Label(input_frame, text='Enter c:', font=('Arial', 18))
entry_c = tk.Entry(input_frame, width=25)

output_frame = tk.Frame(root)

label_d = tk.Label(output_frame, text='Discriminant result:', font=('Arial', 18))
output_d = tk.Entry(output_frame, width=25, state='readonly')

label_sq = tk.Label(output_frame, text='Square root:', font=('Arial', 18))
output_sq = tk.Entry(output_frame, width=25, state='readonly')

result_frame = tk.Frame(root)
label_result = tk.Label(result_frame, text='Result:', font=('Arial', 24))

label_x1 = tk.Label(result_frame, text='x1', font=('Arial', 18))
entry_x1 = tk.Entry(result_frame, width=10, state='readonly')

label_x2 = tk.Label(result_frame, text='x2', font=('Arial', 18))
entry_x2 = tk.Entry(result_frame, width=10, state='readonly')

copy_button_x1 = tk.Button(result_frame, text='copy', font=('Arial', 12), command=copy_x1)
copy_button_x2 = tk.Button(result_frame, text='copy', font=('Arial', 12), command=copy_x2)

label_calc = tk.Button(root, text='Calculate', font=('Arial', 25), command=calculate)
version_label = tk.Label(root, text="version 1.0", font=('Arial', 10))

link_label = tk.Label(root, text='Github', fg='purple', cursor='hand2')
link_label.bind('<Button-1>', github)

# place widgets:
formula_box.grid(row=0, column=0, padx=70, pady=30)
info_box.grid(row=0, column=1, padx=270, pady=30)
input_frame.grid(row=1, column=0, pady=5)

label_a.grid(row=0, column=0, padx=10, pady=20)
entry_a.grid(row=0, column=1, padx=10, pady=20)

label_b.grid(row=1, column=0, padx=10, pady=20)
entry_b.grid(row=1, column=1, padx=10, pady=20)

label_c.grid(row=2, column=0, padx=10, pady=20)
entry_c.grid(row=2, column=1, padx=10, pady=20)

output_frame.grid(row=1, column=1, pady=5, sticky='n')

label_d.grid(row=0, column=0, padx=10, pady=20)
output_d.grid(row=0, column=1, padx=10, pady=20)

label_sq.grid(row=1, column=0, padx=10, pady=20)
output_sq.grid(row=1, column=1, padx=10, pady=20)

result_frame.grid(row=2, column=0, columnspan=2, pady=10, padx=(0, 100))
label_result.grid(row=0, columnspan=4, column=0, pady=(0, 15))

label_x1.grid(row=1, column=0, pady=5)
entry_x1.grid(row=1, column=1, padx=(10, 30))

label_x2.grid(row=1, column=2, padx=5)
entry_x2.grid(row=1, column=3, padx=5)

copy_button_x1.grid(row=2, column=1, sticky='w', padx=(10, 0), pady=(5, 0))
copy_button_x2.grid(row=2, column=3, sticky='w', padx=5, pady=(5, 0))


label_calc.grid(row=2, column=1, sticky='se', padx=200, pady=30)
logo_label.grid(row=2, column=0, padx=(0, 70))

link_label.place(rely=1.0, anchor='sw', x=10, y=-10)
version_label.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

root.mainloop()