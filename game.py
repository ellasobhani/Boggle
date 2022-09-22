# script game.py
"""Implements the logic of the game of boggle."""

# import all relevant packages and classes
from graphics import *
from random import randint
from boggleboard import BoggleBoard
from boggleletter import BoggleLetter
from bogglewords import BoggleWords

# This helper function creates the Boggle lexicon.
def lexicon(filename='bogwords.txt'):
    """Reads words (one per line) from filename (by default 'bogwords.txt')
    and returns a set of all words"""
    result = set()
    with open(filename) as f:
        for lines in f:
            result.add(lines.strip())
    return result

def setup(win, board):
    """Given a graphical window and BoggleBoard board,
    sets up the game board by resetting the letters on it
    and drawing the board with letters"""
    board.reset()
    board.drawBoard(win)

def resetLower(board):
    """Given a BoggleBoard board, clears the letters on the board,
    along with the lower text area"""
    board.clearLetters()
    board.clearLowerText()

def update(board, bWords):
    """Updates the state of the BoggleBoard board after a valid word has been found
    and added to BoggleWords bWords; updates right text area, clears lower
    text area, and resets BoggleLetters to unclicked state."""
    board.clearLetters()
    board.setTextArea(bWords.allWords)
    resetLower(board)
    bWords.clearCurrentWord()


def play(win, board):
    """Given a graphical window and a BoggleBoard board, implements the logic
    for playing the game"""

    # initialize flag and boggle words
    exitFlag = False

    # populate the lexicon
    validWords = lexicon()

    # initialize an empty BoggleWords object
    bWords = BoggleWords()

    while not exitFlag:

        # first find (col, row) coord of mouse click
        point = win.getMouse()
        coord = board.getPosition((point.getX(), point.getY()))

        # step 1: check for exit button and exit
        if board.inExit(point):
            exitFlag = True

        # step 2: check for reset button and reset
        if board.inReset(point):
            board.reset()
            bWords.reset()

        # step 3: check if click is on a cell in the grid
        if board.inGrid(point):

            # get BoggleLetter at that position
            bogLet = board.getLetterObj(coord)
            # if starting a new word, add letter and display it on lower text of board
            if bWords.currWord == []:  #could be problematic
                bWords.addLetter(bogLet)
                board.addStringToLowerText(bogLet.letter)
                bogLet.click()


            # if adding letter to existing word, check for adjacency, update state
            else:
                latestLetter = bWords.currWord[-1]
                latestLetter.color = "green"

                if latestLetter.isAdjacent(bogLet) and not bogLet.isClicked: #commenty comment
                    bWords.addLetter(bogLet)
                    board.addStringToLowerText(bogLet.letter)
                    bogLet.click()


                # if clicked on same letter as last time, end word, check for validity
                # if word is valid update bWords
                elif bogLet == latestLetter and bWords.wordStr.lower() in validWords:
                    bWords.addWord()
                    update(board, bWords)
                # if clicked on some other letter, cancel word, reset state
                else:
                    update(board, bWords)






if __name__ == '__main__':
    win = GraphWin("Boggle", 400, 400)
    board = BoggleBoard()
    setup(win, board)
    play(win, board)
