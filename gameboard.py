class BoardClass:

    def __init__(self, player1, player2, turn='',p1='X', p2='O', wins=0, ties=0, losses=0, count=0):

        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.player1 = player1
        self.player2 = player2
        self.turn = player1
        self.p1 = p1
        self.p2 = p2
        self.wins = wins
        self.ties = ties
        self.count = count
        self.losses = losses
        self.over = False

    def updateGamesPlayed(self):

        self.count += 1

    def resetGameBoard(self):

        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        print(self.board)
        self.turn = self.player1
        self.over = False

    def updateGameBoard(self, move):
        """Provide the move and update the new game board

            Decide whether player1 or player2 wins the game

        """
        if self.turn == self.player1:
            print(f'move1{move}')
            self.board[int(move[0])][int(move[1])] = self.p1
            self.turn = self.player2
            print('Next player: '+self.turn)
        elif self.turn == self.player2:
            print(f'move2{move}')
            self.board[int(move[0])][int(move[1])] = self.p2
            self.turn = self.player1
            print('Next player: '+self.turn)
            
        if self.isWinner():
            if self.turn == 'X':
                self.wins += 1
                self.updateGamesPlayed()
                print('Winner: '+self.player1)
                self.over = True
            elif self.turn == 'O':
                self.losses += 1
                self.updateGamesPlayed()
                print('Winner: '+self.player2)
                self.over = True
        else:
            if self.boardIsFull():
                self.ties += 1
                self.updateGamesPlayed()
                print('No Winner')
                self.over = True

    def isWinner(self):
        """Decide whether player1 or player2 wins the game

        Returns:
            True or False

        """
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] and self.board[row][0]!= ' ':
                self.turn = self.board[row][0]
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col]!= ' ':
                self.turn = self.board[0][col]
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0]!= ' ':
            self.turn = self.board[0][0]
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2]!= ' ':
            self.turn = self.board[0][2]
            return True
        return False

    def boardIsFull(self):
        """To check it the gameboard is full without a win

        """
        full = 0
        for row in range(3):
            for col in range(3):
                if self.board[row][col] != ' ':
                    full += 1
        if full == 9:
            return True
        else:
            return False

    def computeStats(self):
        """Print out all the information of the game

        """
        print('Player1: ' + self.player1)
        print('Player2: ' + self.player2)
        if self.turn == self.player2 or self.turn == 'X':
            print('Last turn of move: '+ self.player1)
        elif self.turn == self.player1 or self.turn == 'O':
            print('Last turn of move: '+ self.player2)
        print('Games played: ' + str(self.count))
        print('Player1: ' + self.player1)
        print('Player1 wins ' + str(self.wins) + ' games')
        print('Player1 losses ' + str(self.losses) + ' games')
        print('Player2: ' + self.player2)
        print('Player2 wins ' + str(self.losses) + ' games')
        print('Player2 losses ' + str(self.wins) + ' games')
        print('Ties: ' + str(self.ties))

