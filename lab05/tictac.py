import pytest

class TicTac:
    def __init__(self):
        self.board = [[None, None, None],
        [None, None, None],
        [None, None, None]]

    def placing(self, x, y, val):
        if self.board[x][y] == None:
            self.board[x][y] = val
        else:
            raise Exception

    def getVal(self, x, y):
        return self.board[x][y]

    def check_winner(self):
        # test row
        for row in self.board:
            if len(list(set(row))) == 1:
                return row[0]
        # test col
        print(len(self.board))
        for x in range(len(list(self.board))):
            if len(list(set(self.board[i][x] for i in range(len(list(self.board)))))) == 1:
                return self.board[0][x]
        # test dia
        if len(list(set(self.board[i][i] for i in range(len(list(self.board)))))) == 1:
            return self.board[0][0]
        if len(list(set(self.board[i][len(self.board) - i - 1] for i in range(len(list(self.board)))))) == 1:
            return self.board[0][len(list(self.board)) - 1]

def test1():
    one = TicTac()
    one.placing(0,1,'O')
    with pytest.raises(Exception):
        one.placing(0,1,'O')
            
def test2():
    one = TicTac()
    one.placing(0,1,'O')
    assert one.getVal(0,1) == 'O'

def test3():
    one = TicTac()
    one.placing(0,0,'O')
    one.placing(0,1,'O')
    one.placing(0,2,'O')
    assert one.check_winner() == 'O'

def test4():
    one = TicTac()
    one.placing(0,0,'O')
    one.placing(1,0,'O')
    one.placing(2,0,'O')
    assert one.check_winner() == 'O'

def test5():
    one = TicTac()
    one.placing(0,0,'O')
    one.placing(1,1,'O')
    one.placing(2,2,'O')
    assert one.check_winner() == 'O'
    
def test6():
    one = TicTac()
    one.placing(0,2,'O')
    one.placing(1,1,'O')
    one.placing(2,0,'O')
    assert one.check_winner() == 'O'


