class Game:
    def __init__(self):
        self.row1 = " | | "
        self.row2 = " | | "
        self.row3 = " | | "

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


    