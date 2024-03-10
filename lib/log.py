import os
log = os.system("git log --oneline --all")
print(log)
os.system(f'echo  "{str(log)}" >> "file.txt" ')

