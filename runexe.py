import os, subprocess
FNULL = open( os.devnull, 'w' )
filename = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
args = ""
subprocess.call( filename + args, stdout=FNULL, stderr=FNULL, shell=False )
