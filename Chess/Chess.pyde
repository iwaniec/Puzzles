class Piece:
    def __init__(self, team, type, position, image):
        self.team = team
        self.type = type
        self.image = image
        self.position = position

# Initialize black team
# --------------------------------------------------
bk =  Piece('b', 'k', 'e8', 'black_king.png')
bq =  Piece('b', 'q', 'd8', 'black_queen.png')
bb1 = Piece('b', 'b', 'c8', 'black_bishop.png')
bb2 = Piece('b', 'b', 'f8', 'black_bishop.png')
bn1 = Piece('b', 'n', 'b8', 'black_knight.png')
bn2 = Piece('b', 'n', 'g8', 'black_knight.png')
br1 = Piece('b', 'r', 'a8', 'black_rook.png')
br2 = Piece('b', 'r', 'h8', 'black_rook.png')
bp1 = Piece('b', 'p', 'a7', 'black_pawn.png')
bp2 = Piece('b', 'p', 'b7', 'black_pawn.png')
bp3 = Piece('b', 'p', 'c7', 'black_pawn.png')
bp4 = Piece('b', 'p', 'd7', 'black_pawn.png')
bp5 = Piece('b', 'p', 'e7', 'black_pawn.png')
bp6 = Piece('b', 'p', 'f7', 'black_pawn.png')
bp7 = Piece('b', 'p', 'g7', 'black_pawn.png')
bp8 = Piece('b', 'p', 'h7', 'black_pawn.png')
black_team = [bk, bq, bb1, bb2, bn1, bn2, br1, br2, bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8]

# Initialize white team
# --------------------------------------------------
wk =  Piece('w', 'k', 'e1', 'white_king.png')
wq =  Piece('w', 'q', 'd1', 'white_queen.png')
wb1 = Piece('w', 'b', 'c1', 'white_bishop.png')
wb2 = Piece('w', 'b', 'f1', 'white_bishop.png')
wn1 = Piece('w', 'n', 'b1', 'white_knight.png')
wn2 = Piece('w', 'n', 'g1', 'white_knight.png')
wr1 = Piece('w', 'r', 'a1', 'white_rook.png')
wr2 = Piece('w', 'r', 'h1', 'white_rook.png')
wp1 = Piece('w', 'p', 'a2', 'white_pawn.png')
wp2 = Piece('w', 'p', 'b2', 'white_pawn.png')
wp3 = Piece('w', 'p', 'c2', 'white_pawn.png')
wp4 = Piece('w', 'p', 'd2', 'white_pawn.png')
wp5 = Piece('w', 'p', 'e2', 'white_pawn.png')
wp6 = Piece('w', 'p', 'f2', 'white_pawn.png')
wp7 = Piece('w', 'p', 'g2', 'white_pawn.png')
wp8 = Piece('w', 'p', 'h2', 'white_pawn.png')
white_team = [wk, wq, wb1, wb2, wn1, wn2, wr1, wr2, wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8]

# find pixel position given chess position
# --------------------------------------------------
def pos2px(position):

    files = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
    file = position[0]
    file_pos = (files[file]-1)*100

    rank = position[1]    
    rank_pos = (8-int(rank))*100
    
    return file_pos, rank_pos # x, y from the top left corner

# find chess position given position position
# --------------------------------------------------
def px2pos(x, y):
    
    files = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h'}
    file = files[x//100+1]
    
    rank = str( (8-y/100) )
    return file+rank

# find piece at chess position
# --------------------------------------------------
def find_piece(position):
    for piece in white_team:
        if piece.position == position:
            return piece
    for piece in black_team:
        if piece.position == position:
            return piece
    else:
        print('No Piece at this Location!')
        return False

             
# --------------------------------------------------
# Setup and Draw Chess Board
# --------------------------------------------------
                                                                        
def setup():
    
    # size and background of board
    size(800, 800)
    background(177, 110, 65)
    
     
    # set to light square fill color and no stroke
    fill(255, 213, 153)
    noStroke()
    
    # draw the light squares
    for i in range(8):       # file
        for j in range(4):   # rank
            file = i*100
            rank = (j*200+i%2*100)
            rect(file, rank, 100, 100)

def draw():
    for piece in white_team:
        x, y = pos2px(piece.position)
        image(loadImage(piece.image), x, y-5)
        
    for piece in black_team:
        x, y = pos2px(piece.position)
        image(loadImage(piece.image), x, y-5)
        
# --------------------------------------------------
# Actions on Mouse Click
# --------------------------------------------------
               
def mouseClicked():
    mouse_piece = find_piece(px2pos(mouseX, mouseY))
    if mouse_piece:
        print(mouse_piece.team + mouse_piece.type)
    
