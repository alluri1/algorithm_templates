#102 - binary tree level order traversal
# recording the size of queue, gives us the number of nodes at that level
# append each level to inner list
# TC:O(n) , SC: O(n) - number of nodes, each node is visited once
def level_order_traversal(root):
    if root is None:
        # None or default value
        return None
    output = []
    q = []
    while q:
        num_nodes = len(q)
        level = []
        for _ in range(num_nodes):
            curr = q.pop()
            level.append(curr.val)
            if curr.left:
                level.append(curr.left)
            if curr.right:
                level.append(curr.right)
            output.append(level)
    return output

def n_ary_level_order_traversal(root):
    if root is None:
        # None or default value
        return None
    output = []
    q = []
    while q:
        num_nodes = len(q)
        level = []
        for _ in range(num_nodes):
            curr = q.pop()
            level.append(curr.val)
            ###
            for child in curr.children:
                q.append(child)
            output.append(level)
    return output


def reverse_level_order_traversal(root):
    if root is None:
        # None or default value
        return None
    output = []
    q = []
    while q:
        num_nodes = len(q)
        level = []
        for _ in range(num_nodes):
            curr = q.pop()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            output.append(level)
    ###
    output.reverse()
    return output

# use a level element instead of list, so that only last element is stored
def right_side_view(root):
    if root is None:
        # None or default value
        return None
    output = []
    q = []
    while q:
        num_nodes = len(q)
        level = None
        for _ in range(num_nodes):
            curr = q.pop()
            level = curr.val
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            output.append(level)

    return output

# use flag and flip it at every level
def zigzag_level_order_traversal(root):
    if root is None:
        # None or default value
        return None
    output = []
    q = [root]
    l_to_r = True
    while q:
        num_nodes = len(q)
        level = []

        for _ in range(num_nodes):
            curr = q.pop()
            level.append(curr.val)
            if curr.left:
                level.append(curr.left)
            if curr.right:
                level.append(curr.right)
            if l_to_r:
                output.append(level)
            else:
                output.append(level.reverse())
            l_to_r = not l_to_r
    return output