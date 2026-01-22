import time
print("\nWelcome to the bank management system")
time.sleep(2)
print("\nSign in")
balance = 300000
deposit_limit = 200000
withdraw_limit = 150000
max_attempts = 3
create_username = input("\nCreate your username: ")
create_pin = input("\nCreate your pin: ")
print("\nAccount created successfully, you can now log in")
while True:
    username=input("Enter your username: ")
    if username == create_username:
        print("Processing...")
        time.sleep(2)
        print("\nUsername confirmed")
        break
    else:
        print("Invalid username. Please try again")
        continue
while True:
    h=False
    for attempt in range(1,4):
        pin = (input(f"\nAttempt{attempt}/3-\nEnter your PIN: "))
        if pin == create_pin:
            time.sleep(2)
            print("\nLogin successful")
            h=True
            break
        else:
            time.sleep(2)
            print("Invalid PIN. Please try again")
            continue
    while True:
        choice=input("\nWhat would you like to do?Transfer, Airtime, Withdraw, Balance, Deposit")
        if choice == "Transfer":
            transfer=int(input("\nSelect or type the amount you like to transfer:"))
            time.sleep(2)
            customer=input("\nType the name of the recipient:")
            time.sleep(2)
            account=input("\nType the account number of the recipient:")
            if transfer <= balance:
               print(f"\nAmount transferred. Your balance is {balance-transfer}")
               break
            else:
               print("\nInsufficient funds. Please enter a valid amount")
               continue
        elif choice == "Airtime":
            time.sleep(2)
            airtime=int(input("\nSelect or type the amount you like to recharge:"))
            time.sleep(2)
            customer=input("\nType the name of the recipient:")
            time.sleep(2)
            phone_number=input("\nType the phone number of the recipient:")
            if airtime <= balance:
                time.sleep(2)
                print(f"\nRecharge successful. Your balance is {balance-airtime}")
                break
            else:
                time.sleep(2)
                print("\nInsufficient funds. Please enter a valid amount")
                continue
        elif choice == "Withdraw":
            time.sleep(2)
            withdraw=(input("\nSelect or type the amount you like to withdraw:"))
            if withdraw.isdigit:
                withdraw=int(withdraw)
                if withdraw <= balance:
                    balance-=withdraw
                time.sleep(2)
                print(f"\nWithdrawal successful. Your balance is {balance}")
                break
            else:
                time.sleep(2)
                print("\nLimit exceeded. Please enter a valid amount")
                continue
        elif choice == "Balance":
            time.sleep(2)
            choice=input("\nHow would you like your balance to be shown?(onscreen/receipt)")
            if choice == "onscreen":
                time.sleep(2)
                print(f"Your balance is {balance}")
                break
            elif balance == "receipt":
                time.sleep(2)
                print("\nPlease take your receipt")
        elif choice == "Deposit":
            time.sleep(2)
            deposit=(input("\nSelect or type the amount you like to deposit:"))
            if deposit.isdigit():
                deposit=int(deposit)
                if deposit <= balance:
                    balance+=deposit
                print(f"\nDeposit successful. Your balance is {balance} ")
                break
            else:
                print("\nLimit exceeded. Please enter a valid amount")
                continue
    while True:
        choice=input("\nWould you like to perform another transaction?(y/n)")
        if choice == "y":
            time.sleep(2)
            print("\nPlease wait while your transaction is processing")
            break
        elif choice == "n":
            time.sleep(2)
            print("\nPlease take your card. Thank you for banking with us")









