import copy

PLAYER1 = 1
PLAYER2 = 2


def caliculate_score(deck):
    score = 0
    for i, card in enumerate(deck[::-1]):
        score += int(card)*(i + 1)

    return score


def game(deck1, deck2, game_count):
    round = 1
    history1 = []
    history2 = []

    print("=== Game {} ===".format(game_count))
    print("")
    while len(deck1) > 0 and len(deck2) > 0:
        print('-- Round {} (Game {}) --'.format(round, game_count))
        print("Player 1's deck: {}".format(', '.join(deck1)))
        print("Player 2's deck: {}".format(', '.join(deck2)))

        for old_deck in history1:
            if deck1 == old_deck:
                print("same order deck: Player 1 wins")
                return deck1, []
        for old_deck in history2:
            if deck2 == old_deck:
                print("same order deck: Player 1 wins")
                return deck1, []
        history1.append(copy.copy(deck1))
        history2.append(copy.copy(deck2))

        play1 = deck1.pop(0)
        play2 = deck2.pop(0)
        print("Player 1 plays: {}".format(play1))
        print("Player 2 plays: {}".format(play2))
        if int(play1) <= len(deck1) and int(play2) <= len(deck2):
            # Enter sub-game
            print("Playing a sub-game to determine the winner...")
            print("")
            sub_deck1 = copy.copy(deck1[:int(play1)])
            sub_deck2 = copy.copy(deck2[:int(play2)])
            sub_deck1, sub_deck2 = game(sub_deck1, sub_deck2, game_count + 1)
            print("...anyway, back to game {}.".format(game_count))

            if len(sub_deck2) == 0:
                print("Player 1 wins round {} of game {}!".format(
                    round, game_count))
                print("")
                deck1.append(play1)
                deck1.append(play2)
            else:
                print("Player 2 wins round {} of game {}!".format(
                    round, game_count))
                print("")
                deck2.append(play2)
                deck2.append(play1)

        else:
            if int(play1) > int(play2):
                print("Player 1 wins round {} of game {}!".format(
                    round, game_count))
                print("")
                deck1.append(play1)
                deck1.append(play2)
            else:
                print("Player 2 wins round {} of game {}!".format(
                    round, game_count))
                print("")
                deck2.append(play2)
                deck2.append(play1)

        round += 1

    winner = PLAYER1
    if len(deck1) == 0:
        winner = PLAYER2
    print("The winner of game {} is player {}".format(game_count, winner))

    return deck1, deck2


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        block1, block2 = f.read().split("\n\n")
        deck1 = block1.splitlines()[1:]
        deck2 = block2.splitlines()[1:]

    deck1, deck2 = game(deck1, deck2, 1)
    print("== Post-game results ==")
    print("Player 1's deck: {}".format(', '.join(deck1)))
    print("Player 2's deck: {}".format(', '.join(deck2)))
    if len(deck1) > 0:
        print(caliculate_score(deck1))
    else:
        print(caliculate_score(deck2))
