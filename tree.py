#!python
# solidity.readthedocs.io

class DjikstaTreeNode(object):

    def __init__(self, weight):
        self.weight = weight
        self.id = id
        self.is_visited = False
        self.above = None
        self.below = None
        self.next = None
        self.below_right = None
        self.above_right = None
    
    def __repr__(self):
        return 'DjikstraTreeNode({!r})'.format(self.weight)

class DjikstraTree(object):
    
    def __init__(self, items = None, grid_max_width = 5):
        self.root = None
        self.size = 0
        self.grid_width = 0
        self.grid_max_width = (grid_max_width)
        if items is not None:
            for item in items:
                self.insert(item)
    
    def __repr__(self):
        return 'DjikstraTree({} nodes)'.format(self.size)
    
    def is_empty(self):
        return self.root is None
    
    def insert(self, weight):
        column = 0
        # row = 0
        node_id = 0

        if self.is_empty():                     #   Handle case where tree is empty
            self.root = DjikstaTreeNode(weight) #   Set first node as root of tree
            self.root.id = node_id              #   Set initial nodes id to 0
            self.size += 1                      #   increase size for each added node
            column += 1
            return

        prev_node = self._find_previous(node_id, self.root)

        if column <= self.grid_max_width:
            prev_node.next = DjikstaTreeNode(weight)
            self.size += 1
            column += 1
        
        # if column > self.grid_max_width:
        #     column = 0
        #     row += 1




    def _find_previous(self, node_id, node, prev_node = None):
        if node is None:
            return prev_node

        elif node_id == node.id:
            return prev_node
        
        elif node_id < node.id:
            return self._find_previous(node_id, node.next, node)

    
    def _find_above(self, id):
        pass

    def _find_above_left(self, id):
        pass
    

def test_djikstra_tree():
    weights =  [1, 2, 3, 4, 5]
    print('items: {}'.format(weights))

    tree = DjikstraTree()

    tree.insert(weights[1])
    
    for weight in weights:
        tree.insert(weight)
        print('insert({}), size: {}'.format(weight, tree.size))
    
    print('tree: {}'.format(tree))

test_djikstra_tree()