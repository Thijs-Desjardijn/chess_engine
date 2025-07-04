import chess
import random
from book_moves import popular_openings

# === Piece values ===
piece_values = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0
}

# === Positional heuristics ===
center_squares = [chess.D4, chess.D5, chess.E4, chess.E5]
development_squares = [
    chess.C3, chess.C4, chess.C5, chess.C6,
    chess.D3, chess.D4, chess.D5, chess.D6,
    chess.E3, chess.E4, chess.E5, chess.E6,
    chess.F3, chess.F4, chess.F5, chess.F6
]
starting_squares_white = [chess.A1, chess.B1, chess.C1, chess.D1, chess.E1, chess.F1, chess.G1, chess.H1]
starting_squares_black = [chess.A8, chess.B8, chess.C8, chess.D8, chess.E8, chess.F8, chess.G8, chess.H8]
flank_pawn_squares_white = [chess.A2, chess.B2, chess.G2, chess.H2]
flank_pawn_squares_black = [chess.A7, chess.B7, chess.G7, chess.H7]

def get_book_move_from_board(board, opening_book):
    """
    Given a python-chess Board, try to find the next book move from opening_book.
    Return a chess.Move if found, else None.
    """
    move_history = [move.uci() for move in board.move_stack]

    current_level = opening_book
    for move in move_history:
        if move in current_level:
            current_level = current_level[move]
            if 'responses' in current_level:
                current_level = current_level['responses']
            elif 'next_moves' in current_level:
                current_level = current_level['next_moves']
            else:
                # End of book line reached
                return None
        else:
            return None
    if isinstance(current_level, dict) and current_level:
        # Pick first available move (can randomize if desired)
        next_uci = random.choice(list(current_level.keys()))
        try:
            return chess.Move.from_uci(next_uci)
        except:
            return None
    return None


def evaluate_position(board):
    if board.is_checkmate():
        return -1000 if board.turn == chess.WHITE else 1000
    if board.is_stalemate():
        return 0

    score = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if not piece:
            continue

        value = piece_values[piece.piece_type]

        if piece.color == chess.WHITE:
            score += value
        else:
            score -= value

        # Development for minor pieces
        if piece.piece_type in [chess.KNIGHT, chess.BISHOP]:
            if square in development_squares and board.fullmove_number < 15:
                score += 0.05 if piece.color == chess.WHITE else -0.05
            elif board.fullmove_number < 30:
                if piece.color == chess.WHITE and square in starting_squares_white:
                    score -= 0.05
                elif piece.color == chess.BLACK and square in starting_squares_black:
                    score += 0.05

        # Center pawns
        if piece.piece_type == chess.PAWN:
            if square in center_squares:
                score += 0.2 if piece.color == chess.WHITE else -0.2
            if board.fullmove_number < 20:
                if square in flank_pawn_squares_white and piece.color == chess.WHITE:
                    score += 0.3
                elif square in flank_pawn_squares_black and piece.color == chess.BLACK:
                    score -= 0.3

        # Penalize hanging pieces
        attackers = board.attackers(not piece.color, square)
        defenders = board.attackers(piece.color, square)
        if attackers and not defenders:
            penalty = value * 1.5
            score -= penalty if piece.color == chess.WHITE else +penalty
        penalty = 0
        attacker_dangerous = 0
        if attackers and defenders:
            for attacker_square in attackers:
                attackers_piece = board.piece_at(attacker_square)
                attacker_value = piece_values[attackers_piece.piece_type]
                if value < attacker_value:
                    penalty += (value - attacker_value) * 1.5
                    attacker_dangerous += 1
            if penalty:
                penalty = penalty/ attacker_dangerous
                score -= penalty if piece.color == chess.WHITE else +penalty

    # Mobility bonus
    mobility = len(list(board.legal_moves))
    score += 0.02 * mobility if board.turn == chess.WHITE else -0.02 * mobility

    #if board.is_check():
    #    score += 0.1 if board.turn == chess.WHITE else -0.1

    return score if board.turn == chess.WHITE else -score


def alphabeta(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_position(board)

    if maximizing_player:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval_score = alphabeta(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval_score = alphabeta(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval


def get_best_move(board, depth):
    best_move = None
    best_value = float('-inf')
    alpha = float('-inf')
    beta = float('inf')

    for move in board.legal_moves:
        board.push(move)
        move_value = alphabeta(board, depth - 1, alpha, beta, False)
        board.pop()
        if move_value > best_value:
            best_value = move_value
            best_move = move
        alpha = max(alpha, best_value)
    return best_move


def main():
    board = chess.Board()
    while not board.is_game_over():
        print(board)

        valid_move = False
        while not valid_move:
            move_input = input("Your move (UCI): ")
            try:
                move = chess.Move.from_uci(move_input)
                if move in board.legal_moves:
                    board.push(move)
                    valid_move = True
                else:
                    print("Illegal move! Format example: e2e4 or e7e8q")
            except:
                print("Invalid input! Format example: e2e4 or e7e8q")
        engine_move = get_book_move_from_board(board, popular_openings)
        if engine_move is None:
            engine_move = get_best_move(board, 4)
        print(f"Engine plays: {engine_move}")
        board.push(engine_move)
        print(f"Eval: {evaluate_position(board)}")

        if board.is_game_over():
            break
    print(board)
    print("Game over:", board.result())


if __name__ == "__main__":
    main()