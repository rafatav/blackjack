import random
import os
from art import logo
def deal_card():
    """"Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "Você ultrapassou. Você perdeu"

    if user_score == computer_score:
        return "Empate"
    elif computer_score == 0:
        return "Você perdeu, oponente tem Blackjack"
    elif user_score == 0:
        return "Você venceu com um Blackjack"
    elif user_score > 21:
        return "Você ultrapassou. Você perdeu"
    elif computer_score > 21:
        return "Oponente ultrapassou. Você venceu"
    elif user_score > computer_score:
        return "Você venceu"
    else:
        return "Você perdeu"
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"    Suas cartas: {user_cards}, pontuação atual: {user_score}")
        print(f"    Primeira carta do computador: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Digite 's' para pegar outra carta, digite 'n' para passar: ")
            if user_should_deal == "s":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Sua mão final: {user_cards}, pontuação final: {user_score}")
    print(f"    Mão final do computador: {computer_cards}, pontuação final: {computer_score}")
    print(compare(user_score, computer_score))
while input("Você quer jogar uma partida de Blackjack? Digite 's' ou 'n': ") == "s":
    os.system('cls')
    play_game()
