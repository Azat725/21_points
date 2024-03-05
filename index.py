import random

def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 11, 1]
    return random.choice(cards)

def calculate_score(cards):
    score = sum(cards)
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def game():
    player_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"Твои карты сущка: {player_cards}, Че бля, считать не умеешь?: {player_score}")
    
        if player_score == 21:
            print("Красава, у тебя 21 ты выйграл ровным счетом нихуя")
            break
        elif player_score > 21:
            print("Нахуй ты столько взял? Ебло тупое")
            break

        choice = input("Подкинуть ещё одну? (да/нет) -> ")
        if choice == 'да':
            player_cards.append(deal_card())
        else:
            while computer_score < 17:
                computer_cards.append(deal_card())
                computer_score = calculate_score(computer_cards)
            
            print(f"Карты ведра с болтами: {computer_cards}, Он считать умеет, в отличии от тебя: {computer_score}")

            if computer_score == 21:
                print("У этого железного пидораса 21 очко. Ты проебал хату.")
            elif computer_score > 21:
                print("У железного перебор. Ебать ты фартовый!")
            elif player_score > computer_score:
                print("Нахуй ты с железякой играешь?")
            else:
                print("Тебя нагнула ебучая железяка. Иди выпей яду и убейся об стену")
                
            game_over = True

game()