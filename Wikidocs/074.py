t = (1, 2, 3)
#t[0] = 'a' #This will throw an error because tuple cannot change its element. Tuple is immutable.
t = ('a', 2, 3) # You must reassign tuple 't' to mutate its element.
print(t)