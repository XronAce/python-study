import os

f = open("before.txt", "w")
f.close()

os.rename("before.txt", "after.txt")