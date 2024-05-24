class Bitboard:
    def __init__(self, number: int):
        self.board = number

    def set_bit(self, index: int):
        self.board |= 1 << index

    def clear_bit(self, index: int):
        self.board &= ~(1 << index)

    def get_bit(self, index: int) -> bool:
        return (self.board >> index) & 1 == 1
    
    def __str__(self):
        board_str = ''
        for row in range(7, -1, -1): 
            for col in range(8): 
                index = row * 8 + col
                board_str += "1" if self.get_bit(index) else "0"
            board_str += '\n'
        return board_str
    
    def populate_up(self, index: int, steps: int, block_mask: 'Bitboard'):
        current_index = index
        for _ in range(steps):
            if is_upper_border(current_index):
                return
            current_index += 8
            self.set_bit(current_index)
            if block_mask.get_bit(current_index):
                return

    def populate_down(self, index: int, steps: int, block_mask: 'Bitboard'):
        current_index = index
        for _ in range(steps):
            if is_lower_border(current_index):
                return
            current_index -= 8
            self.set_bit(current_index)
            if block_mask.get_bit(current_index):
                return

    def populate_right(self, index: int, steps: int, block_mask: 'Bitboard'):
        current_index = index
        for _ in range(steps):
            if is_right_border(current_index):
                return
            current_index += 1
            self.set_bit(current_index)
            if block_mask.get_bit(current_index):
                return

    def populate_left(self, index: int, steps: int, block_mask: 'Bitboard'):
        current_index = index
        for _ in range(steps):
            if is_left_border(current_index):
                return
            current_index -= 1
            self.set_bit(current_index)
            if block_mask.get_bit(current_index):
                return

    def populate_up_right(self, index: int, steps: int, block_mask: 'Bitboard'):
        current_index = index
        for _ in range(steps):
            if is_upper_border(current_index) or is_right_border(current_index):
                return
            current_index += 9
            self.set_bit(current_index)
            if block_mask.get_bit(current_index):
                return

    def populate_up_left(self, index: int, steps: int, block_mask: 'Bitboard'):
        current_index = index
        for _ in range(steps):
            if is_upper_border(current_index) or is_left_border(current_index):
                return
            current_index += 7
            self.set_bit(current_index)
            if block_mask.get_bit(current_index):
                return

    def populate_down_right(self, index: int, steps: int, block_mask: 'Bitboard'):
        current_index = index
        for _ in range(steps):
            if is_lower_border(current_index) or is_right_border(current_index):
                return
            current_index -= 7
            self.set_bit(current_index)
            if block_mask.get_bit(current_index):
                return

    def populate_down_left(self, index: int, steps: int, block_mask: 'Bitboard'):
        current_index = index
        for _ in range(steps):
            if is_lower_border(current_index) or is_left_border(current_index):
                return
            current_index -= 9
            self.set_bit(current_index)
            if block_mask.get_bit(current_index):
                return

    def populate_hor_vert(self, index: int, steps: int, block_mask: 'Bitboard'):
        self.populate_up(index=index, steps=steps, block_mask=block_mask)
        self.populate_down(index=index, steps=steps, block_mask=block_mask)
        self.populate_left(index=index, steps=steps, block_mask=block_mask)
        self.populate_right(index=index, steps=steps, block_mask=block_mask)

    def populate_diag(self, index: int, steps: int, block_mask: 'Bitboard'):
        self.populate_up_left(index=index, steps=steps, block_mask=block_mask)
        self.populate_up_right(index=index, steps=steps, block_mask=block_mask)
        self.populate_down_left(index=index, steps=steps, block_mask=block_mask)
        self.populate_down_right(index=index, steps=steps, block_mask=block_mask)

def is_right_border(index: int) -> bool:
    return index % 8 == 7

def is_left_border(index: int) -> bool:
    return index % 8 == 0

def is_upper_border(index: int) -> bool:
    return index > 55

def is_lower_border(index: int) -> bool:
    return index < 8