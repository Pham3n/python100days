# Blind Auction          First-price Sealed-bid Auction (FPSBA)

# {
#     "name" : "Angela",
#     "price" : 123
# }

bids = []
highestbid = [0]


def bidder(bids, highestbid):
    name = input("What is your name?\n")
    price = int(input("What is your bid price?\n"))

    bids += [{
        name: price
    }]
    if price > highestbid[0]:
        highestbid = [price, name]
    summore = input("Continue bidding? yes or no:")
    if summore == 'yes':
        bidder(bids, highestbid)
    else:
        print(f'The winner is {highestbid[1]} with a bid of R{highestbid[0]}')


bidder(bids, highestbid)
print(bids)
