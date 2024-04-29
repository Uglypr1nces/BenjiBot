import random

class Game:
    def __init__(self):
        self.row1 = [""] * 3
        self.row2 = [""] * 3
        self.row3 = [""] * 3

    def print_board(self):
        board = f"{self.row1}\n{self.row2}\n{self.row3}"
        return board
    
    def reset_board(self):
        self.row1 = [""] * 3
        self.row2 = [""] * 3
        self.row3 = [""] * 3

    def update_board(self, row, index, player):
        if row == 1:
            self.row1[index] = player
        elif row == 2:
            self.row2[index] = player
        elif row == 3:
            self.row3[index] = player
        else:
            print("Invalid row")


    def check_winner(self):
        if self.row1[1] == self.row1[4] == self.row1[7]:
            return self.row1[1]

        if self.row2[1] == self.row2[4] == self.row2[7]:
            return self.row2[1]

        if self.row3[1] == self.row3[4] == self.row3[7]:
            return self.row3[1]
        
        if self.row1[1] == self.row2[1] == self.row3[1]:
            return self.row1[1]

        if self.row1[4] == self.row2[4] == self.row3[4]:
            return self.row1[4]

        if self.row1[7] == self.row2[7] == self.row3[7]:
            return self.row1[7]
        
        if self.row1[1] == self.row2[4] == self.row3[7]:
            return self.row1[1]

        if self.row1[7] == self.row2[4] == self.row3[1]:
            return self.row1[7]

    def check_available_moves(self, row, index):
        if row == 1:
            if self.row1[index] == "":
                return True
        elif row == 2:
            if self.row2[index] == "":
                return True
        elif row == 3:
            if self.row3[index] == "":
                return True
        else:
            print("available moves:")
            print(self.send_available_moves())
            print(f"choosen moves: \nrow: {row}, index: {index}")
            return False
 
    def send_available_moves(self):
        available_moves = []
        for i in range(3):
            if self.row1[i] == "":
                available_moves.append(f"1.{i}")
            if self.row2[i] == "":
                available_moves.append(f"2.{i}")
            if self.row3[i] == "":
                available_moves.append(f"3.{i}")
        return available_moves

    def play_move(self):
        while True:
            row = random.randint(1, 3)
            print(f"row: {row}")
            index = random.randint(0, 2)
            print(f"index: {index}")

            if row == 1 and self.check_available_moves(1, index): 
                print("move available")
                self.update_board(1, index, "Y")
                break
            if row == 2 and self.check_available_moves(2, index):
                print("move available")
                self.update_board(2, index, "Y")  
                break
            if row == 3 and self.check_available_moves(3, index):
                print("move available")
                self.update_board(3, index, "Y") 
                break
