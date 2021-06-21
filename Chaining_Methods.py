class User:
    def __init__(self,name,email):
        self.name = name
        self.account_balance = 0
        self.email = email

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance ${self.account_balance}")
        return self

    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(f"{self.name} transferred ${amount} to {other_user.name}")
        return self

larry = User("larry", "larry@3stooges.com")
curly = User("curly", " curly@3stooges.com")
moe = User("moe", "moe@3stooges.com")

larry.make_deposit(500).make_deposit(300).make_deposit(100).make_withdrawl(200).transfer_money(moe,50).display_user_balance()

curly.make_deposit(500).make_deposit(1000).make_deposit(100).make_withdrawl(200).display_user_balance()

moe.make_deposit(5000).make_withdrawl(1000).make_deposit(100).make_withdrawl(200).display_user_balance()


