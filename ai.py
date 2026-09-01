import random


def winning_move(board, player):
    for move in available_moves(board):
        board[move] = player
        won = check_winner(board) == player
        board[move] = " "
        if won:
            return move
    return None


def available_moves(board):
    return [i for i, cell in enumerate(board) if cell == " "]


def check_winner(board):
    winning_lines = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )

    for a, b, c in winning_lines:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]

    return None


def minimax(board, maximizing_player, ai_player, human_player, alpha, beta):
    winner = check_winner(board)

    if winner == ai_player:
        return 10
    if winner == human_player:
        return -10
    if not available_moves(board):
        return 0

    if maximizing_player:
        best_score = float("-inf")

        for move in available_moves(board):
            board[move] = ai_player
            score = minimax(
                board, False, ai_player, human_player, alpha, beta
            )
            board[move] = " "

            best_score = max(best_score, score)
            alpha = max(alpha, best_score)

            if beta <= alpha:
                break

        return best_score

    best_score = float("inf")

    for move in available_moves(board):
        board[move] = human_player
        score = minimax(
            board, True, ai_player, human_player, alpha, beta
        )
        board[move] = " "

        best_score = min(best_score, score)
        beta = min(beta, best_score)

        if beta <= alpha:
            break

    return best_score


def best_move(board, ai_player, human_player):
    best_score = float("-inf")
    move_choice = None

    # Try center/corners first for more natural play.
    move_order = [4, 0, 2, 6, 8, 1, 3, 5, 7]

    for move in move_order:
        if board[move] != " ":
            continue

        board[move] = ai_player
        score = minimax(
            board,
            False,
            ai_player,
            human_player,
            float("-inf"),
            float("inf"),
        )
        board[move] = " "

        if score > best_score:
            best_score = score
            move_choice = move

    return move_choice


def get_ai_move(board, ai_player, difficulty, human_player):
    moves = available_moves(board)

    if not moves:
        return None

    if difficulty == "easy":
        return random.choice(moves)

    if difficulty == "medium":
        # Always take an immediate win.
        move = winning_move(board, ai_player)
        if move is not None:
            return move

        # Always block an immediate loss.
        move = winning_move(board, human_player)
        if move is not None:
            return move

        # Otherwise use strategy most of the time.
        if random.random() < 0.65:
            return best_move(board, ai_player, human_player)

        return random.choice(moves)

    return best_move(board, ai_player, human_player)
