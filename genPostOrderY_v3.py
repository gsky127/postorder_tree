from treev2 import dtree
import genlogger
import uVDF

Lambda = 1024

# Eval(Lambda, pp, x0, t)
def eval(Dtree, root, string, pp, width):
    data = Dtree.tree.get_node(root).data
    data['y'], data['pai'] = uVDF.Eval(Lambda, pp, data['x'], width*width)

def verify(Dtree, width, depth, string, pp):
    DtreeVf = dtree()
    DtreeVf.BuildTree(width, depth)
    return vfTree(DtreeVf, Dtree, 1, width, string, pp), DtreeVf

def vfTree(DtreeVf, Dtree, root, k, string, pp):
    if DtreeVf.getChildrenID(root, k) == []:
        eval(DtreeVf, root, string, pp, k)
        return DtreeVf.tree.get_node(root).data == Dtree.tree.get_node(root).data
    tmpy = DtreeVf.tree.get_node(root).data['x']
    tmppai = DtreeVf.tree.get_node(root).data['pai']
    if tmppai == None:
        tmppai = string
    for leaf_idx in DtreeVf.getChildrenID(root, k):
        DtreeVf.tree.get_node(leaf_idx).data['x'] = tmpy
        if leaf_idx == DtreeVf.getChildrenID(root, k)[-1]:
            data = DtreeVf.tree.get_node(root).data
            data['y'], data['pai'] = genPostOrderY(DtreeVf, leaf_idx, k, tmppai, pp)
            return DtreeVf.tree.get_node(root).data == Dtree.tree.get_node(root).data
        else:
            tmpy, tmppai = genPostOrderY(DtreeVf, leaf_idx, k, tmppai, pp)
    return DtreeVf.tree.get_node(root).data == Dtree.tree.get_node(root).data

def genPostOrderY(Dtree, root, k, string, pp):
    if Dtree.getChildrenID(root, k) == []:
        eval(Dtree, root, string, pp, k)
        return Dtree.tree.get_node(root).data['y'], Dtree.tree.get_node(root).data['pai']
    tmpy = Dtree.tree.get_node(root).data['x']
    tmppai = Dtree.tree.get_node(root).data['pai']
    if tmppai == None:
        tmppai = string
    for leaf_idx in Dtree.getChildrenID(root, k):
        # print("root为:", root)
        Dtree.tree.get_node(leaf_idx).data['x'] = tmpy
        if leaf_idx == Dtree.getChildrenID(root, k)[-1]:
            data = Dtree.tree.get_node(root).data
            data['y'], data['pai'] = genPostOrderY(Dtree, leaf_idx, k, tmppai, pp)
            # print(leaf_idx, "结束")
        else:
            tmpy, tmppai = genPostOrderY(Dtree, leaf_idx, k, tmppai, pp)
    return Dtree.tree.get_node(root).data['y'], Dtree.tree.get_node(root).data['pai']


if __name__ == '__main__':
    log = genlogger.Logger(level="info").logger
    log.info("begin")
    Dtree = dtree()
    width = 3
    depth = 2
    string = 'ok'
    t = pow(width, depth)   # t = pow(k, h)
    B = t
    pp = (32317006071311007300714876688669951960444102669715484032130345427524655138867890893197201411522913463688717960921898019494119559150490921095088152386448283120630877367300996091750197750389652106796057638384067568276792218642619756161838094338476170470581645852036305042887575891541065808607552399123931018060377997805978415143284572041754169996577559050047772236442528231416907538063350619791066943889311462212082685761586835867184378784402548707287314834561012337870145137505699230030672681448653160520790744306975001078094695646357307326573231447596047146610703048997252261904244564596498937536361545364691905831683, B, width, 1)
    Dtree.BuildTree(width, depth)
    root = 1
    genPostOrderY(Dtree, root, width, string, pp)
    # print(Dtree.tree.all_nodes())
    result, DtreeVf = verify(Dtree, width, depth, string, pp)
    log.info("result:" + str(result))
    log.info(DtreeVf.tree.all_nodes())
    # Dtree.tree.show()
