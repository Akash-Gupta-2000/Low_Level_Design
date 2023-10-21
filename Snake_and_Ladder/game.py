import board
import player
import dice
import random

def play_game(game_board, game_dice):
    while len(game_board.players) > 1:
        for player in game_board.players:
            input(f"{player.name}, press Enter to roll the dice...")
            dice_roll = game_dice.roll()
            game_board.move_player(player, dice_roll)
            print(f"{player.name} is now at position {player.position}")

            if game_board.is_winner(player):
                print(f"{player.name} wins!")
                game_board.players.remove(player)

def main():
    size = int(input("Enter the board size (n x n): "))
    game_board = board.GameBoard(size)
    game_dice = dice.Dice()

    for i in range(size):
        snake_head = random.randint(2, size * size)
        snake_tail = random.randint(1, snake_head - 1)
        game_board.add_snake_or_ladder(snake_head, snake_tail)

        ladder_start = random.randint(1, size * size - 1)
        ladder_end = random.randint(ladder_start + 1, size * size)
        game_board.add_snake_or_ladder(ladder_start, ladder_end)

    num_players = int(input("Enter the number of players: "))
    for i in range(num_players):
        player_name = input(f"Enter Player {i + 1}'s name: ")
        new_player = player.Player(player_name)
        game_board.add_player(new_player)

    play_game(game_board, game_dice)

if __name__ == "__main__":
    main()
