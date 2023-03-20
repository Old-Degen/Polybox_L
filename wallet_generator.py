import tkinter as tk
import csv
from web3 import Web3, Account


def generate_wallets(num_wallets_entry, group_name="", wallet_name=""):
    try:
        # Если не указано имя группы, создаем группу со стандартным именем
        if not group_name:
            group_name = "wallet_group"

        # Если не указано имя кошельков, используем имя группы по умолчанию
        if not wallet_name:
            wallet_name = group_name

        # Создаем Entry виджет для ввода количества кошельков
        num_wallets_entry = tk.Entry(root, width=30)
        num_wallets_entry.pack()

        # Генерируем указанное количество кошельков
        wallets = []
        for i in range(num_wallets_entry):
            account = Account.create()
            name = f"{wallet_name}_{i+1}"
            public_address = account.address
            private_key = account.key.hex()

            # Добавляем кошелек в список кошельков
            wallets.append({"name": name, "address": public_address, "private_key": private_key})

        # Создаем экземпляр класса WalletManager и добавляем кошельки
        manager = WalletManager()
        for wallet in wallets:
            manager.add_wallet(wallet["name"], wallet["address"])

    except Exception as e:
        print(f"Error generating wallets: {e}")


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
