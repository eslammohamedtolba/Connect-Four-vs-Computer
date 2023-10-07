
class Board:
    def __init__(self):
        while True:
            self.RowSize = int(input("Enter number of rows for Board Size that greater than 3: "))
            self.ColSize = int(input("Enter number of Columns for Board Size that greater than 3: "))
            if self.RowSize>3 and self.ColSize>3:
                break
        self.Board = [[' ']*self.ColSize for row in range(self.RowSize)]
    
    def X_axis(self,Y):
        counter=0
        for IndexRow in range(self.RowSize-1,-1,-1):
            if self.Board[IndexRow][Y-1] !=' ':counter+=1
            else:break
        return self.RowSize-counter
    def UpdateBoard(self,Y,Symbol):
        # Check the column is valid
        if Y>0 and Y<=self.ColSize:
            X = self.X_axis(Y)
            # Check the row is valid if isn't filled
            if X>0:
                self.Board[X-1][Y-1] = Symbol
                return True
        return False

    def PrintBoard(self):
        print()
        for col in range(self.ColSize):
            print(f"    {col+1}    ",end="")
        print()
        print("--------"*self.ColSize+"-"*(1+self.ColSize))
        for i in range(self.RowSize):
            print("| ",end="")
            for j in range(self.ColSize):
                print(f"   {self.Board[i][j]}  ",end = ' | ')
            print()
            print("--------"*self.ColSize+"-"*(1+self.ColSize))
        print()

    def IsWinner(self,Symbol):
        # columns
        for IndexCol in range(self.ColSize):
            counter=0
            for IndexRow in range(self.RowSize-1,-1,-1):
                if self.Board[IndexRow][IndexCol] == Symbol:counter+=1
                elif self.Board[IndexRow][IndexCol]==' ':break
                else:counter=0
                if counter==4:return True
        # rows
        for row in self.Board:
            counter=0
            for value in row:
                if value == Symbol:counter+=1
                else:counter=0
                if counter==4:return True
        # diagonal_lr
        for X in range(self.RowSize-2,2,-1):
            x = X
            y=counter=0
            while y<self.ColSize and x>=0:
                if self.Board[x][y]==Symbol:counter+=1
                else:counter=0
                if counter==4:return True
                y+=1
                x-=1
        for Y in range(0,self.ColSize-3):
            y=Y
            x=self.RowSize-1
            counter=0
            while y<self.ColSize and x>=0:
                if self.Board[x][y]==Symbol:counter+=1
                else:counter=0
                if counter==4:return True
                y+=1
                x-=1

        # diagonal_rl
        for X in range(self.RowSize-2,2,-1):
            x = X
            y=self.ColSize-1
            counter=0
            while y>=0 and x>=0:
                if self.Board[x][y]==Symbol:counter+=1
                else:counter=0
                if counter==4:return True
                y-=1
                x-=1
        for Y in range(self.ColSize-1,2,-1):
            y=Y
            x=self.RowSize-1
            counter=0
            while y>=0 and x>=0:
                if self.Board[x][y]==Symbol:counter+=1
                else:counter=0
                if counter==4:return True
                y-=1
                x-=1
                
        return False
        
    def IsDraw(self):
        for row in self.Board:
            if row.count(' ')>0:
                return False
        return True
