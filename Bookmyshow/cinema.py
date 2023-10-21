class Cinema:
    def __init__(self, name):
        self.name = name
        self.halls = []

    def add_hall(self, hall):
        self.halls.append(hall)
