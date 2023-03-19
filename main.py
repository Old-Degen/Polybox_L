from tkinter import *
from tkinter import ttk
from wallet_generator import generate_wallets
from wallet_manager import WalletManager

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
    num_wallets = int(num_wallets_entry.get())
    group_name = group_name_entry.get()
    wallet_name = wallet_name_entry.get()

    try:
        # Генерируем кошельки
        generate_wallets(num_wallets, group_name, wallet_name)
    except Exception as e:
        error_label.config(text=f"Error generating wallets: {e}")
        return

    # Обновляем список кошельков
    try:
        manager = WalletManager()
    except Exception as e:
        error_label.config(text=f"Error loading wallets: {e}")
        return

    wallets = manager.get_wallets_list()
    wallets_listbox.delete(0, END)
    for wallet in wallets:
        wallets_listbox.insert(END, f"{wallet['name']} - {wallet['address']}")

    # Очищаем поля ввода
    num_wallets_entry.delete(0, END)
    group_name_entry.delete(0, END)
    wallet_name_entry.delete(0, END)


def generate_wallets_and_view(num_wallets):
    try:
        # Генерируем кошельки
        num_wallets = int(num_wallets)
        generate_wallets(num_wallets)

        # Обновляем список кошельков
        view_wallets()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of wallets")
    except Exception as e:
        messagebox.showerror("Error", f"Error generating wallets: {e}")


    # Создаем экземпляр класса WalletManager
    manager = WalletManager()

    # Загружаем кошельки из файла и добавляем их в менеджер кошельков
    with open("wallets.csv") as f:
        wallets_csv = csv.reader(f)
        next(wallets_csv)  # skip header
        for row in wallets_csv:
            manager.add_wallet(row[0], row[1], row[2], row[3])

    # Удаляем кнопку "View Wallets"
    view_button.pack_forget()


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




# Создаем кнопки для создания и просмотра кошельков
generate_button = Button(tab1, text="Generate Wallets", command=create_wallet)
generate_button.pack()

view_button = Button(tab1, text="View Wallets", command=view_wallets)
view_button.pack()


notebook.pack()

root.mainloop()
