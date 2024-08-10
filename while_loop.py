account_balance = 50_000

while (account_balance > 0):
    if (account_balance > 20_000):
        continue
    account_balance = account_balance - 5_000
    print("Balance: ", account_balance)