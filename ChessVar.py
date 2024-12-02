# Author: Josue Vicente Cruz
# GitHub username: JosueCruz666666
# Date: 08/17/2023
# Description: Creates a variation of the game, Chess. Classes used are Piece and ChessVar. There are some rules to the
# game that are the same as the original game of Chess. As well as a few different rules from the original game of
# Chess. Chess board is displayed using a list of lists.

class Piece:
    """
    Sets up a class for different pieces in chess game, describes the color of the piece and the type of piece
    """
    def __init__(self, color, piece):
        self._color = color
        self._type = piece
        self._represent = "" + color + "" + piece + ""

    def __repr__(self):
        return self._represent

    def get_color(self):
        """
        Returns color of chess piece
        """
        return self._color

    def get_piece(self):
        """
        Returns type of chess piece
        """
        return self._type

########################################################################################################################


# CREATING CHESS PIECES
white_king = Piece("white", "king")
white_rook = Piece("white", "rook")
white_bishop_1 = Piece("white", "bishop_1")
white_bishop_2 = Piece("white", "bishop_2")
white_knight_1 = Piece("white", "knight_1")
white_knight_2 = Piece("white", "knight_2")
black_king = Piece("black", "king")
black_rook = Piece("black", "rook")
black_bishop_1 = Piece("black", "bishop_1")
black_bishop_2 = Piece("black", "bishop_2")
black_knight_1 = Piece("black", "knight_1")
black_knight_2 = Piece("black", "knight_2")

