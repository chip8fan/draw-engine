import sys
import chess
import chess.engine
import random
engine = chess.engine.SimpleEngine.popen_uci("")
while True:
    line = sys.stdin.readline().split()
    if line[0] == "uci":
        print("id name Draw-Engine")
        print("id author DrawMaster")
        print("uciok")
    elif line[0] == "isready":
        print("readyok")
    elif line[0] == "position":
        if "fen" in line:
            board = chess.Board(fen=" ".join(line[2:]).split(" moves")[0])
        elif "startpos" in line:
            board = chess.Board()
        if "moves" in line:
            move_list = line[3:]
            for move in move_list:
                board.push_uci(move)
    elif line[0] == "go":
        if "wtime" in line:
            white_clock = int(line[line.index("wtime")+1])/1000
        else:
            white_clock = None
        if "btime" in line:
            black_clock = int(line[line.index("btime")+1])/1000
        else:
            black_clock = None
        if "winc" in line:
            white_inc = int(line[line.index("winc")+1])/1000
        else:
            white_inc = None
        if "binc" in line:
            black_inc = int(line[line.index("binc")+1])/1000
        else:
            black_inc = None
        num = len(list(board.legal_moves))
        multipv = 3
        moves = []
        for move in board.legal_moves:
            board.push(move)
            moves.append([abs(engine.analyse(board, chess.engine.Limit(white_clock=white_clock/num, black_clock=black_clock/num, white_inc=white_inc, black_inc=black_inc))["score"].relative.score(mate_score=sys.maxsize)), move])
            board.pop()
        print(f"bestmove {random.choice(sorted(moves, key=lambda x: x[0])[:multipv])[1]}")
    elif line[0] == "quit":
        break
    sys.stdout.flush()
engine.quit()