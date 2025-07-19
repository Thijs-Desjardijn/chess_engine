import chess
import random
import chess.polyglot
import pygame 


PAWN_PST = [
     0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
     0.5,  0.5,  0.5,  0.5,  0.5,  0.5,  0.5,  0.5,
     0.1,  0.1,  0.1,  0.3,  0.3,  0.1,  0.1,  0.1,
     0.05, 0.05, 0.2,  0.5, 0.5,   0.2,  0.0, 0.0,
     0.0,  0.0,  0.0,  0.3,  0.3,  0.0,  0.0,  0.0,
     0.05, 0.0,   0.0,  0.0,  0.0,  0.0,  0.0,  0.05,
     0.05, 0.1,  0.1,  0.0,  0.0,  0.1,  0.1,  0.05,
     0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0
]

KNIGHT_PST = [
   -0.5, -0.4, -0.3, -0.3, -0.3, -0.3, -0.4, -0.5,
   -0.4, -0.2,  0.0,  0.0,  0.0,  0.0, -0.2, -0.4,
   -0.3,  0.0,  0.1,  0.15, 0.15, 0.1,  0.0, -0.3,
   -0.3,  0.05, 0.15, 0.2,  0.2,  0.15, 0.05, -0.3,
   -0.3,  0.0,  0.15, 0.2,  0.2,  0.15, 0.0,  -0.3,
   -0.3,  0.05, 0.1,  0.15, 0.15, 0.1,  0.05, -0.3,
   -0.4, -0.2,  0.0,  0.05, 0.05, 0.0,  -0.2, -0.4,
   -0.5, -0.4, -0.3, -0.3, -0.3, -0.3, -0.4, -0.5
]

BISHOP_PST = [
   -0.2, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.2,
   -0.1,  0.2,  0.0,  0.0,  0.0,  0.0,  0.15, -0.1,
   -0.1,  0.0,  0.05, 0.1,  0.1,  0.05, 0.0, -0.1,
   -0.1,  0.05, 0.05, 0.1,  0.1,  0.05, 0.05, -0.1,
   -0.1,  0.0,  0.1,  0.1,  0.1,  0.1,  0.0, -0.1,
   -0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1, -0.1,
   -0.1,  0.05, 0.0,  0.0,  0.0,  0.0,  0.05, -0.1,
   -0.2, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.2
]

ROOK_PST = [
     0.0,  0.0,  0.0,  0.05, 0.05, 0.0,  0.0,  0.0,
   -0.05,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.05,
   -0.05,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.05,
   -0.05,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.05,
   -0.05,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.05,
   -0.05,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.05,
     0.05, 0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.05,
     0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0
]

QUEEN_PST = [
   -0.2, -0.1, -0.1, -0.05, -0.05, -0.1, -0.1, -0.2,
   -0.1,  0.0,  0.0,   0.0,   0.0,  0.0,  0.0, -0.1,
   -0.1,  0.0,  0.05,  0.05,  0.05, 0.05,  0.0, -0.1,
   -0.05, 0.0,  0.05,  0.05,  0.05, 0.05,  0.0, -0.05,
    0.0,   0.0,  0.05,  0.05,  0.05, 0.05,  0.0, -0.05,
   -0.1,  0.05, 0.05,  0.05,  0.05, 0.05,  0.0, -0.1,
   -0.1,  0.0,  0.05,  0.0,   0.0,  0.0,  0.0, -0.1,
   -0.2, -0.1, -0.1, -0.05, -0.05, -0.1, -0.1, -0.2
]

KING_PST = [
    0.2,  0.3,  0.2,  0.0,  0.0,  0.1,  0.3,  0.2,
    0.2,  0.2,  0.0,  0.0,  0.0,  0.0,  0.2,  0.2,
   -0.1, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.1,
   -0.2, -0.3, -0.3, -0.4, -0.4, -0.3, -0.3, -0.2,
   -0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3,
   -0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3,
   -0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3,
   -0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3
]
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

def mirror_pst(pst):
    #mirror for piece square table
    return sum([pst[i*8:(i+1)*8] for i in reversed(range(8))], [])

