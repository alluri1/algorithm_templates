class TreeNode:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

# TC : O(h) = O(log n) for balanced tree
def search(root, key):
    curr = root
    while curr:
        if curr.key == key:
            return curr
        elif key < curr.key:
            curr = curr.left
        else:
            curr = curr.right
    return None

# Search first, need prev pointer to attach to it. always add a node at leaf level
# if curr became null after jumping to left(k<curr.key), we attach new node on the left
def insert(root, key):
    new_node = TreeNode(key)
    prev = None
    curr = root
    while curr:
        if curr.key == key:
            return curr
        elif key < curr.key:
            prev = curr
            curr = curr.left
        else:
            prev = curr
            curr = curr.right

    if key < prev.key:
        prev.left = new_node
    else:
        prev.right = new_node

    return root

# min - find the least most node in the tree
# only possible in BST in O(log n) as they maintain order (ordered dictionaries),
# not possible in hash table
def find_min(root):
    if root is None:
        return None
    curr = root
    while curr.left:
        curr = curr.left
    return curr.key

# max - find the max node in the tree
def find_max(root):
    if root is None:
        return None
    curr = root
    while curr.left:
        curr = curr.left
    return curr.key

# successor is the next largest key in the tree
# only max element doesn't hav successor in the tree
# case 1 : If node has right subtree, minimum number in the right subtree is the successor
# case 2 : If node doesn't have right subtree, we take the parent to which the node is left child (up and right turn)
# case 3:  If node doesn't have right subtree and doesn't have parent to which it is left child (no up-right turn),
#          we follow the ancestral path until we reach a node that is left child (up & left until right turn)
def find_successor(root, p):
    if root is None:
        return None

    # case 1 : find min in right subtree
    if p.right:
        curr = p.right
        while curr.left:
            curr = curr.left
        return curr

    # no parent pointers to look up, so we search for p from root
    # and track deep-est left turn from the root, we keep updating when left child is accessed until the node
    else:
        ancestor = None
        curr = root
        while curr is not p:
            if p.key < curr.key:
                ancestor = curr
                curr = curr.left
            else:
                curr = curr.right

        return ancestor

# the key may not exist in the tree
# case 1: node to be deleted is a leaf, set left pointer to null if node is deleted from prev left
# case 2: node has one child
def delete(root, key):
    # search for the key
    curr = root
    prev = None
    while curr:
        if key == curr.key:
            break
        elif key < curr.key:
            prev = curr
            curr = curr.left
        else:
            prev = curr
            curr = curr.right

    # node not found or tree is empty, return the original tree
    if not curr:
        return root

    # case1 : leaf node - check if it is left or right child of prev that needs to be set to None
    if not curr.left and not curr.right:
        ## edge case - one node tree
        if prev is None:
            return None
        if curr == prev.left:
            prev.left = None
        else:
            prev.right = None

        return root

    # case2: one child, find the child and if prev.left is child, we point prev's left pointer to child
    child = None
    elif curr.right and not curr.left:
        child = curr.right
    elif curr.left and not curr.right:
        child = curr.left






