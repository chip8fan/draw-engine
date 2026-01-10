import os
import shutil
file = open("draw-engine.py")
lines = [line.rstrip() for line in file]
file.close()
if 'engine = chess.engine.SimpleEngine.popen_uci("")' in lines:
    lines[lines.index('engine = chess.engine.SimpleEngine.popen_uci("")')] = f'engine = chess.engine.SimpleEngine.popen_uci("{input("Engine Path: ")}")'
    file = open("draw-engine.py", "w")
    for line in lines:
        file.write(line+"\n")
    file.close()
if os.path.isdir("_internal"):
    shutil.rmtree("_internal")
    os.remove("draw-engine")
os.system("python3 -m PyInstaller draw-engine.py")
os.chdir("dist/draw-engine")
os.system("mv * ../..")
os.chdir("../..")
shutil.rmtree("build")
shutil.rmtree("dist")
os.remove("draw-engine.spec")