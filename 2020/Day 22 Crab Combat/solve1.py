def caliculate_score(deck):
    score = 0
    for i, card in enumerate(deck[::-1]):
        score += int(card)*(i + 1)

    return score


def game(deck1, deck2):
    round = 1
    while len(deck1) > 0 and len(deck2) > 0:
        print('-- Round {} --'.format(round))
        print("Player 1's deck: {}".format(', '.join(deck1)))
        print("Player 2's deck: {}".format(', '.join(deck2)))
        play1 = deck1.pop(0)
        play2 = deck2.pop(0)
        print("Player 1 plays: {}".format(play1))
        print("Player 2 plays: {}".format(play2))
        if int(play1) > int(play2):
            print("Player 1 wins the round!")
            deck1.append(play1)
            deck1.append(play2)
        else:
            print("Player 2 wins the round!")
            deck2.append(play2)
            deck2.append(play1)
        print("")
        round += 1

    print("")
    print("== Post-game results ==")
    print("Player 1's deck: {}".format(', '.join(deck1)))
    print("Player 2's deck: {}".format(', '.join(deck2)))

    return deck1, deck2


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        block1, block2 = f.read().split("\n\n")
        deck1 = block1.splitlines()[1:]
        deck2 = block2.splitlines()[1:]

    deck1, deck2 = game(deck1, deck2)
    if len(deck1) > 0:
        print(caliculate_score(deck1))
    else:
        print(caliculate_score(deck2))
