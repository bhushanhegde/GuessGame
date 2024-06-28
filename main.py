import random

class Game:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.idx = 0
        self.numbers = []
        self.first = None
        self.second = None 
        self.moves = 0
        self.opened = set()

    def initialise_board(self, rows = 5, cols = 5):
        self.rows = min(rows, 9)
        self.cols = min(cols, 9)
        self.numbers = [num for num in range(1, (self.rows * self.cols) // 2 + 1)] * 2
        random.shuffle(self.numbers)
        print(self.numbers)
        self.print_full_pattern()

    def print_full_pattern(self):
        for row in range(self.rows):
            self.print_pattern(row)
            print()
            print()
    
    def print_pattern(self, row):
        # print("****** "*self.cols)
        # print("****** "*self.cols)
        idx = row * self.cols
        for _ in range(self.cols):
            if idx not in self.opened and self.first != idx and self.second != idx: 
                print(str(idx+1).center(6, "*"), end = ' ')
            else:
                print(str(self.numbers[idx]).center(6, '#'), end = ' ')
            idx += 1
        print()
        # print("****** "*self.cols)
        # print("****** "*self.cols)
    
    def take_input(self):
        while self.first == None or self.second == None:
            try:
                print("Enter the card number to open")
                inp = int(input())
                if inp > len(self.numbers) or inp <= 0:
                    print("Enter the numbers in range")
                else:
                    if self.first is None:
                        self.first = inp-1 
                        self.print_full_pattern()
                    else:
                        if self.first != inp:
                            self.second = inp-1
                            self.print_full_pattern()
                        else:
                            print("First and Second number can't be same")  
            except:
                print("Enter the correct number") 

    
    def start_game(self):
        while True:
            self.take_input()
            self.moves += 2
            if self.numbers[self.first] == self.numbers[self.second]:
                self.opened.add(self.first)
                self.opened.add(self.second)
                if len(self.opened) == len(self.numbers):
                    print(f"Finished with {self.moves} moves")
                else:
                    print("Nice work. You got a match")
                    self.first = None 
                    self.second = None
            else:
                self.first = None 
                self.second = None 
        


g = Game()
g.initialise_board()
g.start_game()

            
# def f(a=1, b=2, c=3):
#     print("Hello")
#     print(a,b,c)

# def f1(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     kwargs['fn'](10)

    

# f(1,2,3)
# f(10, b = 20, c=30)
# f1(1,1000000,10000,1000,100,10, fn = f)
