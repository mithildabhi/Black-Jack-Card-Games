import random

# i want to make a turn for computer and user randomly
turn = random.choice(['user', 'computer'])
print(turn)

# Card values (11 = Ace, 10 = King/Queen/Jack)
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # Ace is 1 or 11, face cards are 10
answer = ['y','n'] 

# Deal 2 cards each
user_cards = random.sample(cards, 2)
computer_cards = random.sample(cards, 2)

def has_blackjack(cards):
    return sum(cards) == 21 and len(cards) == 2

# Check for Blackjack
user_blackjack = has_blackjack(user_cards)
computer_blackjack = has_blackjack(computer_cards)

# Show cards
print(f"Your cards: {user_cards} (Total: {sum(user_cards)})")
# print(f"Computer's cards: {computer_cards} (Total: {sum(computer_cards)})") # TO HIDE FOR USER
print(f"Computer's first card: {computer_cards[0]}") 

# Outcome logic
if user_blackjack and computer_blackjack:
    print("Draw! Both have Blackjack!")
    exit()
elif user_blackjack:
    print("You win with a Blackjack!")
    exit()
elif computer_blackjack:
    print("Computer wins with a Blackjack!")
    exit()
else:
    print("No Blackjack. Game continues...")
    
# Ask user if they want to hit or skip

# score under than 21
def hit_or_skip_user():
    user_hit = input("Tell y to hit and n to skip:")
    if user_hit == 'y':
        if sum(user_cards) < 21:
            user_another = random.choice(cards)  
            user_cards.append(user_another)
            print(f"New user cards: {user_cards} (Total: {sum(user_cards)})")
            if sum(user_cards) > 21:
                print("User Busted! Computer Wins")
                exit()
               
    elif user_hit == 'n':
        print("Original Remain cards: ", user_cards)
        print("User chose to skip.")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        hit_or_skip_user()  
        
def hit_or_skip_computer():
    computer_hit = random.choice(answer)
    if computer_hit == 'y':
        if sum(computer_cards) < 21:
            computer_another = random.choice(cards)
            computer_cards.append(computer_another)
            # print(f"New computer cards: {computer_cards} (Total: {sum(computer_cards)})")
            print(f"Computer's first card: {computer_cards[0]}")
            if sum(computer_cards) > 21:
                print("Computer Busted! User Wins")
                exit()
            elif sum(computer_cards) < 21:
                hit_or_skip_user() 
    elif computer_hit == 'n':
        print("Original Remain cards: ",computer_cards[0])
        print("Computer chose to skip.")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        hit_or_skip_user()
        
# MAIN PROGRAM LOGIC         
if turn == 'user':
    hit_or_skip_user()
    hit_or_skip_computer()   # turn for both side to take place     
if turn == 'computer':
    hit_or_skip_computer()
    hit_or_skip_user()      # turn for both side to take place


# Final outcome
print(f"Final user cards: {user_cards} (Total: {sum(user_cards)})")
print(f"Final computer cards: {computer_cards} (Total: {sum(computer_cards)})")

# Determine winner
if sum(user_cards) == 21:
    print("User Wins")
elif sum(computer_cards) == 21:
    print("Computer Wins")
elif sum(user_cards) > 21:
    print("User Busted! Computer Wins")
elif sum(computer_cards) > 21:
    print("Computer Busted! User Wins")
elif sum(user_cards) > sum(computer_cards):
    print("User Wins")
else:
    print("Computer Wins")
    
print("Game Over")