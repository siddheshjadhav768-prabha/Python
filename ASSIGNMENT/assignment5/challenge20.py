class Player:
    def __init__(self, name, team):
        self.name = name
        self.team = team

    def show(self):
        print(self.name)
        print(self.team)

p1 = Player("Virat", "India")

p1.show()