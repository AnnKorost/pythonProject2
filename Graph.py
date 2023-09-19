class Graph:
    limit_y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        a, b = self.limit_y
        lst_num = range(a, b + 1)
        print(*filter(lambda num: num in lst_num, self.data))


graf_1 = Graph()
graf_1.set_data([i for i in range(-10, 20)])
graf_1.draw()
