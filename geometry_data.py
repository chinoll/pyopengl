import numpy as np
class DotList:
    def __init__(self):
        self.dot = []
    def add_dot(self,pos):
        self.dot.append(np.array(pos))
    def get_dot(self,index):
        return self.dot[index]
    def __str__(self):
        s = ""
        count = 1
        for i in self.dot:
            s += "v" + str(count) + ":" + str(list(i)).replace("[","").replace("]","").replace(" ","") + "\n"
            count += 1
        return s
class EdgeList:
    def __init__(self):
        self.edge = []
        self.patch = None
    def add_edge(self,dot1,dot2):
        self.edge.append(dot2 - dot1)

        #检查是否生成一个面
        if len(self.edge) >= 3:
            result = np.zeros(3)
            edge_list = []
            for i in self.edge:
                result += i
                edge_list.append(i)
                if not result.any():
                    if self.patch == None:
                        self.patch = PatchList()
                    self.patch.add_patch(edge_list)
                    edge_list = []

    def __str__(self):
        s = ""
        count = 1
        for i in self.edge:
            s += "E" + str(count) + ":v" + str(count) + "v" + str(count + 1) + "\n"
            count += 1
        return s
class PatchList:
    def __init__(self):
        self.patch = []
    def add_patch(self,patch):
        self.patch.append(patch)
    def __str__(self):
        count = 1
        s = ""
        for i in self.patch:
            s += "S" + str(count) + ":"
            count1 = 1
            for j in i:
                s += "E" + str(count1)
                count1 += 1
            s += "\n"
        return s
count = 1
dot_list = DotList()
edge_list = EdgeList()

try:
    while True:
        x = [int(i) for i in input().split(",")]
        dot_list.add_dot(x)
        if count >= 2:
            edge_list.add_edge(dot_list.get_dot(count - 2),dot_list.get_dot(count - 1))
        count += 1
except KeyboardInterrupt:
    print(dot_list)
    print(edge_list)
    print(edge_list.patch)