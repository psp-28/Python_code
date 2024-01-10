# Auction bidding code : The code will ask for name and the bid ammount as an user input,
# then the user input is stored in an empty dictonary.
# when we ask for name and the bid input from user after getting inputs clear the screen.
# If 'no' bid is there then display the hoghest bid.

from replit import clear
# HINT : You can call clear() to clear the screen at output in the console.abs

import art
print(art.logo)


def find_highest_bidder(bidding_record):
    highest_bid = 0         # to check the highest bid amount
    winner = ""
    # Example : bidding_record = {"Angela" : 123, "James" : 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The Winner is {winner} with the bid of ₹{highest_bid}")


bids = {}           #Create an empty dictonary
bidding_finished = False    # In while loop if we want to end the loop to finish the bidding.
while not bidding_finished:
    name = input("Enter your name? : ")
    price = int(input("Enter the bid ammount: ₹"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n ")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)           

    elif should_continue == "yes":
        clear()
