import math
from heapq import*

def test():
    lst=['Case1.txt','Case2.txt','Case3.txt']
    for i in lst:
        print('Length and Path for {}'.format(i))
        print(Dijkstra(i))
        
def read_file(File):
    infile = open(File, "r")
    fname = infile.read()
    strings = fname.split('\n')
    lst = []

    points = int(strings.pop(0))
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for i in strings:
        if i!= '':
            i = i.split(' ')
            temp = temp.split(' ')
    temp = (alph.index(element[0]), alph.index(i[1]), int(i[2]))
    lst.append(temp)
    getFile.close()
    edge = sorted(lst, key = lambda x:x[0])
    return points, edge

def Dijkstra(File):
    points, edge = read_file(File)
    contents = [[0, None]]
    this = [(0,0)]
    for i in range(1, points):
        content.append([math.inf, None])
        pushStuff(this,(i,math.inf))
    while this != []:
        u = pushStuff(this)[0]
        for i in edge:
            if i[0] == u:
                v = i[1]
                These = contents[u][0]+i[2]
                if these < contents[v][0]:
                    contents[v] = [these, u]
                    pushstuff(this, (v, these))
        array=[]
        alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        n = 1
        while contents[n][1]!=None:
            array.insert(0, alph[i])
            n = contents[n][1]
        array.insert(0, 'A')
        return contents[1][0], path
    
    
