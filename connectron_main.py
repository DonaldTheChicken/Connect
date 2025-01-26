from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout
from connectron_ui import Ui_MainWindow
import time, sys

"""
Connectron

0-10 Players
Size of Grid: 6x6 - 100x100

Length of line needed to win: 4-10 (chosen at the start of the game)
Line can be vertical, horizontal or both diagonals

Players take time to drop a counter into a column
The counter falls to the bottom of the column

A counter in any of the corners is special and counts as more, so less counters are needed for a winning line.
If the winning line length is 6 or less, corner counters count as 2
If the winning line length is 7 or more, corner counters count as 3

If a counter is completely surrounded by counters from one other player, it disappears and all the counters above it move down by one. This is kind of like GO.

Once per game, a player can place a bomb-counter that when placed, detonates and destroys itself and any immediately adjacent counters. (Ill interpret immediately adjacent as counters above, left, right and below)

If the board is at least 6 rows, any counter filling a column completely will overflow into adjacent columns
If there are two adjacent columns, it overflows into both, and both will gain a counter (this is how i interpreted the task)



Players can choose to play a best of 3 or best of 5, and the winner is the player with the most amount of wins after that many rounds



Alliances

"""

def save_score():
    pass

class Game: #Handles a Game until someone wins or board fills
    def __init__(self):
        #2D Nested List to hold the board and its pieces
        self.row_count = 0
        self.col_count = 0
        #the board is a list of rows
        #the bottom of the board is the highest row_num
        
        self.player_count = 0 #the AIs are counted at the front of this. The AIs go first.
        #if there is 1 AI, the first player is an AI.
        self.ai_count = 0 #
        self.move_count = 0 #number of moves that have occured

        self.alliances = [] #
        self.alliance_count = 0

        self.bomb_size = 1 #how big of a square the bomb deletes (1 in each direction)

        self.colours = (
            ("Blank", "#B2BABB"),
            ("Red", "#FF0000"),
            ("Blue", "#0000FF"),
            ("Green", "#00FF00"),
            ("Yellow", "#FFFF00"),
            ("Orange", "#FFA500"),
            ("Purple", "#800080"),
            ("Cyan", "#00FFFF"),
            ("Pink", "#FFC0CB"),
            ("Magenta", "#FF00FF"),
            ("Lime", "#BFFF00")
        )

        self.infinite_overflow = True
        self.bombs_enabled = True

        self.current_turn = 0

        self.win_len = 4

        self.row_count = 6
        self.col_count = 6

    
    def set_size(self, r_num, c_num):
        self.row_count = r_num
        self.col_count = c_num
        self.grid = [[0 for i in range(self.col_count)] for j in range(self.row_count)]
    
    def set_win_len(self, w_len):
        self.win_len = w_len
    
    def set_players(self, p_num):
        self.player_count = p_num
        if p_num < 2:
            self.ai_count = 2-p_num
            self.player_count = 2
        else:
            self.ai_count = 0

        self.alliances = [0 for i in range(self.player_count)]

    def new_alliance(self, new_alliance_members):
        self.alliance_count += 1
        for new_member in new_alliance_members:
            self.alliances[new_member] = self.alliance_count
    
    def del_alliance(self, delete_alliance_num):
        self.alliances.remove(delete_alliance_num)
    
    def add_members(self, alliance_num, new_members):
        for new_member in new_members:
            self.alliances[new_member] = alliance_num
    
    def print_board(self):
        for row in self.grid:
            print("|".join([(str(i) if i > 0 else ".") for i in row]))
        
        return self.grid

    def insert(self, inserted_column):
        #insert counter into a column

        #need to handle
        #overflows
        #solitaire (go)
        
        if self.grid[0][inserted_column]:
            #column is full
            #overflow
            col1 = col2 = inserted_column

            #looking left
            while self.grid[0][col1]: #while the column is full
                col1 -= 1
                if col1 < 0:
                    break

            if col1 >= 0:
                self.grid[0][col1] = self.current_turn+1
                self.gravity()
            
            #looking right
            while self.grid[0][col2]: #while the column is full
                col2 += 1
                if col2 >= self.col_count:
                    break
                
            if col2 < self.col_count:
                self.grid[0][col2] = self.current_turn+1
                self.gravity()

        else:
            #not full
            #insert counter
            lowest_empty = self.row_count
            for i in range(self.row_count):
                if self.grid[i][inserted_column] == 0:
                    lowest_empty = i
            
            self.grid[lowest_empty][inserted_column] = self.current_turn+1
        

        
        #next turn
        #turn ranges from 0 to playercount-1
        #in the grid, players are represented by 1 to playercount
        #in the grid, a 0 represents an empty square
        self.current_turn = (self.current_turn+1)%self.player_count
        pass

    def gravity(self):
        #parse through grid, if there are floating counters,
        #collapse them down.
        for col_num in range(self.col_count):
            old_column = [self.grid[i][col_num] for i in range(self.row_count)]
            for i in range(self.row_count):
                if old_column[i] != 0:
                    highest_counter = i
                    break
            new_column = []
            for i in range(self.row_count-1, highest_counter-1, -1):
                #[5, 4, 3, 2, 1, 0]
                if old_column[i] != 0:
                    new_column.append(old_column[i])
            new_column.extend([0]*(self.row_count-len(new_column)))

            for i in range(self.row_count):
                self.grid[i][col_num] = new_column[self.row_count-i-1]

        return 0
    

    def solitaire(self):
        #parse through the grid, finding tiles surrounded by one single colour.
        #remove
        pass

    def bomb(self, bomb_coord):
        #bomb
        return 0
    
    def check_sequence(self, sequence):
        #check if there is a winner in a sequence (basically a list)
        #return the winner, return 0 if no winner

        cur_len = 1 #length of current continuous sequence
        for tile_num in range(1, len(sequence)):
            if sequence[tile_num] == 0:
                cur_len = 1
            else:
                if sequence[tile_num] == sequence[tile_num-1]:
                    cur_len += 1
                else:
                    cur_len = 1
            if cur_len == self.win_len:
                return 1
        return 0

    def check_win(self):
        #check if there's a winner

        #rows
        for row_num in range(self.row_count):
            pass
                
            

        #columns
        for col_num in range(self.col_count):
            pass
        

        return 0
    
    def computer_move(self):
        #generate the optimal computer AI player move
        #given the current turn
        #add a counter to the longest current line of its colour
        #that can be added to. If there is a counter under the position, it is valid.
        pass
    


