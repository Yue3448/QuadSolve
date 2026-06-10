import tkinter as tk
import webbrowser
import ctypes
from math import *
import cmath
from tkinter import messagebox


# Backend:
def github(n):
    webbrowser.open_new('https://github.com/Yue3448')


def copy_x1():
    root.clipboard_clear()
    root.clipboard_append(entry_x1.get())


def copy_x2():
    root.clipboard_clear()
    root.clipboard_append(entry_x2.get())


def copy_sq():
    root.clipboard_clear()
    root.clipboard_append(output_sq.get())


def step_by_step(text):
    output_main.config(state='normal')
    output_main.delete('1.0', tk.END)
    output_main.insert('1.0', text)
    output_main.config(state='normal')

def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
    except ValueError:
        messagebox.showerror('ERROR', 'Error! Try input number.')
        return

    discriminant = b ** 2 - 4 * a * c

    output_d.config(state='normal')
    output_d.delete(0, tk.END)
    output_d.insert(0, discriminant)
    output_d.config(state='readonly')

    if discriminant < 0 and a != 0:
        sq_val_complex = cmath.sqrt(discriminant)
        x1 = (-b + sq_val_complex) / (2 * a)
        x2 = (-b - sq_val_complex) / (2 * a)

        x1_real = x1.real
        x1_imag = abs(x1.imag)

        x2_real = x2.real
        x2_imag = abs(x2.imag)

        entry_x1.config(state='normal')
        entry_x1.delete(0, tk.END)
        entry_x1.insert(0, f'{x1_real} + {x1_imag}i')
        entry_x1.config(state='readonly')

        entry_x2.config(state='normal')
        entry_x2.delete(0, tk.END)
        entry_x2.insert(0, f'{x2_real} - {x2_imag}i')
        entry_x2.config(state='readonly')

        output_sq.config(state='normal')
        output_sq.delete(0, tk.END)
        output_sq.insert(0, str(sq_val_complex)[:-1:] + 'i')
        output_sq.config(state='readonly')

        step_by_step(
            f'D = {b**2} - 4 * {a} * {c} = {b**2 - 4 * a * c}\n'
            '\n'
            f'D < 0 => x = (-b ± i√|D|) / (2 * a)\n'
            '\n'
            f'x1 = ({-b} + i√|{discriminant}|) / (2 * {a}) = {str(x1)[:-2:] + 'i' + ')'}\n'
            '\n'
            f'x2 = ({-b} - i√|{discriminant}|) / (2 * {a}) = {str(x2)[:-2:] + 'i' + ')'}\n'
        )

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

        step_by_step(
            f'D = {b**2} - 4 * {a} * {c} = {b**2 - 4 * a * c}\n'
            '\n'
            f'√D = {sq_val}\n'
            '\n'
            f'x1 = ({-b} + {sq_val}) / (2 * {a}) = {x1}\n'
            '\n'
            f'x2 = ({-b} - {sq_val}) / (2 * {a}) = {x2}\n'
        )

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

        step_by_step(
            f'D = {b ** 2} - 4 * {a} * {c} = {b ** 2 - 4 * a * c}\n'
            '\n'
            f'D < 0 => x = -b / (2 * a)\n'
            '\n'
            f'x = {-b} / (2 * {a}) = {x1}'
        )


    else:
        output_d.config(state='normal')
        output_d.delete(0, tk.END)
        output_d.insert(0, 'None')
        output_d.config(state='readonly')

        output_sq.config(state='normal')
        output_sq.delete(0, tk.END)
        output_sq.insert(0, 'a = 0')
        output_sq.config(state='readonly')

        entry_x1.config(state='normal')
        entry_x1.delete(0, tk.END)
        entry_x1.insert(0, 'None')
        entry_x1.config(state='readonly')

        entry_x2.config(state='normal')
        entry_x2.delete(0, tk.END)
        entry_x2.insert(0, 'None')
        entry_x2.config(state='readonly')

        step_by_step(
            'This is a linear equation.'
        )

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass

# Window start:
root = tk.Tk()
root.title('QuadSolve')
root.geometry('800x480')
root.resizable(width=False, height=False)
root.grid_columnconfigure(0, weight=0)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=0)
root.grid_rowconfigure(1, weight=1)

logo_img = tk.PhotoImage(file='QSI.png')

root.iconbitmap('favicon.ico')

logo_label = tk.Label(root, image=logo_img)
logo_label.img = logo_img

# Widgets:
formula_box = tk.Label(
    root, text='d = b² - 4ac', relief='solid', borderwidth=1,
    padx=12, pady=8, font=('Arial', 18), bg='white',
)
input_frame = tk.Frame(root)

label_a = tk.Label(input_frame, text='a =', font=('Arial', 14, 'bold'))
entry_a = tk.Entry(input_frame, width=12, font=('Arial', 14), relief='solid', bd=1)

label_b = tk.Label(input_frame, text='b =', font=('Arial', 14, 'bold'))
entry_b = tk.Entry(input_frame, width=12, font=('Arial', 14), relief='solid', bd=1)

