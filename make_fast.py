file = open("draw-engine.py")
lines = [line.rstrip() for line in file]
file.close()
lines[lines.index('            moves.append([abs(engine.analyse(board, chess.engine.Limit(time=1))["score"].relative.score(mate_score=sys.maxsize)), move])')] = lines[lines.index('            moves.append([abs(engine.analyse(board, chess.engine.Limit(time=1))["score"].relative.score(mate_score=sys.maxsize)), move])')].replace("time=", "depth=")
file = open("drawmaster.py", "w")
for line in lines:
    file.write(line+"\n")
file.close()