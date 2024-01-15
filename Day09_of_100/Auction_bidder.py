import os

bid_Status = False
def bidder_pro(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of $ {highest_bid}\n\n\n\n\n\n\n")


while not bid_Status:
    name = input("Whats your Name : ")
    price = int(input("What is your Bid $ : "))
    bids ={}
    bids[name] = price
    life = input("are there any other bidder's y or n")
    if life == "n":
        bid_Status = True
        os.system("cls")
        bidder_pro(bids)
    elif life =="y":
        os.system("cls")

