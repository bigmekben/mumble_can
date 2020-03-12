import random
from time import sleep

def hesitate():
    for i in range(1,4):
        sleep(0.5)
        s = "."
        for j in range(1, i):
            s += "."
        print(s)


def pause():
    sleep(0.8)

def reach_in_can():
    print("\nYou reach into the can...\n")
    hesitate()
    
def drop_into_can(what):
    print(f"\nYou drop {what} into the can...\n")
    hesitate()

def can_contents():
    could_have = ['coins', 'donuts']
    index = random.randint(0, 1)
    return could_have[index]
    
def can_coins():
    return random.randint(1, 10)
    
def take(inventory):
    took = can_contents()
    reach_in_can()
    if (took == 'coins'):
        coins = can_coins()
        inventory['coins'] += coins
        print(f"[...and took {coins} coins.]")
        pause()
        print("\n\t'What's wrong with you?  That money is for the children!'\n")
        pause()
        inventory['score'] -= (20 * coins)
    else:
        print("[...and scored a donut! Yum...]")
        inventory['donuts'] += 1
        inventory['score'] += 100
        pause() 
  
def give_coins(inventory):
    if inventory['coins'] < 1:
        print("You don't have any money to give.")
        pause()
        return
    quit = False
    give = inventory['coins'] + 1
    while quit != True and give > inventory['coins']:
        print(f"Give how many coins? (1 to {inventory['coins']}, or q to give none):")
        response = input(">")
        if (response == 'q' or int(response) == 0):
            print("\n\t'Cheapskate!!!  It's for the kids!!!'\n")
            pause()
            inventory['score'] -= 100
            return
        give = int(response)
    inventory['coins'] -= give
    drop_into_can(f"{give} coins")
    if can_contents() == 'coins':
        print(f"[You gave {give} coins.]")
        pause() 
        print("\n\t'The children thank you, man!'\n")
        pause() 
        inventory['score'] += (50 * give)
    else:
        print("\n\t'What's wrong with you??? You're ruining the donuts with those filthy coins!!!'\n")
        pause()
        inventory['score'] -= (10 * give)
    
def give_donut(inventory):
    if inventory['donuts'] < 1:
        print("You don't have any donuts to give.")
        return
    inventory['donuts'] -= 1
    drop_into_can('a donut')
    print("You gave a donut...")
    if can_contents() == 'donuts':
        print("\n\t'Thanks for the donut, bro!'\n")
        inventory['score'] += 75
        pause()
    else:
        print("\n\t'What the heck??? A linty donut??? The children need MONEY, man!'\n")
        inventory['score'] -= 50
    
def give(inventory):
    quit = False
    while quit != True:
        print("Give what?")
        print("Your choices are:\n\t1 - coins\n\t2 - donut\n\tq - quit")
        choice = input(">")
        if choice == '1':
            give_coins(inventory)
            quit = True
        elif choice == '2':
            give_donut(inventory)
            quit = True
        elif choice == 'q':
            quit = True
        else:
            print("I don't understand...")

def mumble():
    prompts = [
        'Would you like mvvth a duhnmfbt?', 
        'Would you mwwt mm blmvpt?',
        'Wmbl dlmfl merghfl wuhmfut?']
    index = random.randint(0,2)
    return prompts[index]
    
def play():    

    print("\n\n")
    print("=======================")
    print("| M U M B L E - C A N |")
    print("=======================\n")
    
    inventory = {
        'coins': 10,
        'donuts': 0,
        'score': 0
        }

    quit = False
    while quit != True:
        print(f"You have {inventory['coins']} coins and {inventory['donuts']} donuts.\n")
        print("A man approaches you and holds out a can towards you. He says:\n")
        print(f"\t'{mumble()}'\n")
        print("Your choices are:\n\t1 - take\n\t2 - give\n\tq - quit")
        choice = input(">")
        if choice == '1':
            take(inventory)
        elif choice == '2':
            give(inventory)
        elif choice == 'q':
            quit = True
        else:
            print("I don't understand...")
            
    print("========================")
    print("| F I N A L  S C O R E |")
    print("========================")
    print(f"You ended the game with {inventory['coins']} coins and {inventory['donuts']} donuts.")
    print(f"Your final SCORE: {inventory['score']}")

# Start the game    
play()
