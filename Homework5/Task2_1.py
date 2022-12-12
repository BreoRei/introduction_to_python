import tkinter as tk
from tkinter import messagebox as mesg
from random import randint


def add_digit(digit):
    candys = candy_counter.get()
    value = player_field.get()
    if int(candys) < int(digit) and value == 'от 1 до 28':
        mesg.showinfo('Внимание', f'Конфет осталось {candys}')
    elif value != 'от 1 до 28' and int(candys) < int(value + digit):
        mesg.showinfo('Внимание', f'Конфет осталось {candys}')
    elif value == 'от 1 до 28':
        value = str(digit)
    elif value == '0':
        value = str(digit)
    elif len(value) < 2:
        value += str(digit)
        if int(value) > 28:
            mesg.showinfo('Внимание', 'Будет больше 28 конфет')
            value = value[0]
    else:
        mesg.showinfo('Внимание', 'Будет больше 28 конфет')
    player_field['state'] = tk.NORMAL
    player_field.delete(0, tk.END)
    player_field.insert(0, value)
    player_field['state'] = tk.DISABLED


def add_clear():
    value = player_field.get()
    player_field['state'] = tk.NORMAL
    player_field.delete(0, tk.END)
    player_field.insert(0, 'от 1 до 28')
    player_field['state'] = tk.DISABLED


def computer_walks():
    candys = candy_counter.get()
    if candys == '0':
        mesg.showinfo('Ванилопа-Фон-Кекс', f'Неееет...\nЗабирай конфеты, ты победил.')
        root.destroy()
    else:
        value = randint(1, 28) if int(candys) > 28 else candys
        candy_counter['state'] = tk.NORMAL
        candy_counter.delete(0, tk.END)
        candys = int(candys) - int(value)
        candy_counter.insert(0, candys)
        candy_counter['state'] = tk.DISABLED
        mesg.showinfo('Ванилопа-Фон-Кекс', f'Я взяла из кучи {value} конфет')
        if candys == 0:
            mesg.showinfo('Ванилопа-Фон-Кекс', f'Хи-хи-хи я победила.\nВсе конфеты мои!!!')
            root.destroy()


def add_operation():
    value = player_field.get()
    candys = candy_counter.get()
    try:
        candys = int(candys) - int(value)
        player_field['state'] = tk.NORMAL
        candy_counter['state'] = tk.NORMAL
        player_field.delete(0, tk.END)
        candy_counter.delete(0, tk.END)
        candy_counter.insert(0, candys)
        player_field.insert(0, 'от 1 до 28')
        player_field['state'] = tk.DISABLED
        candy_counter['state'] = tk.DISABLED
        computer_walks()
    except (ValueError, SyntaxError):
        mesg.showinfo('Внимание', 'Нужны только цифры')
        player_field['state'] = tk.NORMAL
        player_field.delete(0, tk.END)
        player_field.insert(0, 'от 1 до 28')
        player_field['state'] = tk.DISABLED


def make_digit_buttom(digit):
    return tk.Button(text=digit, bd=5, bg="#22D822", font=("Arial bold", 12), command=lambda: add_digit(digit))


def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char == '\r':
        add_operation()


root = tk.Tk()
root.title("Игра конфетки")
root.geometry('300x250+450+150')
root['bg'] = '#FA8072'
root.resizable(False, False)
root.bind('<Key>', press_key)

candys = tk.Label(root, text="Конфеты", bg="#832EF2", fg='#8AED63', font=("Arial 14 bold"))
candys.grid(column=0, row=0, columnspan=2, stick='wens', padx=5)
candy_counter = tk.Entry(root, justify=tk.CENTER, bg="#C942F2", fg='#8AED63', font=("Arial 18 bold"), width=1)
candy_counter.insert(0, "285")
candy_counter['state'] = tk.DISABLED
candy_counter.grid(column=0, row=1, columnspan=2, stick='wens', padx=4, pady=4)

player = tk.Label(root, text="Возьми конфеты", bg="#832EF2", fg='#8AED63', font=("Arial 12 bold"))
player.grid(column=2, row=0, columnspan=3, stick='wens', padx=5)
player_field = tk.Entry(root, justify=tk.RIGHT, bg="#22D8D5", font=("Arial 14 bold"), width=1)
player_field.insert(0, 'от 1 до 28')
player_field['state'] = tk.DISABLED
player_field.grid(column=2, row=1, columnspan=3, stick='wens', padx=4, pady=4)

make_digit_buttom('1').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_buttom('2').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_buttom('3').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_buttom('4').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_digit_buttom('5').grid(row=2, column=4, stick='wens', padx=5, pady=5)
make_digit_buttom('6').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_buttom('7').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_buttom('8').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_buttom('9').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_digit_buttom('0').grid(row=3, column=4, stick='wens', padx=5, pady=5)
tk.Button(text='Взять', bd=5, bg="#F53D0A", font=("Arial Bold", 12), command=add_operation)\
    .grid(row=4, column=0, columnspan=3, stick='wens', padx=5, pady=5)
tk.Button(text='Удалить', bd=5, bg="#F5E90A", font=("Arial Bold", 12), command=add_clear)\
    .grid(row=4, column=3, columnspan=2, stick='wens', padx=5, pady=5)

root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)
root.grid_columnconfigure(4, minsize=60)

root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)
root.grid_rowconfigure(4, minsize=60)

mesg.showinfo('Правила игры', f'На столе лежат конфеты, каждый игрок берёт от 1 до 28 конфет.'
                              f'\nКто делает последний ход - побеждает.\n\n'
                              f'Победитель забирает все конфеты !')

root.mainloop()
