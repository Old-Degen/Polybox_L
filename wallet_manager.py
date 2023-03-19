from web3 import Web3, Account

class Wallet:
    def __init__(self, address, private_key):
        self.address = address
        self.private_key = private_key
        self.balance = 0

    @staticmethod
    def create_wallet():
        account = Account.create()
        return Wallet(account.address, account.key.hex())

    def get_balance(self):
        balance = w3.eth.get_balance(self.address)
        self.balance = w3.fromWei(balance, 'ether')
        return self.balance

    def send_tokens(self, recipient_address, amount):
        txn = {
            'to': recipient_address,
            'value': w3.toWei(amount, 'ether'),
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei'),
            'nonce': w3.eth.getTransactionCount(self.address)
        }
        signed_txn = w3.eth.account.sign_transaction(txn, self.private_key)
        txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return txn_hash.hex()

    def delete_wallet(self):
        # удаление кошелька
        pass

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

    def distribute_tokens(self, amount):
        num_wallets = len(self.wallets)
        if num_wallets == 0:
            print("No wallets available")
            return
        share = amount // num_wallets
        remainder = amount % num_wallets
        for i, wallet in enumerate(self.wallets):
            if i == 0:
                # Add the remainder to the first wallet
                balance = share + remainder
            else:
                balance = share
            # Perform the transfer
            print(f"Transferring {balance} tokens to {wallet['address']}")
            # TODO: implement the transfer logic

        # Save the updated wallets
        self.save_wallets()
