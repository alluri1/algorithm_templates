from collections import deque

# In-order recursive
def inorder_recursive(root):
    if root is None:
        return
    inorder_recursive(root.left)
    print(root.data)
    inorder_recursive(root.right)

# Pre-order recursive
def preorder_recursive(root):
    if root is None:
        return
    print(root.data)
    preorder_recursive(root.left)
    preorder_recursive(root.right)

# Post-order recursive
def postorder_recursive(root):
    if root is None:
        return
    postorder_recursive(root.left)
    postorder_recursive(root.right)
    print(root.data)

# Level order
def level_order_traversal(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        curr = queue.popleft()
        print(curr.val, end = "")
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
        