label_c = tk.Label(input_frame, text='c =', font=('Arial', 14, 'bold'))
entry_c = tk.Entry(input_frame, width=12, font=('Arial', 14), relief='solid', bd=1)

output_main = tk.Text(
    root, width=40, height=10, font=('Arial', 13), relief='solid', bd=1,
    wrap='word', state='disabled', bg='white',
)

right_frame = tk.Frame(root)

info_box = tk.Label(
    right_frame, text='Info', relief='solid', borderwidth=1,
    padx=8, pady=4, font=('Arial', 12),
)

label_d = tk.Label(right_frame, text='Discriminant', font=('Arial', 13))
output_d = tk.Entry(right_frame, width=18, state='readonly', font=('Arial', 14), relief='solid', bd=1)

label_sq = tk.Label(right_frame, text='Square root', font=('Arial', 13))
output_sq = tk.Entry(right_frame, width=18, state='readonly', font=('Arial', 14), relief='solid', bd=1)
copy_button_sq = tk.Button(right_frame, text='Copy', font=('Arial', 11), command=copy_sq)

result_frame = tk.LabelFrame(root, text='Result', font=('Arial', 14, 'bold'), padx=12, pady=8)

label_x1 = tk.Label(result_frame, text='x1', font=('Arial', 13))
entry_x1 = tk.Entry(result_frame, width=18, state='readonly', font=('Arial', 14), relief='solid', bd=1)

label_x2 = tk.Label(result_frame, text='x2', font=('Arial', 13))
entry_x2 = tk.Entry(result_frame, width=18, state='readonly', font=('Arial', 14), relief='solid', bd=1)

copy_button_x1 = tk.Button(result_frame, text='Copy', font=('Arial', 11), command=copy_x1)
copy_button_x2 = tk.Button(result_frame, text='Copy', font=('Arial', 11), command=copy_x2)

label_calc = tk.Button(root, text='Calculate', font=('Arial', 16, 'bold'), command=calculate, relief='solid', bd=1)
version_label = tk.Label(root, text='v1.0.2', font=('Arial', 10), fg='gray')

link_label = tk.Label(root, text='Github', fg='purple', cursor='hand2')
link_label.bind('<Button-1>', github)

input_frame.grid(row=0, column=0, rowspan=4, sticky='nw', padx=(20, 10), pady=(95, 0))

label_a.grid(row=0, column=0, sticky='e', padx=(0, 8), pady=10)
entry_a.grid(row=0, column=1, sticky='w', pady=10)

label_b.grid(row=1, column=0, sticky='e', padx=(0, 8), pady=10)
entry_b.grid(row=1, column=1, sticky='w', pady=10)

label_c.grid(row=2, column=0, sticky='e', padx=(0, 8), pady=10)
entry_c.grid(row=2, column=1, sticky='w', pady=10)

formula_box.grid(row=0, column=1, sticky='n', pady=(20, 8), padx=10)
output_main.grid(row=1, column=1, rowspan=3, sticky='nsew', padx=10, pady=(0, 10))

right_frame.grid(row=0, column=2, rowspan=4, sticky='ne', padx=(10, 20), pady=(90, 0))

label_d.grid(row=0, column=0, sticky='w', pady=(0, 2))
output_d.grid(row=1, column=0, sticky='ew', pady=(0, 18))
label_sq.grid(row=2, column=0, sticky='w', pady=(0, 2))
output_sq.grid(row=3, column=0, sticky='ew')
copy_button_sq.grid(row=4, column=0, pady=(6, 0))

label_d.grid(row=1, column=0, sticky='w', pady=(0, 2))
output_d.grid(row=2, column=0, sticky='ew', pady=(0, 18))
label_sq.grid(row=3, column=0, sticky='w', pady=(0, 2))
output_sq.grid(row=4, column=0, sticky='ew')
copy_button_sq.grid(row=5, column=0, pady=(6, 0))

logo_label.grid(row=4, column=0, sticky='sw', padx=20, pady=(10, 35))

result_frame.grid(row=4, column=1, sticky='n', pady=(10, 35), padx=10)
result_frame.grid_columnconfigure(0, weight=1)
result_frame.grid_columnconfigure(1, weight=1)

label_x1.grid(row=0, column=0, pady=(0, 4))
entry_x1.grid(row=1, column=0, padx=(0, 15), sticky='ew')
copy_button_x1.grid(row=2, column=0, pady=(6, 0))

label_x2.grid(row=0, column=1, pady=(0, 4))
entry_x2.grid(row=1, column=1, padx=(15, 0), sticky='ew')
copy_button_x2.grid(row=2, column=1, pady=(6, 0))

label_calc.grid(row=4, column=2, sticky='ne', padx=(0, 20), pady=(10, 35), ipadx=20, ipady=25)

link_label.grid(row=5, column=0, sticky='sw', padx=15, pady=(0, 8))
version_label.grid(row=5, column=2, sticky='se', padx=15, pady=(0, 8))

root.mainloop()