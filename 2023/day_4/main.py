from typing import List, Dict
from Card import Card

def recursive_reduce(card: Card, deck: List[Card], memo: Dict[int, int]):
    if card is None: return 0
    if card.id in memo: return memo.get(card.id)
    result = 1 + sum([recursive_reduce(next_card, deck, memo) for next_card in deck[card.id:card.id + card.compute_value()]])
    memo[card.id] = result
    return result 

if __name__ == '__main__':
    f = open('test_input.txt')
    simple_total_value = 0
    # original_deck: Dict[int, Card] = {}
    card_deck = []
    
    for line in f.readlines():
        card = Card(line)
        simple_total_value += card.compute_value()
        # original_deck.update({ card.id: card })
        card_deck.append(card)
    print(f'Total value for part 1: {simple_total_value}')

    # card_queue: List[Card] = list(original_deck.values())
    card_counter: int = 0
    memo: Dict[int, int] = {}
    cards_count: int = 0
    for card in card_deck:
        cards_count += recursive_reduce(
            card,
            deck=card_deck,
            memo=memo
        )
    # while len(card_queue) > 0:
    #     card = card_queue.pop(0)
    #     card_counter += 1
    #     value = card.compute_value()
    #     i = card.id + 1
    #     while i - card.id <= value and  i < len(original_deck):
    #         card_queue.append(original_deck.get(i))
    #         i += 1
    # print(f'Cards count for part 2: {card_counter}')
    print(f'Cards count for part 2: {cards_count}')

