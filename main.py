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
num_wallets = Entry(tab1)
num_wallets.pack()


def create_wallets():
    # Создаем диалоговое окно для ввода параметров создания кошельков
    create_wallets_window = tk.Toplevel(root)
    create_wallets_window.title("Create Wallets")

    # Создаем элементы управления для ввода параметров создания кошельков
    num_wallets_label = tk.Label(create_wallets_window, text="Number of wallets:")
    num_wallets_entry = tk.Entry(create_wallets_window, width=30)
    group_name_label = tk.Label(create_wallets_window, text="Group name (optional):")
    group_name_entry = tk.Entry(create_wallets_window, width=30)
    wallet_name_label = tk.Label(create_wallets_window, text="Wallet name (optional):")
    wallet_name_entry = tk.Entry(create_wallets_window, width=30)

    # Создаем кнопку для создания кошельков
    create_wallets_button = tk.Button(create_wallets_window, text="Create Wallets", command=lambda: generate_wallets(
        num_wallets_entry.get(),
        group_name_entry.get(),
        wallet_name_entry.get()
    ))

    # Размещаем элементы управления в окне
    num_wallets_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    num_wallets_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    group_name_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    group_name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
    wallet_name_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    wallet_name_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
    create_wallets_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)



def generate_wallets(num_wallets, group_name="", wallet_name=""):
    try:
        # Если не указано имя группы, создаем группу со стандартным именем
        if not group_name:
            group_name = "wallet_group"

        # Если не указано имя кошельков, используем имя группы по умолчанию
        if not wallet_name:
            wallet_name = "wallet"

        # Генерируем указанное количество кошельков
        for i in range(num_wallets):
            account = Account.create()
            name = f"{wallet_name}_{i+1}"
            public_address = account.address
            private_key = account.key.hex()

            # Добавляем кошелек в список кошельков
            wallets.append({"name": name, "address": public_address, "private_key": private_key})

        # Создаем экземпляр класса WalletManager и добавляем кошельки
        for wallet in wallets:
            manager.add_wallet(wallet["name"], wallet["address"])

    except Exception as e:
        print(f"Error generating wallets: {e}")



# Создаем вкладку для просмотра кошельков
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="View Wallets")


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
