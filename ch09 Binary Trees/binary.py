class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right



    #                314
    #             /       \
    #         6               6
    #       /   \          /    \
    #     271   561       2      271
    #    /  \      \       \       \
    #  28    0      3       1        28
    #              /       / \
    #             17     401  257
    #                     \
    #                     641

M = TreeNode(641)
N = TreeNode(257)
P = TreeNode(28)
D = TreeNode(28)
E = TreeNode(0)
H = TreeNode(17)
L = TreeNode(401, None, M)
K = TreeNode(1, L, N)
J = TreeNode(2, None, K)
O = TreeNode(271, None, P)
G = TreeNode(3, H, None)
F = TreeNode(561, None, G)
C = TreeNode(271, D, E)
I = TreeNode(6, J, O)
B = TreeNode(6, C, F)
root = TreeNode(341, B, I)


def preorder_traversal(node):
    if node:
        print("Preorder: {}".format(node.data))
        preorder_traversal(node.left)
        preorder_traversal(node.right)


def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print("Inorder: {}".format(node.data))
        inorder_traversal(node.right)


def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print("Postorder: {}".format(node.data))


preorder_traversal(root)


