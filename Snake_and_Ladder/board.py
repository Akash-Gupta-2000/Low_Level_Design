class GameBoard:
    def __init__(self, size):
        self.size = size
        self.board = [0] * (size * size + 1)
        self.players = []
        self.snakes_and_ladders = {}

    def add_player(self, player):
        self.players.append(player)

    def add_snake_or_ladder(self, start, end):
        self.snakes_and_ladders[start] = end

    def is_winner(self, player):
        return player.position == self.size * self.size

    def move_player(self, player, steps):
        current_position = player.position
        new_position = current_position + steps

        if new_position in self.snakes_and_ladders:
            new_position = self.snakes_and_ladders[new_position]

        if new_position <= self.size * self.size:
            player.position = new_position
