import tkinter as tk
from tkinter import *
from tkinter import ttk
from wallet_generator import generate_wallets
from wallet_manager import WalletManager
import sys
import os


sys.path.append(os.path.abspath("/path/to/directory"))


root = Tk()
root.title("ToolBox")

notebook = ttk.Notebook(root)

# Создаем вкладку для создания кошельков
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Create Wallets")

# Добавляем элементы на вкладку создания кошельков
group_label = Label(tab1, text="Group Name:")
group_label.pack()
group_name = Entry(tab1)
group_name.pack()

wallet_label = Label(tab1, text="Wallet Name:")
wallet_label.pack()
wallet_name = Entry(tab1)
wallet_name.pack()

num_label = Label(tab1, text="Number of Wallets:")
num_label.pack()
num_wallets_entry = Entry(tab1)
num_wallets_entry.pack()


def create_wallets():
    num_wallets = int(num_wallets_entry.get())
    manager = WalletManager()
    for i in range(num_wallets):
        wallet = manager.create_wallet()
        manager.add_wallet(wallet.address, wallet.private_key)
    manager.save_wallets()
    create_wallets_window.destroy()



def view_wallet():
    # Создаем экземпляр класса WalletManager
    manager = WalletManager()

    # Получаем список кошельков из экземпляра класса
    wallets = manager.get_wallets_list()

    # Создаем список для отображения кошельков
    wallet_listbox = Listbox(tab2)
    wallet_listbox.pack()

    # Очищаем список для обновления
    wallet_listbox.delete(0, END)

    # Добавляем каждый кошелек в список
    for wallet in wallets:
        wallet_listbox.insert(END, f"{wallet[0]} - {wallet[1]}: {wallet[2]}")

def view_wallets():
    manager = WalletManager()
    if not manager.wallets:
        messagebox.showinfo("Error", "No wallets found")
        return
    view_window = Toplevel(root)
    view_window.title("View Wallets")
    wallets_list = Listbox(view_window)
    for wallet in manager.wallets:
        wallets_list.insert(END, f"{wallet[0]} - {wallet[1]} - {wallet[2]} - {wallet[3]}")
    wallets_list.pack()
    view_window.mainloop()




# Создаем кнопки для создания и просмотра кошельков
generate_button = Button(tab1, text="Generate Wallets", command=create_wallets)
generate_button.pack()

view_button = Button(tab1, text="View Wallets", command=view_wallets)
view_button.pack(side=LEFT, padx=10)



notebook.pack()

root.mainloop()
