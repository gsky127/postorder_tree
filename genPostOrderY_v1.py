from treev2 import dtree



def genPostOrderY(Dtree, root, k):
    if Dtree.getChildrenID(root, k) == []:
        data = Dtree.tree.get_node(root).data
        data['y'] = data['x'] * 2
        return data['y']
    tmp = Dtree.tree.get_node(root).data['x']
    for leaf_idx in Dtree.getChildrenID(root, k):
        Dtree.tree.get_node(leaf_idx).data['x'] = tmp
        if leaf_idx == Dtree.getChildrenID(root, k)[-1]:
            Dtree.tree.get_node(root).data['y'] = genPostOrderY(Dtree,leaf_idx, k)
        else:
            tmp = genPostOrderY(Dtree,leaf_idx, k)
    return Dtree.tree.get_node(root).data['y']




if __name__ == '__main__':
    Dtree = dtree()
    width = 3
    depth = 1
    Dtree.BuildTree(width, depth)
    print(Dtree.tree.all_nodes())
    genPostOrderY(Dtree, 1, width)
    print(Dtree.tree.all_nodes())
    # Dtree.tree.show()
