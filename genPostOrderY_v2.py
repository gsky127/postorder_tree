# 加入pai
from treev2 import dtree

def genPostOrderY(Dtree, root, k, string):
    if Dtree.getChildrenID(root, k) == []:
        data = Dtree.tree.get_node(root).data
        data['y'] = data['x'] * 2
        data['pai'] = string + str(data['y'])
        return data['y'], data['pai']
    tmpy = Dtree.tree.get_node(root).data['x']
    tmppai = Dtree.tree.get_node(root).data['pai']
    if tmppai == None:
        tmppai = string
    for leaf_idx in Dtree.getChildrenID(root, k):
        # print("root为:", root)
        Dtree.tree.get_node(leaf_idx).data['x'] = tmpy
        if leaf_idx == Dtree.getChildrenID(root, k)[-1]:
            data = Dtree.tree.get_node(root).data
            data['y'], data['pai'] = genPostOrderY(Dtree, leaf_idx, k, tmppai)
            # print(leaf_idx, "结束")
        else:
            tmpy, tmppai = genPostOrderY(Dtree, leaf_idx, k, tmppai)
    return Dtree.tree.get_node(root).data['y'], Dtree.tree.get_node(root).data['pai']

if __name__ == '__main__':
    Dtree = dtree()
    width = 3
    depth = 2
    Dtree.BuildTree(width, depth)
    print(Dtree.tree.all_nodes())
    genPostOrderY(Dtree, 1, width, 'ok')
    print(Dtree.tree.all_nodes())
    # Dtree.tree.show()
