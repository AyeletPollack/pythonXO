

class table:

    def __init__(self, number):
        self.table = [['-' for i in range(number) ] for j in range(number)]
        self.number = number
        self.amountInput = 0

    def checkIfAvailabe(self, row, col):
        if row >= self.number or col >= self.number or row < 0 or col < 0 or self.table[row][col] != '-':
            return False
        return True
    def addToTablePlayer(self, row, col, player):
        self.table[row][col] = player.shape

    def printtable(self):
        print(' ', end=' ')
        for i in range(self.number):
            print(i, end=' ')
        print('\n')
        for i in range(self.number):
            print(i , end=' ')
            for j in range(self.number):
                print(self.table[i][j], end=' ')
            print()

    def checkAmount(self):
        if self.amountInput == self.number*self.number:
            return True
        return False

    def checkWinner(self, player):
        for i in range(self.number):
            count = 0
            for j in range(self.number):
                if self.table[i][j] == player.shape:
                    count += 1
            if count == self.number:
                return True
        for i in range(self.number):
            count = 0
            for j in range(self.number):
                if self.table[j][i] == player.shape:
                    count += 1
            if count == self.number:
                return True
        i = 0
        j = 0
        count = 0
        while i < self.number and j < self.number:
            if self.table[i][j] == player.shape:
                count += 1
            i += 1
            j += 1
        if count == self.number:
            return True
        i = self.number-1
        j = 0
        count = 0
        while i >= 0 and j < self.number:
            if self.table[i][j] == player.shape:
                count += 1
            i -= 1
            j += 1
        if count == self.number:
            return True
        return False






