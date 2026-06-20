class CricketPlayer:
    def __init__(self, name, runs, matches):
        self.name = name
        self.runs = runs
        self.matches = matches

p1 = CricketPlayer("Virat", 13000, 275)

print(p1.name)
print(p1.runs)
print(p1.matches)