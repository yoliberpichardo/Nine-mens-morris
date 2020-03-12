class Player:
    def __init__(self, name):
        self.name = name
        self.token = 9

    def test(self):
        self.token -= 1
        print(self.name)
        print(self.token)


david = Player("david")
daniel = Player("daniel")
yolibel = Player("yoli")

david.test()
david.test()
david.test()
david.test()
david.test()
david.test()
print(daniel.token)
print(daniel.name)
print(david.name)
yolibel.test()