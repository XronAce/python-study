def fib_optimized(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        prev = 1
        curr = 1
        for i in range(3, n+1):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr



# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))

"""
This function optimizes the memory space by only recording the two last fibonacci numbers.
"""