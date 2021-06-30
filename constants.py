from pygame import image
from screeninfo import get_monitors

main = get_monitors()[0]
for m in get_monitors()[1:]:
    if m.width > main.width:
        main = m

# Colors
BLACK = 0, 0, 0
WHITE = 255, 255, 255
LIGHTBEIGE = 181, 136, 99
BROWN = 240, 217, 181
GREEN = 63, 123, 82
ORANGE = 253, 189, 89
RED = 250, 41, 76
GREY = 185, 199, 185

BG_COLOR = BLACK
CASECOLOR1 = BROWN
CASECOLOR2 = LIGHTBEIGE

# Sizes
WIDTH, HEIGHT = main.width, main.height
MIDW = WIDTH // 2
MIDH = HEIGHT // 2
BOARDSIZE = HEIGHT * 0.8
BOARDTOPLEFTPOS = (MIDW - BOARDSIZE // 2, MIDH - BOARDSIZE // 2)

# Pieces

P_image = image.load(r"assets/row-1-col-6.png")  # white
R_image = image.load(r"assets/row-1-col-5.png")
N_image = image.load(r"assets/row-1-col-4.png")
B_image = image.load(r"assets/row-1-col-3.png")
Q_image = image.load(r"assets/row-1-col-2.png")
K_image = image.load(r"assets/row-1-col-1.png")

p_image = image.load(r"assets/row-2-col-6.png")  # black
r_image = image.load(r"assets/row-2-col-5.png")
n_image = image.load(r"assets/row-2-col-4.png")
b_image = image.load(r"assets/row-2-col-3.png")
q_image = image.load(r"assets/row-2-col-2.png")
k_image = image.load(r"assets/row-2-col-1.png")

# other
STARTINGPOSFEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
fen1 = "rnbqkbnr/ppp1pppp/8/3p4/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2"
fencheck = "rnbqkbnr/pppppppp/5K2/8/8/8/PPPPPPPP/RNBQ1BNR w kq - 0 1"
fenmate = "r1bqkb1r/pppp1ppp/2n2n2/4p2Q/2B1P3/8/PPPP1PPP/RNB1K1NR w KQkq - 0 1"
test = 'rn1qkb1r/pp2pppp/5n2/3p1b2/3P4/2N1P3/PP3PPP/R1BQKBNR w KQkq - 0 1 id "CCR01"; bm Qb3;'
endgame_fen = "2k5/8/8/8/2K5/8/3Q4/8 w - - 0 1"
castlefen = "r3k2r/pppppppp/8/8/8/8/PPPPPPPP/R3K2R w KQkq - 0 1"
mate2fen = "r1b2r2/pp4pp/1qnbpk2/3p2nQ/3P1N2/1P4PB/P4P1P/R1B2RK1 w - - 2 18"
mate2cool = "r1b1kb1r/3qn2p/p1Np1pn1/1p1P4/4Q2p/4R3/PPB2PPP/4R1K1 w kq - 0 24"
mate2 = "6rk/pp3prp/4bQ1R/8/3p4/1PP2N1P/1P2q3/6RK w - - 0 29"
mate3 = "6B1/p1Q4p/2P2ppk/8/4P3/4qP2/1r4rP/2R2R1K b - - 3 29"