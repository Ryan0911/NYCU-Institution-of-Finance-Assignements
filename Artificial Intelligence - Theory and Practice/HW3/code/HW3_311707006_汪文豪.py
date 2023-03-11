import math
from sklearn import datasets
import numpy as np


def entropy(p1, n1):
    if(p1 == 0 and n1 == 0):
        return 1
    elif (p1 == 0 or n1 == 0):  # 完全歸類 完全不亂
        return 0
    else:
        pp = p1/(p1+n1)
        np = n1/(p1+n1)
        return -pp*math.log2(pp) - np*math.log2(np)


def InformationGain(p1, n1, p2, n2):  # 2個node 1 & 0 binary classification, 越高代表切的越細越好
    num1 = p1+n1  # 掉在1的數量
    num2 = p2+n2  # 掉在2的數量
    num = num1+num2  # 總數量
    #根節點的亂度 - 節點1的亂度
    return entropy(p1+p2, n1+n2) - (num1/num*entropy(p1, n1)+num2/num*entropy(p2, n2))


def ID3DTtrain(feature, target):
    node = dict()
    node['data'] = range(len(target))  # root initialization
    tree = []
    tree.append(node)
    t = 0
    while(t < len(tree)):
        idx = tree[t]['data']
        if(sum(target[idx]) == 0):
            tree[t]['leaf'] = 1
            tree[t]['decision'] = 0
        elif(sum(target[idx]) == len(idx)):  # 都是1 加起來就是長度
            tree[t]['leaf'] = 1
            tree[t]['decision'] = 1
        else:
            bestIG = 0
            for i in range(feature.shape[1]):  # TRY每個特徵切區塊
                pool = list(set(feature[idx, i]))
                pool.sort()
                for j in range(len(pool)-1):
                    thres = (pool[j] + pool[j+1])/2
                    G1 = []
                    G2 = []
                    for k in idx:
                        if(feature[k][i] < thres):
                            G1.append(k)
                        else:
                            G2.append(k)
                    p1 = sum(target[G1] == 1)
                    n1 = sum(target[G1] == 0)
                    p2 = sum(target[G2] == 1)
                    n2 = sum(target[G2] == 0)
                    thisIG = InformationGain(p1, n1, p2, n2)
                    if(thisIG > bestIG):
                        bestIG = thisIG
                        bestG1 = G1
                        bestG2 = G2
                        bestThres = thres
                        bestFeature = i
            if(bestIG > 0):
                tree[t]['leaf'] = 0
                tree[t]['selectf'] = bestFeature
                tree[t]['threshold'] = bestThres
                tree[t]['child'] = [len(tree), len(tree) + 1]
                node = dict()
                node['data'] = bestG1
                tree.append(node)
                node = dict()
                node['data'] = bestG2
                tree.append(node)
            else:
                tree[t]['leaf'] = 1
                if(sum(target[idx] == 1) > sum(target[idx] == 0)):
                    tree[t]['decision'] = 1
                else:
                    tree[t]['decision'] = 0
        t += 1
    return tree


def ID3DTtest(tree, feature1):
    now = 0
    while(tree[now]['leaf'] == 0):
        bestf = tree[now]['selectf']
        thres = tree[now]['threshold']
        if(feature1[bestf] < thres):
            now = tree[now]['child'][0]
        else:
            now = tree[now]['child'][1]
    return tree[now]['decision']


data = datasets.load_iris()
feature = data['data']
target = data['target']

# 第三題
T = ID3DTtrain(feature[50:150, :], target[50:150]-1)
error = 0
for i in range(50, 150):
    if(ID3DTtest(T, feature[i, :]) != (target[i]-1)):
        print("Predit: ", ID3DTtest(T, feature[i, :]), "\nReal: ", target[i])
        error += 1
print("正確率: ", (100-error)/100)

# 第四題
########################################################################
train_data = np.concatenate((feature[50:80, :], feature[100:130, :]))  #
train_target = np.concatenate((target[50:80] - 1, target[100:130] - 1))
########################################################################
test_data = np.concatenate((feature[80:100, :], feature[130:150, :]))  #
test_target = np.concatenate((target[80:100] - 1, target[130:150] - 1))
########################################################################
T4 = ID3DTtrain(train_data, train_target)

error_4 = 0
for i in range(0, 40):
    if(ID3DTtest(T4, test_data[i, :]) != (test_target[i])):
        print("Predit: ", ID3DTtest(
            T4, test_data[i, :]), "\nReal: ", test_target[i])
        error_4 += 1
print("正確率: ", (40-error_4)/40)
