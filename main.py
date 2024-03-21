'''
What do i need to play this game?

1. Board representation

2. Two players and their representation 

3. Ability for player to make a move

4. Store and represent the player move

5. Ability to switch turns from player to player

6. Ability to determine a winner after every move

7. End the game once a winner is found

'''

import numpy as np

class TicTacToe:
    """Models the tic tac toe game"""
    # initialize an empty board
    def __init__(self):
        self.board = ""
        self.current = ""
        self.next = ""
        self.solution = np.zeros((3,3), dtype=int)

    def blankBoard(self):
        for i in range(5):
            # switch between printing vertical and horizontal bars
            if i%2 == 0:
                self.board += "|    " * 4
            else:
                self.board += " --- " * 3
            # don't forget to start a new line after each row using "\n"
            self.board += "\n"

        return

    def showBoard(self):
        print(self.board)

        return 

    def instructions(self):
        print(
            """
            ---------------------------------------------
                        WELCOME TO TIC TAC TOE
            ---------------------------------------------
            - This is a two player game
            - Abide by the rules and have fun!
            - To play, input the row and column you want to play in as a tuple
            For example 1,2 means I want to play in row 1 column 2
            \n
            """
        )

        return

    def playerSelect(self):
        valid = ["x", "o"]

        current = input("\nSelect which player you want to be (x, o): ")
        current = current.lower()
        if current not in valid:
            print("\nWrong selection, try again")

            return False
        else:
            self.current = current
            if current == "x":
                self.next = "o"
            else:
                self.next = "x"

            print("\n Awesome! Let the games begin!!!!")

            return True

    def playerMove(self):
        return input("\n Player {}, it is your turn, What row and column do you want to play in? --> row,column: ".format(self.current))
        
    def isMoveValid(self, move):
        valid = [1, 2, 3]

        moveList = move.split(',')

        if len(moveList) != 2:
            print("\nWrong selection, try again")
            return False

        for move in moveList:
            try:
                if int(move) not in valid:
                    print("\nWrong selection, try again")
                    return False
            except ValueError:
                    print("\nWrong selection, try again")
                    return False

        row = int(moveList[0])
        col = int(moveList[1])

        if self.solution[row-1][col-1] != 0:
            print("\nSpace on board is occupied")
            return False

        return True

    def addMove(self, move):
        moveList = move.split(",")
        row = int(moveList[0])
        col = int(moveList[1])

        board_list = self.board.split('\n')

        for index, section in enumerate(board_list):
            if (row*2) - 2 == index:
                new_section = list(section)
                new_section[(col*5)-3] = self.current
                new_new = ''.join(new_section)
                board_list[index] = new_new

        self.board = '\n'.join(board_list)

        if self.current == "x":
            self.solution[row-1][col-1] = 1
        else:
            self.solution[row-1][col-1] = 2

        return

    def switchPlayer(self):
        temp = self.current
        self.current = self.next
        self.next = temp

        return False

    def isGameOver(self):
        # Check Row
        for row in self.solution:
            if (np.sum(row) % 3 == 0) and (np.sum(row) != 0) and (np.all(row != 0)):
                self.showBoard()
                print("\n Game Over, player {} wins!".format(self.current))
                return True

        # Check column
        for col in self.solution.T:
            if (np.sum(col) % 3 == 0) and (np.sum(col) != 0) and (np.all(col != 0)):
                self.showBoard()
                print("\n Game Over, player {} wins!".format(self.current))
                return True
    
        # Check main diagonal
        if (np.sum(np.diag(self.solution)) % 3 == 0) and (np.sum(np.diag(self.solution)) != 0) and (np.all(np.diag(self.solution) != 0)):
            if self.solution[0, 0] == 1:
                self.showBoard()
                print("\n Game Over, player {} wins!".format(self.current))
                return True
    
        # Check secondary diagonal
        if (np.sum(np.diag(np.fliplr(self.solution))) % 3 == 0) and (np.sum(np.diag(np.fliplr(self.solution))) != 0) and (np.all(np.diag(np.fliplr(self.solution)) != 0)):
            if self.solution[0, 0] == 1:
                self.showBoard()
                print("\n Game Over, player {} wins!".format(self.current))
                return True

        # No more moves
        if np.all(self.solution != 0):
            self.showBoard()
            print("\n Game Over, its a tie!")
            return True
    
        return False
            

if __name__ == "__main__":
    game = TicTacToe()
    game.blankBoard()
    game.instructions()

    playerSelected = False
    gameOver = False
    valid = False

    while not playerSelected:
        playerSelected = game.playerSelect()
    
    while not gameOver:
        game.showBoard()
        while not valid:
            move = game.playerMove()
            valid = game.isMoveValid(move)
        game.addMove(move)
        gameOver = game.isGameOver()
        valid = game.switchPlayer()


