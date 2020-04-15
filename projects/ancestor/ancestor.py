
def earliest_ancestor(ancestors, starting_node):

    vertex = {}
    parent = []
    child = []

    for ancestor in ancestors:
        vertex[ancestor[0]] = set()
        vertex[ancestor[1]] = set()
        parent.append(ancestor[0])
        child.append(ancestor[1])


    for i in range(0, len(parent)):
        vertex[child[i]].add(parent[i])

    n = 0
    while len(vertex[starting_node]) != 0:
        n += 1

        if starting_node in vertex:
            if len(vertex[starting_node]) > 1:
                starting_node = min(vertex[starting_node])
            else:
                starting_node = vertex[starting_node].pop()

    if n == 0:
        return -1

    return starting_node




'''
       10
     /
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \
        6   7   9
    '''

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# print("s",sorted(test_ancestors))

print(earliest_ancestor(test_ancestors, 9))




