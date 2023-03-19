import csv


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
        view_wallets()

    def delete_wallet(self, index):
        del self.wallets[index]
        self.save_wallets()
        view_wallets()

    def save_wallets(self):
        with open("wallets.csv", mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "address"])
            for wallet in self.wallets:
                writer.writerow([wallet["name"], wallet["address"]])

    def get_wallets_list(self):
        return self.wallets


