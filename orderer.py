#Adapted from www.101computing.net/sudoku-generator-algorithm/
from random import randint, shuffle


# Use this! This returns a list of count lists of length,
# each with every number in range(count) appearing once in each position
def orderer(count):
    global fac_count
    fac_count = count
    global order
    order = [[fac_count + 1] * fac_count for i in range(fac_count)]
    global numberList
    numberList = list(range(fac_count))
    fill_order(order)
    return order


# A function to check if the order is full
def check_order(order):
    for row in range(fac_count):
            for col in range(fac_count):
                if order[row][col] == fac_count + 1:
                    return False
    # We have a complete grid!
    return True


def fill_order(order):
    # Find next empty cell
    for i in range(0, fac_count*fac_count):
        row = i // fac_count
        col = i % fac_count
        if order[row][col] == fac_count + 1:
            shuffle(numberList)
            for value in numberList:
                # Check that this value has not already be used on this row
                if value not in order[row]:
                    # Check this value has not already be used on this column
                    if value not in [order[i][col] for i in range(fac_count)]:
                        order[row][col] = value
                        if check_order(order):
                            return True
                        else:
                            if fill_order(order):
                                return True
            break
    order[row][col] = fac_count + 1             

'''test = orderer(10)
#test output:
for i in test:
  print(i)'''
