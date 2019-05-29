from cell import *
import matplotlib.pyplot as plt
import random

class Maze:
    def __init__(self, N):
        self.size = N
        self.cells=[]
        for i in range(0, self.size):
            row = []
            self.cells.append(row)
            for j in range(0, self.size):
                row.append(Cell([i,j]))

        self.cells[0][0].setStart();
        self.cells[N-1][N-1].setEnd();

        self.__build();

    def __build(self):
        stack=[]
        currentCell = self.cells[0][0]
        currentCell.visit()

        visitCtr = 1
        while visitCtr<self.size*self.size:
            allAdjCelss=[]
            directions=[]
            if currentCell.getY()-1 >= 0:
                left = self.cells[currentCell.getX()][currentCell.getY()-1]
                if left.isVisit()==False:
                    allAdjCelss.append(left)
                    directions.append(Cell.LEFT)


            if currentCell.getY()+1 < self.size:
                right = self.cells[currentCell.getX()][currentCell.getY()+1]
                if right.isVisit() == False:
                    allAdjCelss.append(right)
                    directions.append(Cell.RIGHT)


            if currentCell.getX()+1 < self.size:
                up = self.cells[currentCell.getX()+1][currentCell.getY()]
                if up.isVisit() == False:
                    allAdjCelss.append(up)
                    directions.append(Cell.UP)

            if currentCell.getX() - 1 >=0:
                down = self.cells[currentCell.getX()-1][currentCell.getY()]
                if down.isVisit() == False:
                    allAdjCelss.append(down)
                    directions.append(Cell.DOWN)


            if allAdjCelss!=[]:
                stack.append(currentCell)
                num = len(allAdjCelss)
                chose = random.randint(0, num-1)

                direct = directions[chose]
                nextCell = allAdjCelss[chose]


                if direct==Cell.UP:
                    currentCell.removeWall(Cell.UP)
                    nextCell.removeWall(Cell.DOWN)
                if direct==Cell.DOWN:
                    currentCell.removeWall(Cell.DOWN)
                    nextCell.removeWall(Cell.UP)
                if direct==Cell.LEFT:
                    currentCell.removeWall(Cell.LEFT)
                    nextCell.removeWall(Cell.RIGHT)
                if direct==Cell.RIGHT:
                    currentCell.removeWall(Cell.RIGHT)
                    nextCell.removeWall(Cell.LEFT)

                nextCell.visit()
                visitCtr=visitCtr+1
                currentCell = nextCell
            else:
                if(stack!=[]):
                    preCell = stack[len(stack)-1]
                    stack.pop(len(stack)-1)
                    currentCell = preCell





    def printMaze(self):
        h = 30
        y=0
        for i in range(0, self.size):
            x=0
            for j in range(0, self.size):
                cell = self.cells[i][j]
                cell.draw(plt, x, y, h)
                x = x+h

            y=y+h

        plt.axis('equal')
        plt.axis('off')
        plt.show()



