import subprocess
import os.path
save_path = "C:\\Users\\"
pcName = input("What is your PC name: ")
completeName = os.path.join(save_path, pcName)


# subprocess.Popen('explorer "C:\\Windows\\Prefetch"')
# subprocess.Popen('explorer "C:\\Windows\\Temp"')
# subprocess.Popen('explorer "C:\\Users\\Nasif Azam\\AppData\\Local\\Temp"')
subprocess.Popen(['explorer', completeName, "\\AppData\\Local\\Temp"])
# subprocess.Popen('explorer "C:\\Users\\Nasif Azam\\Recent"')
# subprocess.Popen('explorer "C:\\Windows\\System32\\tree.com"')
