def store(wishList):

    with open("wishlist.txt", "w") as wish_file:

        for key,value in wishList.items():
            wish_file.write(f"{key},{value[0]},{value[1]}\n")


def read():
    with open("wishlist.txt", "r") as wish_file:
        for line in wish_file:
            wish = line.strip().split(",")
            print (wish)

# example_wishlist = {
#    1 : ["book", 5.43],
#    2 : ["glasses", 105.43],
#    3 : ["Box", 40],
#    4 : ["Alcohol", 11.15]
#}

read()

