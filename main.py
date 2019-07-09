

with open("main.py", "r+") as f:
     old = f.read()
     f.seek(0) 
     f.write(" \n \nprint('Hello {} "+" World'.format({0})) \n\n".format(4)  + old ) 
 
 
import subprocess  

def runAgain(c):
    subprocess.call(["bash", "-c", "source ~/.profile; " + c])  

runAgain('python main.py')
