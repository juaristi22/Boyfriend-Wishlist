from storeFile import store, read

# add to wish list

def add(item, price, wishlist = None):
    if None:
        wishlist = {}

    n = len(wishlist.items())
    wishlist[n+1] = [item, price]
    store(wishlist)

prev_wishlist = read()
add('ice cream', 5.5, prev_wishlist)


