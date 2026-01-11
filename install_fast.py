import os
import shutil
if os.path.isfile("drawmaster.py") == False:
    os.system("python3 make_fast.py")
file = open("drawmaster.py")
lines = [line.rstrip() for line in file]
file.close()
if 'engine = chess.engine.SimpleEngine.popen_uci("")' in lines:
    lines[lines.index('engine = chess.engine.SimpleEngine.popen_uci("")')] = f'engine = chess.engine.SimpleEngine.popen_uci("{input("Engine Path: ")}")'
    file = open("drawmaster.py", "w")
    for line in lines:
        file.write(line+"\n")
    file.close()
if os.path.isdir("_internal"):
    shutil.rmtree("_internal")
if os.path.isfile("drawmaster"):
    os.remove("drawmaster")
os.system("python3 -m PyInstaller drawmaster.py")
os.chdir("dist/drawmaster")
os.system("mv * ../..")
os.chdir("../..")
shutil.rmtree("build")
shutil.rmtree("dist")
os.remove("drawmaster.spec")