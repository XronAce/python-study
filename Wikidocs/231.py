def n_plus_1 (n) :
    result = n + 1

#n_plus_1(3)
#print (result)

"""
This function will throw error, since the variable 'result' is internal variable which cannot be accessed externally.
You must declare a new variable at the outside of the function like this:
result = n_plus_1(3)
print(result)
"""