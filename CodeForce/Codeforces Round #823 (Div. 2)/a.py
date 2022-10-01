import random
import numpy as np


class Sudoku():

    def __init__(self, n_classes, courses):
        self.board = np.zeros([4, 5, n_classes])
        self.n_classes = n_classes
        self.courses = courses
        
    
    def empty_cell(self):
        for i in range(4):
            for j in range(5):
                for k in range(self.n_classes):
                    if self.board[i, j, k] == 0:
                        return i, j, k
    

    def is_valid(self, time, day, clas, course):

        if course in self.board[:, day, clas]:
            return False
        
        #add spread of same course
        
        return True


    def solve(self):
        if len(self.courses) == 0:
            return True

        time, day, clas = self.empty_cell()

        for course in self.courses:
            if self.is_valid(time, day, clas, course):
                self.board[time, day, clas] = course
                self.courses.remove(course)
                if self.solve():
                    return True
                self.board[time, day, clas] = 0
                self.courses.append(course)
        
        return False
    

    def print(self):
        for i in range(self.n_classes):
            print(self.board[:, :, i])


            
n = 2
courses = [1,1,1,2,2,2,2,2,2,2,2,3,3,3,4,4,5,5,6]

S = Sudoku(n, courses)
S.solve()
S.print()