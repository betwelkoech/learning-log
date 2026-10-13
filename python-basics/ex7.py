first= 77
second=95
third=43
print("WELCOME TO GUESSGAME")
deposit=int(input("Enter Amount in the Wallet"))
print("ENTER YOUR LUCKY NUMBVER BETWEEN 0 AND 100")
if deposit>20:
    guess=int(input("Lucky No:"))
    if guess==first or guess==second or guess==third:
       print("WON")
       deposit=deposit-20

    else:
     print("LOST")
else:
    print("Insufficient Balance, Deposit to play.")
    exit



