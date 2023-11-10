from abc import ABC, abstractmethod

class Bank:
    total_balance = 0
    loan_amount = 0

    def __init__(self, bank_name) -> None:
        self.bank_name = bank_name
        self.users = []
        self.admins = []
        self.__loan_feature = None

    @property
    def loan_feature(self):
        return self.__loan_feature
    
    @loan_feature.setter
    def loan_feature(self, feature):
        self.__loan_feature = feature

    def add_user(self, user):
        self.users.append(user)

    def add_admin(self, admin):
        self.admins.append(admin)

    def __repr__(self) -> str:
        return f'Bank Name: {self.bank_name}, Users: {len(self.users)}, Admins: {len(self.admins)}'


class Open_Account(ABC):
    def __init__(self, name, email, nid, phone_no, branch_name) -> None:
        self.name = name
        self.email = email
        self.nid = nid
        self.phone_no = phone_no
        self.branch_name = branch_name

    @abstractmethod
    def display_information(self):
        raise NotImplementedError
    
class User(Open_Account):
    def __init__(self, name, email, nid, phone_no, branch_name, password, acc_no, initial_balance) -> None:
        super().__init__(name, email, nid, phone_no, branch_name)
        self.password = password
        self.acount_no = acc_no
        self.balance = initial_balance
        Bank.total_balance += initial_balance
        self.transaction_history = []

    # 2 deposit amount
    def deposit(self, amount):
        self.balance += amount
        Bank.total_balance += amount
        self.transaction_history.append(f'Deposited Amount: {amount}')

    # 2 withdraw amount
    def withdraw(self, amount):
        if amount <= Bank.total_balance:
            if amount > self.balance:
                print(f'{self.name}, Sorry! You do not have sufficient balance. Your balance: {self.balance}')
            else:
                self.balance -= amount
                Bank.total_balance -= amount
                self.transaction_history.append(f'Withdrawal Amount: {amount}')
        else:
            print(f'Sorry! The bank is bankrupted...')

    # 3 check available balance
    def available_balance(self):
        return f'{self.name} available balance is: {self.balance}'

    # 4 transfer money to another user account
    def transfer(self, receiver, amount):
        if self.balance >= amount:
            self.balance -= amount
            receiver.balance += amount
            self.transaction_history.append(f'Transferred: {amount} to {receiver.name}')
        else:
            print(f'{self.name}, Sorry! You don not have sufficient balance.')

    # 5 check transaction history
    def transaction_history_check(self):
        return self.transaction_history
    
    # 6 take loan from the bank
    def take_loan(self, loan_amount):
        if Bank.loan_feature:
            if loan_amount <= 2 * self.balance:
                if loan_amount <= Bank.total_balance:
                    #loan_amount = 2 * self.balance
                    self.balance += loan_amount
                    Bank.loan_amount += loan_amount
                    Bank.total_balance -= loan_amount
                    self.transaction_history.append(f'Loan taken: {loan_amount}')
                else:
                    print('Bank has not sufficient balance to give you loan....')
            else:
                print(f'{self.name}, You cannot take loan more than {2 * self.balance}')
        else:
            print(f'You cannot take loan right now.....')

    def display_information(self):
        print(f'------------User Account No: {self.acount_no} Info.----------')
        print(f'Name: {self.name}, Branch: {self.branch_name}, Phone no.: {self.phone_no}')
        print('-------------------------------------------------')


class Admin(Open_Account):
    def __init__(self, name, email, nid, phone_no, branch_name, password, id_no) -> None:
        super().__init__(name, email, nid, phone_no, branch_name)
        self.password = password
        self.id_no = id_no
        
    # 2 check total available balance
    def bank_availabe_balance(self):
        return f'Bank has total balance: {Bank.total_balance}'
        
    
    # 3 check total loan amount
    def total_loan_amount(self):
        return f'Bank loan amount: {Bank.loan_amount}'
    
    # 4 loan feature on/off
    def set_loan_feature(self, loan_feature):
        Bank.loan_feature = loan_feature
    
    def display_information(self):
        print(f'Admin Name: {self.name}, ID: {self.id_no}')


new_bank = Bank('Notun Bank')

user1 = User('Sayed', 'sa@gmail.com', 38483, 1845, 'Mohakhali', '17df#@', 234, 5000)
user2 = User('Mohammad', 'md@gmail.com', 45486, 1860, 'Uttara', '9i0df#@', 456, 7000)
user3= User('Riad', 'rd@gmail.com', 30487, 1849, 'Gulshan', '8y33#@', 896, 3000)

admin1 = Admin('Rahul', 'ra@gmail.com', 89971, 1345, 'Uttara', '367$#@', 1246)
admin2 = Admin('Amin', 'am@gmail.com', 52109, 1387, 'Gulshan', '359&#@', 1209)

new_bank.add_user(user1)
new_bank.add_user(user2)
new_bank.add_user(user3)

new_bank.add_admin(admin1)
new_bank.add_admin(admin2)

print(new_bank)

# user1.display_information()
# user2.display_information()
# user3.display_information()

user1.deposit(1500)
user2.deposit(500)
user3.deposit(1000)

user1.withdraw(500)
user2.withdraw(1500)
user3.withdraw(3000)

print(user1.available_balance())
print(user2.available_balance())
print(user3.available_balance())

user1.transfer(user2, 5000)
user2.transfer(user3, 4000)

print(user1.available_balance())
print(user2.available_balance())
print(user3.available_balance())

print(admin1.bank_availabe_balance())
user1.take_loan(1000)
print(user1.available_balance())
print(admin1.bank_availabe_balance())

print(user1.transaction_history_check())
print(user2.transaction_history_check())
print(user3.transaction_history_check())

print(admin1.total_loan_amount())

# admin1.display_information()
# admin2.display_information()

admin1.set_loan_feature(False)
user2.take_loan(5000)

admin1.set_loan_feature(True)
user3.take_loan(3000)

print(user3.available_balance())
print(admin1.total_loan_amount())
print(admin1.bank_availabe_balance())

user3.take_loan(15000)



