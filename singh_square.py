'''Magic Square from Singh
https://twitter.com/Mathgarden/status/1039247616616194048
Sept 10, 2018'''


from random import sample, shuffle

N_HUNTERS = 5
COLS = 5
ROWS = 5

class Cell(object):
    def __init__(self,contents):
        self.open = True
        self.contents = contents

class Grid(object):
    '''creates an m x n grid
    defaults to 5x5'''
    def __init__(self):
        self.m = ROWS #rows
        self.n = COLS #cols
        self.inputList = [0 for i in range(25)]
        indices = sample(list(range(25)),N_HUNTERS)
        #print(indices)

        for num in indices:
            self.inputList[num] = 'H'
            
        self.cellList = []
        #self.inputList = inputList
        index = 0
        for r in range(self.m):
            self.cellList.append([])
            for c in range(self.n):
                self.cellList[r].append(Cell(self.inputList[index]))
                index += 1
        self.score = 0

    def hunt(self):
        '''fills in rows, cols and diags of
        hunters'''
        output = [[0 for j in range(self.n)] for i in range(self.m)]
        for r, row in enumerate(self.cellList):
            for c,cell in enumerate(row):
                #cell is self.cellList[r][c]
                if cell.contents != 'H':
                    continue
                else:
                    #replace rows and columns with '_'
                    for x in range(5):
                        if self.cellList[r][x].contents != 'H':
                            self.cellList[r][x].contents = '_'
                    
                        if self.cellList[x][c].contents != 'H':
                            self.cellList[x][c].contents = '_'

                    #check down diagonal
                    diff = c - r
                    for m in range(self.m):
                        for n in range(self.n):
                            if n - m == diff:
                                if self.cellList[m][n].contents != 'H':
                                    self.cellList[m][n].contents = '_'
                    #check up diagonal
                    add = r + c
                    for m in range(self.m):
                        for n in range(self.n):
                            if m + n == add:
                                if self.cellList[m][n].contents != 'H':
                                    self.cellList[m][n].contents = '_'

                
    def scoreList(self):
        output = 0
        for row in self.cellList:
            for c in row:
                if c.contents == 0:
                    output += 1
        return output
    
    def render(self):
        self.hunt()
        for row in self.cellList:
            #print(' | ',end = '')
            for c in row:
                print(c.contents,end = ' ')
            print()#'\n',' __________')

    
    

def shuffleList(a):
    output = list(a)
    shuffle(output)
    return output

N_HUNTERS = 5

'''g = Grid([0,0,0,'H',0,
        0,0,0,0,0,
        0,'H',0,0,0,
        0,0,0,0,0,
        'H',0,0,0,0])'''

while True: #for k in range(10000):
    g = Grid()
    g.hunt()
    sc = g.scoreList()
    print(sc)
    if sc == 3:
        g.render()
        break
    #print(g.scoreList())

'''Solution:
0 0 _ _ _ 
_ _ _ H H 
_ _ _ _ H 
0 _ _ _ _ 
_ _ H H _

'''
