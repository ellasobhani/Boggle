# Boggle board class
"""Extends the Board class with specific features required for Boggle"""

# import modules and classes
from graphics import *
from myrandom import randint
from boggleletter import BoggleLetter
from board import Board

# global variable to represent letters that can go on a boggle cube
CUBES =   [[ "A", "A", "C", "I", "O", "T" ],
           [ "T", "Y", "A", "B", "I", "L" ],
           [ "J", "M", "O", "Qu", "A", "B"],
           [ "A", "C", "D", "E", "M", "P" ],
           [ "A", "C", "E", "L", "S", "R" ],
           [ "A", "D", "E", "N", "V", "Z" ],
           [ "A", "H", "M", "O", "R", "S" ],
           [ "B", "F", "I", "O", "R", "X" ],
           [ "D", "E", "N", "O", "S", "W" ],
           [ "D", "K", "N", "O", "T", "U" ],
           [ "E", "E", "F", "H", "I", "Y" ],
           [ "E", "G", "I", "N", "T", "V" ],
           [ "E", "G", "K", "L", "U", "Y" ],
           [ "E", "H", "I", "N", "P", "S" ],
           [ "E", "L", "P", "S", "T", "U" ],
           [ "G", "I", "L", "R", "U", "W" ]]


class BoggleBoard(Board):
    """Boggle Board class implements the functionality of a Boggle board.
    It inherits from the Board class and extends it by creating a grid
    of BoggleLetters, shaken appropriately to randomize play."""

    __slots__ = ['_grid']

    def __init__(self):
        super().__init__()
        self._grid = []
        for col in range(self.cols):
            colLetters = [BoggleLetter(col, row) for row in range(self.rows)]
            self._grid.append(colLetters)


    def getLetterObj(self, pos):
        """Returns the letter object (that is, a BoggleLetter)
        at given grid position pos, a tuple of (column, row)"""
        col, row = pos
        return self._grid[col][row]

    def getLetter(self, pos):
        """Returns the text (string) of the BoggleLetter
        at given position pos, a tuple of (column, row)"""
        letObj = self.getLetterObj(pos)
        return letObj.letter

    def setLetter(self, pos, alph):
        """Given grid position pos, a tuple of (column, row),
        set the text of the BoggleLetter at that position to alph (a string)"""
        letObj = self.getLetterObj(pos)
        letObj.letter = alph

    def clearLetters(self):
        """Unclicks all boggle letters on the board without changing any other attribute
        "unclick" all BoggleLetters in the grid by resetting the appropriate attributes
        but do not change the text on the BoggleLetters."""
        #traversing through boggle board
        for col in range(self.cols):
            for row in range(self.rows):
                bogglelet = self._grid[col][row]
                #unclicking the bogglelet
                bogglelet.unclick()


    def reset(self):
        """Clears the boggle board by clearing letters,
        clears all text areas (right, lower, upper) on board
        and resets the letters on board by calling shakeCubes"""
        # for x in range(self.cols):
        #     for y in range(self.rows):
        #         boggleLet = self._grid[x][y]
        self.clearLetters()
        self.shakeCubes()
        self.clearTextArea()
        self.clearLowerText()
        self.clearUpperText()

    def drawBoard(self, win):
        """Draws the boggle board with all the letters on it.
        Overrides inherited drawBoard method of super class"""
        super().drawBoard(win)

        #traversing through boggle board
        for col in range(self.cols):
            for row in range(self.rows):
                #assigns bogglelet to a specific text obj on the grid
                bogglelet = self._grid[col][row]
                #draws bogglelet
                bogglelet.textObj.draw(win)

    def shakeCubes(self):
        """Shakes the boggle board and sets letters
        as described by the handout."""
        index = (self.cols*self.rows) - 1
        #traversing through boggle board
        for col in range(self.cols):
            for row in range(self.rows):
                #randomly choosing cube and side of cube
                cubeNumber = randint(0,index)
                sideNumber = randint(0,5)
                #setting new var equal to random boggleletter value
                bogLet = CUBES[cubeNumber][sideNumber]
                #creating tuple for position
                pos = (col, row)
                self.setLetter(pos, bogLet)
                #update index
                index -= 1

                #swap
                temp = CUBES[cubeNumber]
                CUBES[cubeNumber] = CUBES[index]
                CUBES[index] = temp

    def __str__(self):
        """ Returns a string representation of this BoggleBoard """
        #initialize variable board
        board = ''
        #traversing through boggle board
        for c in range(self.cols):
            for r in range(self.rows):
                color = self.getLetterObj((c,r)).color
                letter = self.getLetter((c,r))
                #add the letter:color of the boggleletter in the boggle board to the board var
                board += '[{}:{}] '.format(letter,color)
            #new line in board
            board += '\n'
        return board


if __name__ == "__main__":
    #pass
    win = GraphWin("Boggle", 400, 400)
    board = BoggleBoard()
    board.reset()
    board.drawBoard(win)

    exit = False
    while not exit:
       pt = win.getMouse()
       if board.inExit(pt):
           exit = True
       else:
           position = board.getPosition((pt.getX(), pt.getY()))
           print("{} at {}".format(board.getLetter(position), position))
