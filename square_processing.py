def square_preceding(values):

    """ (list of number) -> NoneType

    Replace each item in the list with square the value of the

    preceding item, and replace the first item with 0.

    # >>> L = [1, 2, 3]
    #
    # >>> square_preceding(L)
    #
    # >>> L

    [0, 1, 4]

    """
    temp = []

    if values != []:
        temp.append(values[0])
        values[0] = 0
        for i in range(len(values)-1):
            temp.append(values[i+1])
            values[i+1] = temp[i] ** 2

    return values

    # return [0] + [values[i-1] ** 2 for i in range (1, len(values))]  This way would be better

print(square_preceding([1, 2, 3]))
