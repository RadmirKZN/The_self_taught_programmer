class Horse():
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
    def print_horse(self):
        print(self.height, self.weight)
    def enter_size(Horse):
        self.height=input('Enter size:')
        self.weight=input('Enter sizze:')
        print(self.height, self.weight)

horse_1 = Horse(100, 100)
horse_2 = Horse(50, 50)
horse_1.print_horse()
horse_2.print_horse()
        
