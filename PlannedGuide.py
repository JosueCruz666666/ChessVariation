class Piece:
    """
    A class that will represent a chess piece describing the color and the type of piece. This class will be used
in class ChessVar
"""

    def __init__(self, color, piece):
        """
        Will take two parameters: color and piece, will allow for identifying a certain piece and color in
        class ChessVar to determine who’s turn it is and if a certain move is allowed based on the piece and it’s
        capabilities.
        """
        pass

    def get_color(self):
        """
        Will take in no parameters, will return the color of the Chess piece to allow for determining who's turn
        it is.
        """
        pass

    def get_piece(self):
        """
        Will take in no parameters, will return the type of chess piece to allow for determining if a move is
        valid. Will also help in determining if the King is in check or not.
        """
        pass


"""
Section will be used to build Chess pieces using class Piece. These pieces will then be used in class ChessVar.
"""

"""
    Section will be used to create a board using a dictionary. Individual squares on the chess board will be the keys.
Empty squares will be represented as None for the value, while non-emtpy squares will be represented by a Piece(object)
The dictionary will created with the starting positions of both opponents.
    A dictionary will be tested first, a list of lists may be an alternative option later on.
"""


class ChessVar:
    """
    Class that will represent the game-play of Chess. White always goes first. Moves will be validated whether
    it's the right opponents turn or if the piece makes a legal move. State of the game will be returned. Illegal
    checking of the king will be denied. Validation of win will be determined.
    """

    def __init__(self):
        """
        Initializer function will take no parameters.
        Private data members:
            "turn" will be initialized to None.
            "state" will be initialized to an empty string
            "board" will be initialized to the dictionary "board".
            "pieces" will be initialized to a tuple of two empty lists
        """
        pass

    def get_board(self):
        """
        Takes no parameter. Prints the dictionary board in a horizontal board-like visualization of a chess game.
        """
        pass

    def get_turn(self):
        """
        Takes no parameter. Will check turn and if turn == None, function will return "WHITE'S TURN" and set turn = 1.
        Integers will increment to keep track of whose turn it is. If "turn" is an odd number, this means that white
        made the last move, so should then return "BLACK'S TURN". If "turn: is an even number, this means that black
        made the last move, so should then return "WHITE'S TURN". get_turn will also be used to determine the case in
        white has a true victory if white so happens to make it to row 8.
        """
        pass

    def get_game_state(self):
        """
        Takes no parameter. Returns "state" of the game whether it's "UNFINISHED", "WHITE_WON", "BLACK_WON", or "TIE"
        """
        pass

    def update_game(self, update):
        """
        Takes one parameter as a string, Will update the "state" of the game to the parameter whether it's 
        "UNFINISHED", "WHITE_WON", "BLACK_WON", or "TIE". 
        """
        pass

    def get_pieces(self, color):
        """
        Takes one parameter: color. color will be used to determine the desired opponent. get_pieces will return the
        active pieces left of the user by calling the tuple "pieces" of the corresponding color.
        """
        pass

    def remove_piece(self, color, piece):
        """Will take two parameters: color & piece. color & piece will be used to determine the desired contender's
        chess piece and will remove any piece that has been captured form the tuple "pieces". """
        pass

    def make_move(self, start, end):
        """
        Takes two parameters - strings that represent the square of the piece decided to be moved from and the desired
        square to move said piece to. Will check if it's the correct contender's turn. Will check if piece made a legal
        movement. Will update the "board" dictionary to display the updated board after the legal move. If legal move,
        and opponent's chess piece is in new square, the piece will be captured and removed from the opponent's list in
        "pieces" tuple. Will also increment "turn" and update state of game.
        """
        pass

    def move_validation(self, color, piece, start, end):
        """
        Will take four parameters: color, piece, start, end. color represents the contender in question.
        piece represents the type of chess piece. start represents the square being moved from. end represents the
        square being moved to. Will validate a legal move by the specific chess piece. Will return True if move is
        valid or raise an Error otherwise.
        """
        pass

    def check_validation(self, color, piece, start, end):
        """
        Will take four parameters: color, piece, start, end. color represents the contender in question.
        piece represents the type of chess piece. start represents the square being moved from. end represents the
        square being moved to. Will only validate if move does not put any of the opponents' kings in check.
        Will return True if move passes check_validation or raise an Error otherwise.
        """
        pass

    def victory(self, color, end):
        """
        Will take three parameters: color, start, end. color represents the contender in question. end represents the
        square being moved to. The function will verify at then end of the make_move function if a victory has occurred.
        "turn" will be called to confirm that black does not have an existing turn even after white has made it to
        row: 8. If a true victory has occurred, will return True, otherwise will return False.
        """
        pass