def main():
    #main logic
    return 0

def menu_main():

    return 0


def test_game():
    #test game without GUI
    game1 = Game()
    game1.set_players(3)
    game1.set_size(6, 8)
    game1.set_win_len(4)
    game1.new_alliance([0])
    game1.add_members(1, [2])
    # game1.print_board()
    game1.insert(0)
    game1.insert(0)
    game1.insert(1)
    game1.insert(2)
    game1.insert(2)
    game1.insert(3)
    game1.insert(6)
    game1.insert(6)
    game1.insert(6)
    game1.insert(6)
    game1.insert(6)
    game1.insert(6)
    game1.insert(6)
    game1.print_board()

test_game()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.switch_page(0)

        #connecting button events to methods
        self.ui.pushButton_NewGame.clicked.connect(self.NewGame_pressed)
        self.ui.pushButton_NewGame_2.clicked.connect(self.NewGame_2_pressed)

    def NewGame_pressed(self):
        #First NewGame button was pressed.
        #Width, Height, PlayerCount
        self.game = Game()
        self.game.set_size(self.get_int(0), self.get_int(1))

        self.game.set_players(self.get_int(2))
        self.create_board(self.game.row_count, self.game.col_count)

        self.switch_page(1)

        
    def NewGame_2_pressed(self):
        self.game.set_win_len(self.get_int(3))
        self.round_count = self.get_int(4)

        self.switch_page(2)


    def create_board(self, board_rnum, board_cnum):
        #creates the gridlayout with the buttons
        self.board_buttons = [[] for i in range(board_rnum)]
        for i in range(board_rnum):
            for j in range(board_cnum):
                self.board_buttons[i].append(QPushButton())
                # self.board_buttons[i][j]



        for button_rnum in range(board_rnum):
            for button_cnum in range(board_cnum):
                self.ui.gridLayout_Board.addWidget(self.board_buttons[button_rnum][button_cnum], button_rnum, button_cnum)
                
        

    def switch_page(self, stacked_page_num):
        #switches the stacked_widget_menu page number
        """
        0: width, height, playercount
        1: Win len, Round number
        2: Alliances
        3: Game
        4: Result
        5: Change Alliances?
        """
        self.ui.stackedWidget_Menu.setCurrentIndex(stacked_page_num)

    def get_int(self, button_num):
        """
        0: board height
        1: board width
        2: player count
        3: win len
        4: round num
        """
        #easily get the integer inside a PlainTextEdit
        text_edits = [
            self.ui.plainTextEdit_BoardHeight,
            self.ui.plainTextEdit_BoardWidth,
            self.ui.plainTextEdit_PlayerCount,
            self.ui.plainTextEdit_WinningLength,
            self.ui.plainTextEdit_RoundNum
            ]
        
        return int(text_edits[button_num].toPlainText())

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

