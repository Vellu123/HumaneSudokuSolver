class Cell:
    def __init__(self):
        self.is_solved = False
        self.number = 0
        self.possible_numbers = [x for x in range(1, 10)]
        self.position = (0, 0)

    def __repr__(self):
        return str(self.number)
