from gameboard import BoardClass
import socket
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


RECV_SIZE = 1024


class client:
    
    def __init__(self):
        #self.game = BoardClass()
        self.xclicked = True
        self.socket_connected = False
        self.count = 0
        self.game = BoardClass('', '')

        
        self.canvasSetup()
        print('canvassetup')
        self.initTKVariables()
        print('initvariables')
        self.original_button()
        print('original_button')
        self.game_info()
        print('game info')
        self.runUI()
        print('run')

    def initTKVariables(self):
        self.HOST = tk.StringVar()
        self.PORT = tk.IntVar()
        self.player1 = tk.StringVar()
        self.player2 = tk.StringVar()
        self.p_turn1 = tk.StringVar()
        self.n_win1 = tk.IntVar()
        self.n_ties1 = tk.IntVar()
        self.n_win11 = tk.IntVar()

    def connect_info(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.HOST.get(), self.PORT.get()))
        
        self.socket_connected = True
        
        if self.socket_connected:
            self.master.title('Tic Tac Toe Game Client(Successfuly connected)')
        print('connected')
            

    def start_game(self):
        self.player11 = self.player1.get()
        self.s.sendall(self.player11.encode('utf-8'))

        
        self.player22 = self.s.recv(RECV_SIZE).decode()
        self.player2.set(self.player22)
        self.player_2 = tk.Label(self.master, text='Player2:').grid(row = 1, column = 3, pady = 2, padx = 2)
        self.p2 = tk.Label(self.master, textvariable=self.player2).grid(row = 1, column = 4, sticky = 'W', pady = 2, padx = 2)
        
        self.game = BoardClass(self.player11, self.player22)

    def str_move(self):
        self.move1 = []
        for i in self.move:
            self.move1.append(str(i))
        self.move = ','.join(self.move1)

    def list_move(self):
        self.move1 = self.move.split(',')
        self.move = []
        for i in self.move1:
            if i != '':
                self.move.append(int(i))
                

    def canvasSetup(self):
        self.master = tk.Tk()
        self.master.title('Tic Tac Toe Game Client(Not connected)')
        self.master.geometry('750x700')
        self.master.configure(background = 'light blue')
        self.master.resizable(0,0)

    def game_info(self):
        #textvariable=self.HOST
        
        #First Row
        self.hostinfo = tk.Label(self.master, text='Host info:').grid(row = 0, column = 0, pady = 2, padx = 2)
        self.e1 = tk.Entry(self.master, textvariable=self.HOST).grid(row = 0, column = 1, sticky = 'W', pady = 2, padx = 2)
        self.portinfo = tk.Label(self.master, text='Port info:').grid(row = 0, column = 2, pady = 2, padx = 2)
        self.e2 = tk.Entry(self.master, textvariable=self.PORT).grid(row = 0, column = 3, sticky = 'W', pady = 2, padx = 2)
        self.connect_button = tk.Button(self.master, text='Connect', command=self.connect_info).grid(row = 0, column = 4, pady = 2, padx = 2)

        #Second Row 
        self.player_1 = tk.Label(self.master, text='Player1:').grid(row = 1, column = 0, pady = 2, padx = 2)
        self.p1 = tk.Entry(self.master, textvariable=self.player1).grid(row = 1, column = 1, sticky = 'W', pady = 2, padx = 2)
        self.p1_button = tk.Button(self.master, text='Submit P1', command=self.start_game).grid(row = 1, column = 2, pady = 2, padx = 2)
        self.player2.set('')
        self.player_2 = tk.Label(self.master, text='Player2:').grid(row = 1, column = 3, pady = 2, padx = 2)
        self.p1 = tk.Label(self.master, textvariable=self.player2).grid(row = 1, column = 4, sticky = 'W', pady = 2, padx = 2)

        #Third Row
        self.show_boardinfo()

        #Fourth Row
        self.show_final = tk.Label(self.master, text='Final Result:', font=('Helvetica', 25), bg='light blue').grid(row = 3, column = 2, pady = 2, padx = 2)

        #Fifth to Seventh Row
        self.stats_row()

        #Eight Row
        self.gameboard = tk.Label(self.master, text='GameBoard', font=('Helvetica', 25), bg='light blue').grid(row = 7, column = 2, pady = 2, padx = 2)

        #Ninth Row
        self.play_again = tk.Label(self.master, text='Play agian?:').grid(row = 8, column = 4, pady = 2, padx = 2)
        self.yes = tk.Button(self.master, text='Yes', textvariable=self.want_again).grid(row = 9, column = 4, sticky = 'W', pady = 2, padx = 2)
        self.no = tk.Button(self.master,text='No', textvariable=self.not_again).grid(row = 10, column = 4, sticky = 'W', pady = 2, padx = 2)

        #Tenth Row
        self.quitbutton = tk.Button(self.master, text='Quit', command=self.master.destroy).grid(row = 11, column = 3, pady = 2, padx = 2)

    def show_boardinfo(self):
        #Thrid Row
        self.p_turn1.set(self.game.turn)
        self.n_win1.set(self.game.wins)
        self.n_win11.set(self.game.losses)
        self.n_ties1.set(self.game.ties)
        

        self.whose_turn = tk.Label(self.master, text='Whose turn:').grid(row = 2, column = 0, pady = 2, padx = 2)
        self.p_turn = tk.Label(self.master, textvariable=self.p_turn1).grid(row = 2, column = 1, sticky = 'W', pady = 2, padx = 2)
        self.num_win = tk.Label(self.master, text='Wins:').grid(row = 2, column = 2, pady = 2, padx = 2)
        self.n_win = tk.Label(self.master, textvariable=self.n_win1).grid(row = 2, column = 3, sticky = 'W', pady = 2, padx = 2)


        
    def stats_row(self):
        #Fifth Row
        self.player_1 = tk.Label(self.master, text='Player1:').grid(row = 4, column = 0, pady = 2, padx = 2)
        self.p1 = tk.Label(self.master, textvariable=self.player1).grid(row = 4, column = 1, sticky = 'W', pady = 2, padx = 2)
        self.player_2 = tk.Label(self.master, text='Player2:').grid(row = 4, column = 2, pady = 2, padx = 2)
        self.p2 = tk.Label(self.master, textvariable=self.player2).grid(row = 4, column = 3, sticky = 'W', pady = 2, padx = 2)

        #Sixth Row
        self.num_win = tk.Label(self.master, text='Wins:').grid(row = 5, column = 0, pady = 2, padx = 2)
        self.n_win = tk.Label(self.master, textvariable=self.n_win1).grid(row = 5, column = 1, sticky = 'W', pady = 2, padx = 2)
        self.num_win = tk.Label(self.master, text='Wins:').grid(row = 5, column = 2, pady = 2, padx = 2)
        self.n_win = tk.Label(self.master, textvariable=self.n_win11).grid(row = 5, column = 3,sticky = 'W', pady = 2, padx = 2)
        self.num_tie = tk.Label(self.master, text='Ties:').grid(row = 5, column = 4, pady = 2, padx = 2)

        #Seventh Row
        self.num_loss = tk.Label(self.master, text='Losses:').grid(row = 6, column = 0, pady = 2, padx = 2)
        self.n_loss = tk.Label(self.master, textvariable=self.n_win11).grid(row = 6, column = 1, sticky = 'W', pady = 2, padx = 2)
        self.num_loss = tk.Label(self.master, text='Losses:').grid(row = 6, column = 2, pady = 2, padx = 2)
        self.n_loss = tk.Label(self.master, textvariable=self.n_win1).grid(row = 6, column = 3, sticky = 'W', pady = 2, padx = 2)
        self.n_tie = tk.Label(self.master, textvariable=self.n_ties1).grid(row = 6, column = 4, pady = 2, padx = 2)

        
        
    def b_click(self,b):
        while True:
            self.b = b
            if self.b['text'] == '' and self.xclicked == True:
                #X Turn
                self.show_boardinfo()
                self.b['text'] = 'X'
                self.move = [self.b.grid_info()['row']-8,self.b.grid_info()['column']-1]
                self.game.updateGameBoard(self.move)
                self.show_boardinfo()
                self.str_move()
                self.is_Win()
                if self.game.over == True:
                    self.s.sendall(self.move.encode('utf-8'))
                    self.xclicked = False
                    break
                else:
                    self.s.sendall(self.move.encode('utf-8'))
                    self.xclicked = False

                #O Turn
                self.show_boardinfo()
                self.move = self.s.recv(RECV_SIZE).decode()
                if self.move != '':
                    self.list_move()
                    self.game.updateGameBoard(self.move)
                    self.show_boardinfo()
                    self.b = tk.Button(self.master, text='O', font=('Helvetica', 20), height=5, width=10, command=lambda: self.b_click(self.b))
                    self.b.grid(row=self.move[0]+8, column=self.move[1]+1, pady=5)
                    self.is_Win()
                    self.xclicked = True
            else:
                messagebox.showerror('Tic Tac Toe', 'The box has already been selected\n Select another one')
            break
        
    def is_Win(self):
        #Check whether win or loss or tie
        if self.game.isWinner():
            if self.game.turn == 'X':
                self.game.updateGamesPlayed()
                print('Winner: '+self.player11)
                self.game.over = True
            elif self.game.turn == 'O':
                self.game.updateGamesPlayed()
                print('Winner: '+self.player22)
                self.game.over = True
        else:
            if self.game.boardIsFull():
                self.game.updateGamesPlayed()
                print('No Winner')
                self.game.over = True

        #Check want to play again or not
        if self.game.over == True:
            self.game_over = tk.Label(self.master, text='Game Over!', font=('Helvetica', 25), bg='pink').grid(row = 11, column = 2, pady = 2, padx = 2)
            print('game over')
            #Ninth Row
            self.play_again = tk.Label(self.master, text='Play agian?:').grid(row = 8, column = 4, pady = 2, padx = 2)
            self.yes = tk.Button(self.master, text='Yes', command=self.want_again).grid(row = 9, column = 4, sticky = 'W', pady = 2, padx = 2)
            self.no = tk.Button(self.master,text='No', command=self.not_again).grid(row = 10, column = 4, sticky = 'W', pady = 2, padx = 2)

    def want_again(self):
        self.s.sendall('y'.encode('utf-8'))
        self.game.resetGameBoard()
        self.original_button()
        self.show_boardinfo()
        self.xclicked = True
        self.game_over = tk.Label(self.master, text='Play again!', font=('Helvetica', 25), bg='pink').grid(row = 11, column = 2, pady = 2, padx = 2)
        print('Play Again!')

    def not_again(self):
        self.s.sendall('n'.encode('utf-8'))
        print('n')
        self.game_over = tk.Label(self.master, text='GoodBye!', font=('Helvetica', 25), bg='pink').grid(row = 11, column = 2, pady = 2, padx = 2)
        print('Fun Times!')
        self.game.computeStats()
        self.stats_row()
        
                
        
        
        

    def original_button(self):
        self.b1 = tk.Button(self.master, text='', font=('Helvetica', 20), height=5, width=10, command=lambda: self.b_click(self.b1))
        self.b2 = tk.Button(self.master, text='', font=('Helvetica', 20), height=5, width=10, command=lambda: self.b_click(self.b2))
        self.b3 = tk.Button(self.master, text='', font=('Helvetica', 20), height=5, width=10, command=lambda: self.b_click(self.b3))
        
        self.b4 = tk.Button(self.master, text='', font=('Helvetica', 20), height=5, width=10, command=lambda: self.b_click(self.b4))
        self.b5 = tk.Button(self.master, text='', font=('Helvetica', 20), height=5, width=10, command=lambda: self.b_click(self.b5))
        self.b6 = tk.Button(self.master, text='', font=('Helvetica', 20), height=5, width=10, command=lambda: self.b_click(self.b6))

        self.b7 = tk.Button(self.master, text='', font=('Helvetica', 20), height=5, width=10, command=lambda: self.b_click(self.b7))
        self.b8 = tk.Button(self.master, text='', font=('Helvetica', 20), height=5, width=10, command=lambda: self.b_click(self.b8))
        self.b9 = tk.Button(self.master, text='', font=('Helvetica', 20), height=5, width=10, command=lambda: self.b_click(self.b9))
        
        self.b1.grid(row=8, column=1, pady=5)
        self.b2.grid(row=8, column=2)
        self.b3.grid(row=8, column=3)
        
        self.b4.grid(row=9, column=1, pady=5)
        self.b5.grid(row=9, column=2)
        self.b6.grid(row=9, column=3)
        
        self.b7.grid(row=10, column=1, pady=5)
        self.b8.grid(row=10, column=2)
        self.b9.grid(row=10, column=3)
        
    def runUI(self):
        '''define a method start UI'''
        self.master.mainloop()
        
        



if __name__ == '__main__':
    a = client()


