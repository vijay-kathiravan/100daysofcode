print("Welcome to the Secret Auction Program")
from replit import clear
auction = []
def add_new_auctioneer(name:str,bid:int):
    """
    This function allows us to add new auctioneer, and their bid
    :param name: This parameter takes the auctioneer's name as input
    :param bid: This parameter take the auctioneer's bid as input
    :return: This function returns's a updated list as output
    """
    aucti = {}
    aucti[name] = bid
    auction.append(aucti)
user = True
maxi = 0
winner = ''
while user:
    user_inp = input("If you are bidding,Enter Your name:\t")
    bidding_amount = int(input("Enter your bidding amount:\t$"))
    add_new_auctioneer(user_inp,bidding_amount)
    con = input("Are there more person's participating in the auction?\t")
    if con == 'Yes'.casefold():
        clear()
        continue
    else:
        user = False
        for i in range(len(auction)):
            for j in auction[i]:
                if auction[i][j]> maxi:
                    maxi = auction[i][j]
                    winner = j
        print(f"The winner of the auction is {winner} with a bidding amount of ${maxi}")