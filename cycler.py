from copy import deepcopy

# returns set of all disjoint sets of cycles
def cycler(wt):
    global want_table
    want_table = wt
    global list_of_lists
    list_of_lists = [[] for i in range(len(want_table))]
    for i in range(len(want_table)):
        c = Cycle(i)
        _cycler(c)
    return disjointer(list_of_lists)

class Node:
    # data is an integer
    def __init__(self, data):
        self.data = data
        self.prev_node = None

    def set_prev(self, prev_node):
        self.prev_node = prev_node


class Cycle:
    # start is an integer
    def __init__(self, start_num):
        self.start = Node(start_num)
        self.end = self.start
        self.value = 0
        self.length = 1
        if start_num == 0:
            self.zeros = 1
        else:
            self.zeros = 0

    def add_node(self, next_num, add_val):
        new_node = Node(next_num)
        new_node.set_prev(self.end)
        if next_num == 0:
            self.zeros += 1
        self.end = new_node
        self.value += add_val
        self.length += 1

    def pop(self):
        if self.end != self.start:
            if self.end.data == 0:
                self.zeros -= 1
            self.end = self.end.prev_node
        self.length -= 1

    def is_disjoint(self, other_cyc):
        current = self.end
        while 1:
            oth_curr = other_cyc.end
            while 1:
                if current.data == oth_curr.data:
                    return False
                if oth_curr.prev_node is None:
                    break
                oth_curr = oth_curr.prev_node
            if current.prev_node is None:
                return True
            current = current.prev_node

    # returns true iff number is in list
    def contains(self, number):
        current = self.end
        while 1:
            if current.data == number:
                return True
            if current.prev_node is None:
                return False
            current = current.prev_node

    def print_cycle(self):
        current = self.end
        output = 'cycle: '
        while 1:
            output += str(current.data) + ' '
            if current.prev_node is None:
                break
            current = current.prev_node
        output += ' value: ' + str(self.value)
        print(output)


# cyc is a cycle with only one node. cycler finds all of the simple cycles
#   that start  with this node and adds them to the list indexed by that node.
# This is the more elegant version. Not sure if it's fast enough.
# Efficiency notes: If allowing for more than one zero in cycle, it takes forever.
# TODO MAYBE: Somehow randomly try a fraction (1/4) of the zero-paths to try?
#             And allow for two or three zeros?
def _cycler(cyc):
    if cyc.length < 4:     # adjust maximum cycle length for efficiency
        for want in want_table[cyc.end.data]:
            if cyc.zeros != 0 and  want[1] == 0:
                continue
            if want[1] == 0 and cyc.length < 3:
                continue    # for efficiency, only start with 2 positive value wants
            if want[0] < cyc.start.data:
                continue        # this refers to previous sections
            if want[0] == cyc.start.data:   # if a cycle is complete!
                if cyc.value != 0:
                    temp = deepcopy(cyc)
                    temp.value += want[1]
                    # add the completed cycle to the list of lists.
                    list_of_lists[cyc.start.data].append(temp)
                continue
            if cyc.contains(want[0]):
                continue    # found a cycle which doesn't involve cyc.start.data
            # follow want recursively
            cyc.add_node(want[0], want[1])
            _cycler(cyc)
            cyc.pop()
            cyc.value -= want[1]


# returns the set of all disjoint cycles from cycle_list,
# in the form of a list of lists.
# cycle_list[i] contains all cycles which begin with i
def disjointer(cycle_list):
    results = [[]]  # start with the empty set
    disjoint_so_far = True
    for i in range(len(cycle_list)):
        more_results = []
        for result in results:
            for cyc in cycle_list[i]:   # cyc is a cycle that starts with i
                disjoint_so_far = True
                for other_cyc in result:
                    if not cyc.is_disjoint(other_cyc):
                        disjoint_so_far = False
                        break
                if disjoint_so_far:
                    more_results.append(result + [cyc])
        results.extend(more_results)
    return results


#c = Cycle(0)
#c.print_cycle()
#
#
#c.add_node(1,1)
#c.add_node(2,1)
#c.add_node(3,1)
#c.print_cycle()
#print(c.contains(3))
#print(c.contains(0))
#print(c.contains(7))


#want: [(y_1,v_1), ... ,(y_n,v_n)]
#want_table[x] = list of courses that owner of course index x wants
#y_i = one section's ID, desired by this section's owner in a trade
#v_i = how much more this section's owner would bid for the trade

'''old_test_want_table = []
old_test_want_table.append([(1,1), (2,1)]) #sections 0's owner wants
old_test_want_table.append([(0,1), (2,1), (5,1)])
old_test_want_table.append([(3,1)])
old_test_want_table.append([(0,1), (1,1), (2,1), (4,1)])
old_test_want_table.append([(0,1)])
old_test_want_table.append([(6,1)])
old_test_want_table.append([])'''
#the above test was successful!

'''want_table = []
want_table.append([(1, 0), (7, 0)])  # section 0's owner wants these to trade for section 0
want_table.append([]) #section 1's owner doesn't want anything for section 1
want_table.append([(1,2),(4,2),(5,2)])
want_table.append([])
want_table.append([(2,4)])
want_table.append([(8,5)])
want_table.append([(0,6)])
want_table.append([(6,7),(9,7)])
want_table.append([(9,8),(5,8)])
want_table.append([(5,9)])'''
#the above test was successful!

#want_table = []
#want_table.append([(1,0),(2,0)])
#want_table.append([(0,1),(2,1)])
#want_table.append([(0,2),(1,2)])
#the above test was successful!

# big test: 200 sections with 5 wants each
# from random import randint
# 
# want_table = []
# for i in range(200):
#     this_row = []
#     for j in range(randint(0, 5)):
#         k = randint(0,199)
#         if k != i:
#             this_row.append((k, 1))
#     want_table.append(this_row)


#for j in range(len(list_of_lists)):
#    for i in range(len(list_of_lists[j])):
#        for k in range(len(list_of_lists)):
#            for m in range(len(list_of_lists[k])):
#                list_of_lists[j][i].print_cycle()
#                list_of_lists[k][m].print_cycle()
#                print(list_of_lists[j][i].is_disjoint(list_of_lists[k][m]))

#
#for i in disjoint_sets:
#    print('disjoint set: ')
#    for j in i:
#        j.print_cycle()



if(__name__ == '__main__'):
    table = []
    table.append([(1, 0), (7, 0)])  # section 0's owner wants these to trade for section 0
    table.append([]) #section 1's owner doesn't want anything for section 1
    table.append([(1,2),(4,2),(5,2)])
    table.append([])
    table.append([(2,4)])
    table.append([(8,5)])
    table.append([(0,6)])
    table.append([(6,7),(9,7)])
    table.append([(9,8),(5,8)])
    table.append([(5,9)])
    dj = cycler(table)
    for d in dj:
        print('disjoint set: ')
        for c in d:
            c.print_cycle()