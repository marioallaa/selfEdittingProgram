

with open("main.py", "r") as f:
     old = f.read()
     
with open("main.py", "w") as f:
     f.seek(0) 
     f.write(" \n \nprint('hello from a new line')"  + old ) 
 
 
import subprocess  

def runAgain(c):
    subprocess.call(["bash", "-c", "source ~/.profile; " + c])  

runAgain('python main.py')

exit()
