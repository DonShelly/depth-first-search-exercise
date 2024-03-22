class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    def __str__(self):
        return "Node(" + str(self.value) + ")"
    
def walk(tree, stack):
    stack.append(tree)
    while len(stack) > 0:
        node = stack.pop()
        if node is not None:
            print(node)
            stack.append(node.right)
            stack.append(node.left)

stack = []

tree = Node('A', Node('B', Node('D'), Node('E')), Node('C', Node('F', Node('G'), Node('H'))))


if __name__ == "__main__":
    walk(tree, stack)