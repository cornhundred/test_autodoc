print('here')

from new_module import Customer

print('initialize new customer')
cust = Customer('nick', 100)

print('initial balance')
print(cust.balance)

cust.deposit(50)

print('balance after deposit')
print(cust.balance)
