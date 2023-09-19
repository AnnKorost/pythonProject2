class Cat:
    def __init__(self, color, breed):
        self.paws_count = 4
        self.color = color
        self.breed = breed

    def show_paws_count(self):
        return Cat.paws_count

siam = Cat()

print(siam.show_paws_count())
