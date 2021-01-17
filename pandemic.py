d = {}
add = True

def add_card(card):
    if card in d:
        d[card] += 1
    else:
        d[card] = 1

def remove_card(card):
    if card in d:
        d[card] -= 1
        if d[card] == 0:
            d.pop(card)
    
while True:
    card = input(f"input the card [add is {add}]: ")
    if card == "show":
        for city, count in d.items():
            print("city: {}, count: {}".format(city, count))
    elif card == "epidemic":
        card = input("input the card: ")
        add_card(card)
        add = False
    elif add:
        add_card(card)
    else:
        remove_card(card)