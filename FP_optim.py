from collections import OrderedDict

if __name__ == '__main__':
    class treeNode:
        def __init__(self, nameValue, numOccur, parentNode):
            self.name = nameValue  # 节点名称
            self.count = numOccur  # 节点出现的次数
            self.nodeLink = None  # 链接指向的下一个节点
            self.parent = parentNode  # 父节点
            self.children = {}  # 子节点


        def inc(self, numOccur):  # 该函数用来增加节点出现的次数
            self.count += numOccur

        def disp(self, ind=1):
            # print ' '*ind,self.name,' ',self.count #展示节点名称和出现的次数
            print('  ' * ind, self.name, ' ', self.count)
            for child in self.children.values():
                child.disp(ind + 1)  # 打印时，子节点的缩进比父节点更深一级


    def loadSimpDat():
        simpDat = [['r', 'z', 'h', 'j', 'p'],
                   ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
                   ['z'],
                   ['r', 'x', 'n', 'o', 's'],
                   ['y', 'r', 'x', 'z', 'q', 't', 'p'],
                   ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
        return simpDat


    def createInitSet(dataSet):
        retDict = OrderedDict()
        for trans in dataSet:
            retDict[frozenset(trans)] = 1
        return retDict


    # # rootNode = treeNode('pyramid', 9, None)  # 创建节点
    # # rootNode.children['eye'] = treeNode('eye', 13, None)  # 增加子节点
    # # rootNode.children['phoenix'] = treeNode('phoenix', 3, None)  # 增加另一个子节点
    # # rootNode.disp()  # 展示树
    #
    # simpDat = loadSimpDat()
    # # print(simpDat)
    # dataSet = createInitSet(simpDat)
    # print(dataSet)
    #
    # headerTable = {}  # 用来存储每项元素及其出现次数
    # for trans in dataSet:  # 遍历每条记录
    #     # print(trans)
    #     for item in trans:  # 遍历每条记录的每项元素
    #         # print(item)
    #         # headerTable.get(item, 0) item存在则返回对应值，不存在则返回0
    #         headerTable[item] = headerTable.get(item, 0) + dataSet[
    #             trans]  # 计算每项元素的出现次数            print(item,headerTable[item],dataSet[trans])
    # print(headerTable)
    # print("headerTable's length: %s" % len(headerTable))
    #
    # for k in list(headerTable.keys()):
    #     if headerTable[k] < 3:  # 这里的3是指最小支持度的取值，可根据实际情况改变
    #         del (headerTable[k])  # 如果某项元素的支持度小于最小支持度，从headerTable中删掉该元素
    # freqItemSet = set(headerTable.keys())  # freqItemSet中的每一项元素的支持度均大于或等于最小支持度
    #
    # print(headerTable)
    # print("headerTable's length: %s" % len(headerTable))
    #
    # if len(freqItemSet) != 0:
    #     for k in headerTable:
    #         headerTable[k] = [headerTable[k], None]
    # print('headerTable为：', headerTable)
    #
    # for tranSet, count in dataSet.items():  # 遍历每一条事务数据
    #     # print('tranSet为：',tranSet)
    #     # print('count为：',count)
    #     localD = {}
    #     for item in tranSet:  # 遍历这条数据中的每个元素
    #         if item in freqItemSet:  # 过滤每条记录中支持度小于最小支持度的元素
    #             localD[item] = headerTable[item][0]  # 把headerTable中记录的该元素的出现次数赋值给localD中的对应键
    #     #         print('headerTable[item][0]为：', headerTable[item][0])
    #     # print('localD为：', localD)
    #     # print('localD.items()为：', localD.items())
    #     if len(localD) > 0:  # 如果该条记录有符合条件的元素
    #         orderedItems = [v[0] for v in
    #                         sorted(localD.items(), key=lambda p: p[1], reverse=True)]  # 元素按照支持度排序，支持度越大，排位越靠前
    #         print(orderedItems)

    def createTree(dataSet, minSup=1):
        headerTable = {}  # 用来存储每项元素及其出现次数
        for trans in dataSet:  # 遍历每条记录
            # print(trans)
            for item in trans:  # 遍历每条记录的每项元素
                # print(item)
                # headerTable.get(item, 0) item存在则返回对应值，不存在则返回0
                headerTable[item] = headerTable.get(item, 0) + dataSet[trans]  # 计算每项元素的出现次数
                # print(item,headerTable[item],dataSet[trans])
        print('统计次数后的headerTable为：', headerTable)
        print("headerTable's length: %s" % len(headerTable))

        for k in list(headerTable.keys()):
            if headerTable[k] < 3:  # 这里的3是指最小支持度的取值，可根据实际情况改变
                del (headerTable[k])  # 如果某项元素的支持度小于最小支持度，从headerTable中删掉该元素
        freqItemSet = set(headerTable.keys())  # freqItemSet中的每一项元素的支持度均大于或等于最小支持度

        print('除去不满足最小支持度后的headerTable为：', headerTable)
        print("headerTable's length: %s" % len(headerTable))

        if len(freqItemSet) != 0:
            for k in headerTable:
                headerTable[k] = [headerTable[k], None]
        print('headerTable为：', headerTable)
        retTree = treeNode('Null Set', 1, None)  # 创建根节点
        for tranSet, count in dataSet.items():  # 遍历每一条事务数据
            # print('tranSet为：',tranSet)
            # print('count为：',count)
            localD = {}
            for item in tranSet:  # 遍历这条数据中的每个元素
                if item in freqItemSet:  # 过滤每条记录中支持度小于最小支持度的元素
                    localD[item] = headerTable[item][0]  # 把headerTable中记录的该元素的出现次数赋值给localD中的对应键
            #         print('headerTable[item][0]为：', headerTable[item][0])
            # print('localD为：', localD)
            # print('localD.items()为：', localD.items())
            if len(localD) > 0:  # 如果该条记录有符合条件的元素
                orderedItems = [v[0] for v in
                                sorted(localD.items(), key=lambda p: p[1], reverse=True)]  # 元素按照支持度排序，支持度越大，排位越靠前
                print('orderedItems为：', orderedItems, '===retTree为：', retTree.name, '===count为：', count)
                updateTree(orderedItems, retTree, headerTable, count)
        return retTree, headerTable


    def updateTree(items, inTree, headerTable, count):
        if items[0] in inTree.children:  # 如果inTree的子节点中已经存在该元素
            inTree.children[items[0]].inc(count)  # 树中该元素增加值，增加的值为该元素所在记录的出现次数
        else:
            inTree.children[items[0]] = treeNode(items[0], count, inTree)  # 如果树中不存在该元素，重新创建一个节点
            if headerTable[items[0]][1] == None:  # 如果在相似元素的字典headerTable中，该元素键对应的列表值中，起始元素为None
                headerTable[items[0]][1] = inTree.children[items[0]]  # 把新创建的这个节点赋值给起始元素
            else:
                updateHeader(headerTable[items[0]][1],
                             inTree.children[items[0]])  # 如果在相似元素字典headerTable中，该元素键对应的值列表中已经有了起始元素，那么把这个新建的节点放到值列表的最后
        if len(items) > 1:  # 如果在这条记录中，符合条件的元素个数大于1
            updateTree(items[1::], inTree.children[items[0]], headerTable, count)  # 从第二个元素开始，递归调用updateTree函数。


    def updateHeader(nodeToTest, targetNode):  # 该函数实现把targetNode放到链接的末端
        while (nodeToTest.nodeLink != None):
            nodeToTest = nodeToTest.nodeLink
        nodeToTest.nodeLink = targetNode


    def ascendTree(leafNode, prefixPath):  # 该函数找出元素节点leafNode的所有前缀路径，并把包括该leafNode及其前缀路径的各个节点的名称保存在prefixPath中
        if leafNode.parent != None:
            prefixPath.append(leafNode.name)
            ascendTree(leafNode.parent, prefixPath)


    def findPrefixPath(basePat, treeNode):
        condPats = {}
        while treeNode != None:
            prefixPath = []
            ascendTree(treeNode, prefixPath)
            if len(prefixPath) > 1:
                condPats[frozenset(prefixPath[1:])] = treeNode.count  # 某个元素的前缀路径不包括该元素本身
            treeNode = treeNode.nodeLink  # 下一个相似元素
        return condPats  # condPats存储的是元素节点treeNode及其所有相似元素节点的前缀路径和它的计数


    simpDat = loadSimpDat()
    initSet = createInitSet(simpDat)
    print('initSet为：', initSet)
    myFPtree, myHeaderTab = createTree(initSet, 3)  # 最小支持度
    myFPtree.disp()
    freqItemSet = ['s', 'r', 't', 'y', 'x', 'z']
    for item in freqItemSet:
        condPats = findPrefixPath(item, myHeaderTab[item][1])
        print(item)
        print(condPats)
