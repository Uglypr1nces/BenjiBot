import random

class Game:
    def __init__(self):
        self.row1 = " | | "
        self.row2 = " | | "
        self.row3 = " | | "
        self.gameon = True

    def print_board(self):
        return f" {self.row1}\n{self.row2}\n{self.row3}"
    
    def reset_board(self):
        self.row1 = " | | "
        self.row2 = " | | "
        self.row3 = " | | "

    def update_board(self, row, index, player):
        if row == "1":
            self.row1[index] = player
        if row == "2":
            self.row2[index] = player
        if row == "3":
            self.row3[index] = player

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
        if row == "1":
            if self.row1[index] == " ":
                return True
        if row == "2":
            if self.row2[index] == " ":
                return True
        if row == "3":
            if self.row3[index] == " ":
                return True

    def play_move():
        row = random.randint(1,3)
        index = random.randint(1,3)
        if row == 1 and check_available_moves("1",index):
            self.update_board("1",index,"Y")
        if row == 2 and check_available_moves("2",index):
            self.update_board("2",index,"Y")
        if row == 3 and check_available_moves("3",index):
            self.update_board("3",index,"Y")