# Creating board as a list of lists
board = [[[white_king], [white_rook], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"]],
         [[white_bishop_1], [white_bishop_2], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"]],
         [[white_knight_1], [white_knight_2], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"]],
         [["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"]],
         [["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"]],
         [[black_knight_1], [black_knight_2], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"]],
         [[black_bishop_1], [black_bishop_2], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"]],
         [[black_king], [black_rook], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"], ["*", None, "*"]]]

empty_space = ["*", None, "*"]

# CONFIGURING X-AXIS
x_Co_Ordinates = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}

# REVERSE X-AXIS VALUES, WILL BE USED TO CONVERT LOCATIONS BACK TO USER INPUT LOCATIONS
reverse_x_Co_Ordinates = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}

# CONFIGURING X-AXIS
y_Co_Ordinates = {"0": 1, "1": 2, "2": 3, "3": 4, "4": 5, "5": 6, "6": 7, "8": 9}


########################################################################################################################


class ChessVar:
    """
    Variation of the game of Chess. Only pieces in this game is a King, Rook, Bishop, and Knight.

    Like ordinary Chess, the pieces behave the same. Captures occur like in ordinary. "white" always goes first.

    Unlike ordinary Chess, to win, a player must make it to Row 8. If "White" makes it to row 8 first, Black has one
    chance to "Tie" the game. Moves that result in any King being in check are not valid.
    """
    def __init__(self):
        self._turn = None
        self._state = "UNFINISHED"
        self._board = board
        self._pieces = ([white_king, white_rook, white_bishop_1, white_bishop_2, white_knight_1, white_knight_2],
                        [black_king, black_rook, black_bishop_1, black_bishop_2, black_knight_1, black_knight_2])
        self._last_row = [self._board[0][7][0], self._board[1][7][0],
                          self._board[2][7][0], self._board[3][7][0],  # Will be used to check if
                          self._board[4][7][0], self._board[5][7][0],  # victories are legitimate
                          self._board[6][7][0], self._board[7][7][0]]

    def board(self):
        """
        Prints Chess board in list of lists format
        """
        print(*self._board[0], sep=" ")
        print()
        print()
        print(*self._board[1], sep=" ")
        print()
        print()
        print(*self._board[2], sep=" ")
        print()
        print()
        print(*self._board[3], sep=" ")
        print()
        print()
        print(*self._board[4], sep=" ")
        print()
        print()
        print(*self._board[5], sep=" ")
        print()
        print()
        print(*self._board[6], sep=" ")
        print()
        print()
        print(*self._board[7], sep=" ")

        return self._board

    def get_pieces(self, color):
        """
        If a player wants to see a list of active pieces they have left, "get_pieces" can display it
        """
        if color == "white":  # fetches white pieces
            print()
            print("White pieces left:")
            print(self._pieces[0])
            return self._pieces[0]
        else:  # else fetches black pieces
            print()
            print("Black pieces left:")
            print(self._pieces[1])
            return self._pieces[1]

    def whose_turn(self):
        """Prints whose turn it is currently"""
        if self._turn is None:
            print()                 # white's turn if no move
            print("WHITE'S TURN")   # has been made yet
        elif self._turn % 2 == 0:   # or, the turn count is even
            print()
            print("WHITE'S TURN")
        else:                       # black's turn only after first
            print()                 # has been made and the
            print("BLACK'S TURN")   # turn count is odd

    def get_turn(self, color):
        """
        Takes one parameter: color. Will be used in move_validation. Will return True if it is the correct player's
        turn and return False otherwise.
        """
        if self._turn is None:
            if color == "white":
                return True
            else:
                return False
        if self._turn is not None:
            if self._turn % 2 == 0:
                if color == "white":
                    return True
                else:
                    return False
            else:
                if color == "white":
                    return False
                else:
                    return True

    def get_game_state(self):
        """
        Takes no parameter. Returns "state" of the game whether it's "UNFINISHED", "WHITE_WON", "BLACK_WON", or "TIE"
        """
        print()
        print("State of the game:")
        print(self._state)
        return self._state

    def update_game(self, update):
        """
        Takes one parameter as a string, Will update the "state" of the game to the parameter whether it's 
        "UNFINISHED", "WHITE_WON", "BLACK_WON", or "TIE". 
        """
        self._state = update
        return self._state

    def remove_piece(self, color, piece):
        """Will take two parameters: color & piece. color & piece will be used to determine the desired contender's
        chess piece and will remove any piece that has been captured form the tuple "pieces". """
        if color == "white":
            self._pieces[0].remove(piece)
            print()
            print("White pieces left:")
            print(self._pieces[0])
        else:
            self._pieces[1].remove(piece)
            print()
            print("Black pieces left:")
            print(self._pieces[1])

    def get_white_king(self):
        for letter in range(0, 8):
            for number in range(0, 8):
                if self._board[letter][number][0] == white_king:
                    letter = reverse_x_Co_Ordinates[letter]
                    number += 1
                    return [letter, number]

    def get_black_king(self):
        for letter in range(0, 8):
            for number in range(0, 8):
                if self._board[letter][number][0] == black_king:
                    letter = reverse_x_Co_Ordinates[letter]
                    number += 1
                    return [letter, number]

    def get_location(self, piece):
        for letter in range(0, 8):
            for number in range(0, 8):
                if self._board[letter][number][0] == piece:
                    letter = reverse_x_Co_Ordinates[letter]
                    number += 1
                    return [letter, number]

    def move_validation(self, color, piece, start, end):
        """
        Will take four parameters: color, piece, start, end. color represents the contender in question.
        piece represents the type of chess piece. start represents the square being moved from. end represents the
        square being moved to. Will validate a legal move by the specific chess piece. Will return True if move is
        valid or raise an Error otherwise.
        """
        if self.get_turn(color) is False:
            print("It is not your Turn.")
            return False
        start_x = start[0]                   # Getting Letter value from 'start' position
        start_y = int(start[1]) - 1          # Getting Number value from 'start' position
        end_x = end[0]                       # Getting Letter value from 'end' position
        end_y = int(end[1]) - 1              # Getting Letter value from 'end' position
        start_x = x_Co_Ordinates[start_x]
        end_x = x_Co_Ordinates[end_x]
        if piece == "king":
            if abs(end_x - start_x) != 0 or 1 or -1:  # King legal
                return False                          # move validation
            if abs(end_y - start_y) != 0 or 1 or -1:
                return False
        elif piece == "rook":                                     # Rook legal move validation
            if (end_x == start_x) and (end_y != start_y):         # if moving Rook vertically
                if end_y > start_y:
                    for space in range(start_y + 1, end_y):
                        if self._board[start_x][space][0] != "*":
                            print("Not a legal move by Rook")
                            print("Rook cannot jump over pieces")
                            return False
                    return True
                elif end_y < start_y:
                    for space in range(end_y + 1, start_y):
                        if self._board[start_x][space][0] != "*":
                            print("Not a legal move by Rook")
                            print("Rook cannot jump over pieces")
                            return False
                    return True
            elif (end_x is not start_x) and (end_y == start_y):   # Rook legal move validation
                if end_x > start_x:                               # if moving Rook horizontally
                    for space in range(start_x + 1, end_x):
                        if self._board[space][end_y][0] != "*":
                            print("Not a legal move by Rook")
                            print("Rook cannot jump over pieces")
                            return False
                elif end_x < start_x:
                    for space in range(end_x + 1, start_x):
                        if self._board[space][end_y][0] != "*":
                            print("Not a legal move by Rook")
                            print("Rook cannot jump over pieces")
                            return False
                else:
                    return True
            else:
                print("Not a legal move by Rook")
                return False
        elif piece != "king" and piece != "rook" and piece != "knight_2" and piece != "knight_1":
            if ((end_x - start_x) > 0) and ((end_y - start_y) > 0):  # Bishop legal
                if (end_x - start_x) == (end_y - start_y):           # move validation
                    for horizontal in range(start_x + 1, end_x):     # if moving in
                        start_y += 1                                 # Upper-Right direction
                        if self._board[horizontal][start_y][0] != "*":
                            print("Not a legal move by Bishop")
                            print("Bishop cannot jump over pieces")
                            return False
                    return True
                else:
                    print("Not a legal move by Bishop")
                    return False

            elif ((end_x - start_x) > 0) and ((end_y - start_y) < 0):  # Bishop legal
                if abs(end_x - start_x) == abs(end_y - start_y):       # move validation
                    for horizontal in range(start_x + 1, end_x):       # if moving in
                        start_y -= 1                                   # Lower-Right direction
                        if self._board[horizontal][start_y][0] != "*":
                            print("Not a legal move by Bishop")
                            print("Bishop cannot jump over pieces")
                    return True
                else:
                    print("Not a legal move by Bishop")
                    return False
            elif ((end_x - start_x) < 0) and ((end_y - start_y) > 0):  # Bishop legal
                if abs(end_x - start_x) == (end_y - start_y):          # move validation
                    for horizontal in range(end_x + 1, start_x):       # if moving in
                        start_y -= 1                                   # Upper-Left direction
                        if self._board[horizontal][start_y][0] != "*":
                            print("Not a legal move by Bishop")
                            print("Bishop cannot jump over pieces")
                    return True
                else:
                    print("Not a legal move by Bishop")
                    return False
            elif ((end_x - start_x) < 0) and ((end_y - start_y) < 0):  # Bishop legal
                if abs(end_x - start_x) == abs(end_y - start_y):       # move validation
                    for horizontal in range(end_x + 1, start_x):       # if moving in
                        start_y += 1                                   # Lower-Left direction
                        if self._board[horizontal][start_y][0] != "*":
                            print("Not a legal move by Bishop")
                            print("Bishop cannot jump over pieces")
                    return True
                else:
                    print("Not a legal move by Bishop")
                    return False
        elif piece == "knight_1" or "knight_2":
            if abs(end_x - start_x) == 1:                            # Knight legal move validation
                if abs(end_y - start_y) == 2:                        # if moving horizontally by 1 spaces
                    return True
                else:
                    print("Not a legal move by Knight")
                    return False
            elif abs(end_x - start_x) == 2:                            # Knight legal move validation
                if abs(end_y - start_y) == 1:                        # if moving horizontally by 2 spaces
                    return True
                else:
                    print("Not a legal move by Knight")
                    return False
            else:                                                    # Can only make a valid move if moving
                print("Not a legal move by Knight")                  # horizontally by 1 or 2 spaces
                return False

    def check_validation(self):
        white_king_location = self.get_white_king()  # fetching the location of white's king on the board
        black_king_location = self.get_black_king()  # fetching the location of black's king on the board
        for piece in self._pieces[1]:
            piece_location = self.get_location(piece)
            if self.move_validation(piece.get_color(), piece.get_piece(), piece_location, white_king_location) is True:
                print(piece)
                print("Move puts White's King in check, move not valid")
                return False
            else:
                return True
        for piece in self._pieces[0]:
            piece_location = self.get_location(piece)
            if self.move_validation(piece.get_color(), piece.get_piece(), piece_location, black_king_location) is True:
                print("Move puts Black's King in check, move not valid")
                return False
            else:
                return True

    def victory(self, color):
        """
        Will take two parameters: color and end. color represents the contender in question. end represents the
        square being moved to. The function will verify at then end of the make_move function if a victory has occurred.
        "turn" will be called to confirm that black does not have an existing turn even after white has made it to
        row: 8. If a true victory has occurred, will return True, otherwise will return False.
        """
        if color == "black":
            if white_king not in self._last_row:
                self.update_game("BLACK_WON")
                print(self._state)
                return True
            else:
                self.update_game("TIE")
                print(self._state)
                return True
        elif color == "go_ahead":
            self.update_game("WHITE_WON")
            print(self._state)
            return True

    def make_move(self, start, end):
        """
        A method called make_move that takes two parameters - strings that represent the square moved from and the
        square moved to. For example, make_move('b3', 'c4'). If the square being moved from does not contain a piece
        belonging to the player whose turn it is, or if the indicated move is not legal, or if the game has already
        been won, then it should just return False. Otherwise, it should make the indicated move, remove any captured
         piece, update the game state if necessary, update whose turn it is, and return True.
        """
        if self._state != "UNFINISHED":  # Checking state of the game before allowing move
            print("Game is already finished, no additional moves are allowed.")
            return False
        start_x = start[0]                  # Getting Letter value from 'start' position
        start_y = int(start[1]) - 1              # Getting Number value from 'start' position
        end_x = end[0]                      # Getting Letter value from 'end' position
        end_y = int(end[1]) - 1                  # Getting Letter value from 'end' position
        start_x = x_Co_Ordinates[start_x]
        end_x = x_Co_Ordinates[end_x]
        if None in self._board[start_x][start_y]:    # Checking if there is a piece in start position
            print("No piece was chosen to move.")
            return False
        your_piece = self._board[start_x][start_y][0]
        your_piece_color = your_piece.get_color()
        your_piece_type = your_piece.get_piece()
        if self.get_turn(your_piece_color) is not True:   # Checking if it is the right user's turn
            print("Not " + your_piece_color + "'s turn")
            return False
        if self.move_validation(your_piece_color, your_piece_type, start, end) is not True:  # Checking if correct
            print("Your " + your_piece_type + " is not attempting a valid move")             # piece movement is valid
            return False
        if None not in self._board[end_x][end_y]:               # If end position is
            opponent_piece = self._board[end_x][end_y][0]       # occupied by own piece
            opponent_piece_color = opponent_piece.get_color()   # move is not valid
            if your_piece_color == opponent_piece_color:
                print("Cannot capture your own piece")
                return False
            else:

                switch_a = self._board[start_x][start_y]
                switch_b = empty_space
                self._board[start_x][start_y] = switch_b
                self._board[end_x][end_y] = switch_a
                if self._turn is None:
                    self._turn = 1
                else:
                    self._turn += 1
                self.remove_piece(opponent_piece_color, opponent_piece)

        if None in self._board[end_x][end_y]:           # If designated end position is empty
            switch_a = self._board[start_x][start_y]    # end position becomes occupied with your_piece
            switch_b = self._board[end_x][end_y]        # start position becomes occupied with an empty space
            self._board[start_x][start_y] = switch_b
            self._board[end_x][end_y] = switch_a
            if self._turn is None:
                self._turn = 1
            else:
                self._turn += 1
        if self.check_validation() is False:           # Switches pieces back to pre-move positions if check validation
            switch_a = self._board[start_x][start_y]   # does not return True
            switch_b = self._board[end_x][end_y]
            self._board[start_x][start_y] = switch_b
            self._board[end_x][end_y] = switch_a
            print("Move puts a king in check")
            return False
        if end_y != 7:
            if your_piece_color == "black":
                last_row = [self._board[0][7][0], self._board[1][7][0],
                            self._board[2][7][0], self._board[3][7][0],
                            self._board[4][7][0], self._board[5][7][0],
                            self._board[6][7][0], self._board[7][7][0]]
                if white_king in last_row:
                    return self.victory("go_ahead")
        if end_y == 7:
            last_row = [self._board[0][7][0], self._board[1][7][0],
                        self._board[2][7][0], self._board[3][7][0],
                        self._board[4][7][0], self._board[5][7][0],
                        self._board[6][7][0], self._board[7][7][0]]
            if (your_piece_color == "black") and (white_king not in last_row):
                return self.victory("black")
