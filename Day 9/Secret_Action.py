secret_bidders=[]
def add_new_bidder(name, bid):
    new_bidder={}
    new_bidder["name"]= name
    new_bidder["bid"] = bid
    secret_bidders.append(new_bidder)

bidding= True
while bidding:
    bidder_name = input("Please Enter your Name : ")
    bidder_bid = int(input("Please Enter the bid : "))
    add_new_bidder(bidder_name, bidder_bid)
    new_bidding = input("Please Enter 'y' if there is a new bidder and 'n' for end the actuion : ")
    if new_bidding == "y":
        pass
    else:
        bidding = False
highst_bidder_name = ""
highst_bidder_bid=0
for bidder in secret_bidders: 
    if bidder["bid"] > highst_bidder_bid:
        highst_bidder_name = bidder["name"]
        highst_bidder_bid = bidder["bid"]
print(f"the highst bidder name is {highst_bidder_name} and the bid is {highst_bidder_bid}")
        