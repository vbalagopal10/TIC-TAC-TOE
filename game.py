class TicTacToe:
    WINNING_LINES = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )

    def __init__(self, human="X", ai="O"):
        self.board = [" "] * 9
        self.human = human
        self.ai = ai
        self.current_player = "X"

    def print_board(self):
        display = [
            value if value != " " else str(index + 1)
            for index, value in enumerate(self.board)
        ]

        print()
        print(f" {display[0]} | {display[1]} | {display[2]}")
        print("---+---+---")
        print(f" {display[3]} | {display[4]} | {display[5]}")
        print("---+---+---")
        print(f" {display[6]} | {display[7]} | {display[8]}")

    def available_moves(self):
        return [i for i, cell in enumerate(self.board) if cell == " "]

    def make_move(self, position, player):
        if position not in self.available_moves():
            return False

        self.board[position] = player
        self.current_player = "O" if player == "X" else "X"
        return True

    def human_move(self):
        while True:
            try:
                position = int(input("\nEnter position (1-9): ")) - 1
                if position not in range(9):
                    raise ValueError
                if self.make_move(position, self.human):
                    return
                print("That position is already occupied.")
            except ValueError:
                print("Please enter a number from 1 to 9.")

    def winner(self):
        for a, b, c in self.WINNING_LINES:
            if (
                self.board[a] != " "
                and self.board[a] == self.board[b] == self.board[c]
            ):
                return self.board[a]
        return None

    def is_draw(self):
        return self.winner() is None and not self.available_moves()

    def is_game_over(self):
        return self.winner() is not None or self.is_draw()

    def result(self):
        return self.winner() or "draw"
