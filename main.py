import tkinter as tk
import csv
from web3 import Web3, Account

class WalletManager:
    def __init__(self):
        self.wallets = []
        with open("wallets.csv") as f:
            wallets_csv = csv.reader(f)
            next(wallets_csv)  # skip header
            for row in wallets_csv:
                self.wallets.append(row)

    def add_wallet(self, name, address):
        self.wallets.append({"name": name, "address": address})
        self.save_wallets()

    def delete_wallet(self, index):
        del self.wallets[index]
        self.save_wallets()

    def save_wallets(self):
        with open("wallets.csv", mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "address"])
            for wallet in self.wallets:
                writer.writerow([wallet["name"], wallet["address"]])

class CreateWalletsWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("Create Wallets")

        self.group_name_label = tk.Label(self.window, text="Group Name:")
        self.group_name_label.pack()
        self.group_name_entry = tk.Entry(self.window)
        self.group_name_entry.pack()

        self.wallet_name_label = tk.Label(self.window, text="Wallet Name:")
        self.wallet_name_label.pack()
        self.wallet_name_entry = tk.Entry(self.window)
        self.wallet_name_entry.pack()

        self.num_wallets_label = tk.Label(self.window, text="Number of Wallets:")
        self.num_wallets_label.pack()
        self.num_wallets_entry = tk.Entry(self.window)
        self.num_wallets_entry.pack()

        self.create_wallets_button = tk.Button(self.window, text="Create Wallets", command=self.create_wallets)
        self.create_wallets_button.pack()

    def create_wallets(self):
        try:
            num_wallets = int(self.num_wallets_entry.get())
            manager = WalletManager()
            for i in range(num_wallets):
                account = Account.create()
                wallet_name = self.wallet_name_entry.get() + "_" + str(i+1)
                manager.add_wallet(wallet_name, account.address)
            self.window.destroy()
        except Exception as e:
            print(f"Error generating wallets: {e}")

class ViewWalletsWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("View Wallets")

        self.wallet_listbox = tk.Listbox(self.window)
        self.wallet_listbox.pack()

        self.view_wallets()

    def view_wallets(self):
        manager = WalletManager()
        if not manager.wallets:
            tk.messagebox.showinfo("Error", "No wallets found")
            return
        self.wallet_listbox.delete(0, tk.END)
        for wallet in manager.wallets:
            self.wallet_listbox.insert(tk.END, f"{wallet[0]} - {wallet[1]}")

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Ethereum Wallet Generator")

        self.notebook = tk.ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.create_wallets_tab = tk.ttk.Frame(self.notebook)
        self.notebook.add(self.create_wallets_tab, text="Create Wallets")

        self.group
