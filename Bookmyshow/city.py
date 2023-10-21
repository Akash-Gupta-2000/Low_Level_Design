class City:
    def __init__(self, name):
        self.name = name
        self.cinemas = []

    def add_cinema(self, cinema):
        self.cinemas.append(cinema)
