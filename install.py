import os
import shutil
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