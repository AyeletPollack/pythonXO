from table import table
from Player import player

if __name__ == '__main__':
    print('WELCOME !!\n')
    number = int(input('enter amount of rows and columns: \n'))
    table = table(number)
    player1 = player('X')
    player2 = player('O')
    playing = player1
    table.printtable()
    winner = False
    full = False
    while not winner and not full:
        print('Now its player with the shape: ' + playing.shape + '\n')
        row = int(input('enter row\n'))
        col = int(input('enter col\n'))
        while not table.checkIfAvailabe(row, col):
            print('enter again row and column')
            row = int(input('enter row\n'))
            col = int(input('enter col\n'))
        table.addToTablePlayer(row, col, playing)
        if table.checkWinner(playing):
            winner = True
        else:
            if table.checkAmount():
                full = True
            if playing == player1:
                playing = player2
            else:
                playing = player1
            table.printtable()

    table.printtable()
    if winner:
        print('player : ' + playing.shape + ' won!!')
    elif full:
        print('the bord if full :(')















