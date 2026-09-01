from game import TicTacToe
from ai import get_ai_move


def choose_difficulty():
    print("\nChoose difficulty:")
    print("1. Easy   - AI makes random moves sometimes")
    print("2. Medium - AI mixes strategy and randomness")
    print("3. Hard   - Unbeatable Minimax + Alpha-Beta")

    while True:
        choice = input("Enter choice (1/2/3): ").strip()
        if choice in {"1", "2", "3"}:
            return {"1": "easy", "2": "medium", "3": "hard"}[choice]
        print("Invalid choice. Please enter 1, 2, or 3.")


def choose_player():
    while True:
        symbol = input("\nChoose your symbol (X/O): ").strip().upper()
        if symbol in {"X", "O"}:
            return symbol
        print("Please enter X or O.")


def play_game():
    human = choose_player()
    ai_player = "O" if human == "X" else "X"
    difficulty = choose_difficulty()

    game = TicTacToe(human, ai_player)

    print("\nYou are", human)
    print("AI is", ai_player)
    print("Difficulty:", difficulty)

    while not game.is_game_over():
        game.print_board()

        if game.current_player == human:
            game.human_move()
        else:
            print("\nAI is thinking...")
            move = get_ai_move(
                game.board,
                ai_player,
                difficulty,
                human,
            )
            game.make_move(move, ai_player)

    game.print_board()
    result = game.result()

    if result == "draw":
        print("\nIt's a draw!")
    elif result == human:
        print("\nCongratulations! You won!")
    else:
        print("\nAI wins. Better luck next time!")


def main():
    print("=" * 40)
    print("        TIC-TAC-TOE AI")
    print("=" * 40)

    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
