from enum import Enum
from src.bitboard import Bitboard
from src.color import Color

class Piece(Enum):
    PAWN = "PAWN"
    KNIGHT = "KNIGHT"
    BISHOP = "BISHOP"
    ROOK = "ROOK"
    QUEEN = "QUEEN"
    KING = "KING"

    def get_reach_mask(self, index: int, color: Color, block_mask: Bitboard) -> Bitboard:
        board = Bitboard(0)
        match self:
            case Piece.PAWN:
                on_white_pawn_line = index > 7 and index < 16
                on_black_pawn_line = index > 47 and index < 56
                
                if color == Color.WHITE:
                    steps = 2 if on_white_pawn_line else 1
                    board.populate_up(index=index, steps=steps, block_mask=block_mask)
                else:
                    steps = 2 if on_black_pawn_line else 1
                    board.populate_down(index=index, steps=steps, block_mask=block_mask)

        return board