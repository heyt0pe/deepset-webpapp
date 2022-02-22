array = [1, 2, 3]


def searchIndex(numbers, target):

    # sort the array every time function is called
    numbers.sort()

    # check if that number is even in the array at all
    if(numbers.count(target) < 1):

        # means the number is not in the array
        # so we add it to the array
        # sort the new array (Since we added a new number)
        # return the index of the new number we added

        numbers.append(target)
        numbers.sort()
        return numbers.index(target)

    else:

        # means the number is in the array 
        # return thr index of th number
        return numbers.index(target)

print(searchIndex(array, 10))
