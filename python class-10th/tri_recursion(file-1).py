def tri_recursion(k):
    if( k > 0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
print("\n\n Recursion Example Result")
tri_recursion(int(input("Enter num")))

