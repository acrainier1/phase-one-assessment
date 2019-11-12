# The time complexity (Big-O) of this algorithm is O(n) 
# because worst case scenario requires n shifts

def zero_shift(alist)
    n = len(a_list)

    for i in range(n):
        for j in range(n-1):
            if a_list[j] == 0:
                a_list[j] = a_list[j+1]
                a_list[j+1] = 0
    print(a_list)
    return None

if __name__ == "__main__":
    pass
    #
    # values = [3, 0, 9, 10, 0, 1, 0, 7]
    # zero_shift(values)
    # assert values == [3, 9, 10, 1, 7, 0, 0, 0]
