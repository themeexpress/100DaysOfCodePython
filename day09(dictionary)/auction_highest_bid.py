"""
Highest bid auction program.
This program allows users to place bids on an item and determines the highest bid at the end of
"""
print("Welcome to the secret auction program.")

bids = {}

while True:
    name = input("What is your name? ")
    bid = float(input("What is your bid? $"))
    bids[name] = bid
    more = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if more != "yes":
        break

highest_bidder = max(bids, key=bids.get)
highest_bid = bids[highest_bidder]

print("Bidding complete.")
print(f"The highest bid is ${highest_bid} by {highest_bidder}.")