def sort_moves(board):
    moves = list(board.legal_moves)
    scored_moves = []

    for move in moves:
        board.push(move)

        score = 0
        if board.is_check():
            score += 0.5
        if board.is_capture(move):
            score += 1
        if move in board.generate_castling_moves():
            score += 0.3

        board.pop()
        scored_moves.append((score, move))

    scored_moves.sort(reverse=True, key=lambda x: x[0])
    return [move for score, move in scored_moves]

def get_book_move(board, book_path):
    try:
        with chess.polyglot.open_reader(book_path) as reader:
            entries = list(reader.find_all(board))
            if entries:
                # Pick one move randomly from book entries
                entry = random.choice(entries)
                return entry.move
            else:
                return None
    except Exception as e:
        print(f"Error opening book: {e}")
        return None


def evaluate_position(board):
    if board.is_checkmate():
        return 1000 if board.turn == chess.WHITE else -1000
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

        if piece.piece_type == chess.KNIGHT:
            if chess.WHITE:
                score += KNIGHT_PST[square]
            else:
                score -= mirror_pst(KNIGHT_PST)[square]

        if piece.piece_type == chess.KING:
            if chess.WHITE:
                score += KING_PST[square]
            else:
                score -= mirror_pst(KING_PST)[square]

        if piece.piece_type == chess.BISHOP:
            if chess.WHITE:
                score += BISHOP_PST[square]
            else:
                score -= mirror_pst(BISHOP_PST)[square]

        if piece.piece_type == chess.ROOK:
            if chess.WHITE:
                score += ROOK_PST[square]
            else:
                score -= mirror_pst(ROOK_PST)[square]

        if piece.piece_type == chess.PAWN:
            if chess.WHITE:
                score += PAWN_PST[square]
            else:
                score -= mirror_pst(PAWN_PST)[square]

        if piece.piece_type == chess.QUEEN:
            if chess.WHITE:
                score += QUEEN_PST[square]
            else:
                score -= mirror_pst(QUEEN_PST)[square]

        # Penalize hanging pieces
        attackers = board.attackers(not piece.color, square)
        defenders = board.attackers(piece.color, square)
        if attackers and not defenders:
            penalty = value * 0.7
            score -= penalty if piece.color == chess.WHITE else +penalty
        penalty = 0
        attacker_dangerous = 0
        if attackers and defenders:
            for attacker_square in attackers:
                attackers_piece = board.piece_at(attacker_square)
                attacker_value = piece_values[attackers_piece.piece_type]
                if value > attacker_value:
                    penalty += (value - attacker_value) * 0.7
                    attacker_dangerous += 1
            if penalty:
                penalty = penalty/ attacker_dangerous
                score -= penalty if piece.color == chess.WHITE else +penalty
    # Mobility bonus
    mobility = len(list(board.legal_moves))
    score += 0.005 * mobility if board.turn == chess.WHITE else -0.005 * mobility

    if board.is_check():
        score += 0.1 if board.turn == chess.WHITE else -0.1

    return score if board.turn == chess.WHITE else -score


def alphabeta(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_position(board)

    if maximizing_player:
        max_eval = float('-inf')
        for move in sort_moves(board):
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
        for move in sort_moves(board):
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

    for move in board.legal_moves():
        board.push(move)
        move_value = alphabeta(board, depth - 1, alpha, beta, False)
        board.pop()
        if move_value > best_value:
            best_value = move_value
            best_move = move
        alpha = max(alpha, best_value)
    return best_move


def main():
    pygame.init()
    board = chess.Board()
    print(board)
    book_path = "Cerebellum3Merge.bin"
    while not board.is_game_over():
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
        engine_move = get_book_move(board, book_path)
        if engine_move is None:
            engine_move = get_best_move(board, 4)
        print(f"Engine plays: {engine_move}")
        board.push(engine_move)
        print(board)
        print(f"Eval: {evaluate_position(board)}")

        if board.is_game_over():
            break
    print(board)
    print("Game over:", board.result())


if __name__ == "__main__":
    main()