from src.bitboard import Bitboard

test = Bitboard(0)
block_mask = Bitboard(0)

block_mask.set_bit(9)
block_mask.set_bit(43)

test.populate_diag(27, 8, block_mask)
test.populate_hor_vert(27, 8, block_mask)

print(str(test))