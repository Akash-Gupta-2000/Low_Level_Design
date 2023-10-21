import board
import player
import dice

def play_game(game_board, game_dice):
    while len(game_board.players) > 1:
        for player in game_board.players:
            input(f"{player.name}, press Enter to roll the dice...")
            dice_roll = game_dice.roll()
            print(f"{player.name} rolled a {dice_roll}")
            game_board.move_player(player, dice_roll)
            print(f"{player.name} is now at position {player.position}")

            if game_board.is_winner(player):
                print(f"{player.name} wins!")
                game_board.players.remove(player)
