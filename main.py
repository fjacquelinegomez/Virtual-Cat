import tabby
import ocelot
import check_input
import tiger
import player 


def interact_cat(cat, player):
    """Display the cat interaction menu and get the user's input"""
    print("Cat menu: ")
    print("1. Feed your cat \n2. Play with your cat \n3. Pet your cat")
    menu_choice = check_input.get_int_range("Enter choice: ", 1,3)

    if menu_choice == 1: #based on player's input the activity will display
        cat.feed(player)
    elif menu_choice == 2:
        cat.play(player)
    elif menu_choice == 3:
        cat.pet(player)


def main():
    cats = ["Tabby Cat", "Ocelot", "Tiger"]
    print("Cat Selection: ") # cat selection menu
    print("1. "+cats[0])
    print("2. "+cats[1])
    print("3. "+cats[2])
    user = check_input.get_int_range("Enter choice: ", 1,3)
    catName = str(input("Name your kitty: "))
    p1 = player.Player() #constructs player

    if user == 1:
        c1 = tabby.Tabby(catName)
    elif user == 2:
        c1 = ocelot.Ocelot(catName)
    elif user == 3:
        c1 = tiger.Tiger(catName)


    while p1.hp > 0:
        print(p1)
        print(c1)
        interact_cat(c1,p1)

        if p1.hp == 0:
            print()
            print("Your cat killed you...")

main()