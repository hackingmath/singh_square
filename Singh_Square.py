'''Magic Square from Singh
https://twitter.com/Mathgarden/status/1039247616616194048
Sept 10, 2018'''


from random import sample, shuffle

class Cell(object):
    def __init__(self,contents):
        self.open = True
        self.contents = contents#'' #starts off empty

class Grid(object):
    '''creates an m x n grid'''
    def __init__(self,m,n,inputList):
        self.m = m #rows
        self.n = n #cols
        self.cellList = []
        self.inputList = inputList
        index = 0
        for r in range(m):
            self.cellList.append([])
            for c in range(n):
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


g = Grid(5,5,[0,0,0,'H',0,
              0,0,0,0,0,
              0,'H',0,0,0,
              0,0,0,0,0,
              'H',0,0,0,0])
g.render()
print(g.scoreList())
'''for row in g.cellList:
    for c in row:
        print(c.open,end = ' ')
    print()'''
