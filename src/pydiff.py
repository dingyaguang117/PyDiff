#coding=utf-8
#2013-11-21
__author__ = 'ding'

import sys

def equal(line1,line2):
    return line1 == line2



class node():
    def __init__(self):
        self.val = 0
        self.pre_i = 0
        self.pre_j = 0

    def __repr__(self):
        return '%s,%s,%s'%(self.val,self.pre_i,self.pre_j)

class result_node():
    def __init__(self):
        self.val = None
        self.status = -1


def __printDp(dp):
    for row in dp:
        for col in row:
            print col,
        print


def calc(a,b,dp):
    i,j = len(a)-1,len(b)-1
    result = []
    while i!=0 or j!=0:
        node = result_node()
        if dp[i][j].pre_i != i and dp[i][j].pre_j != j:
            node.val = a[i]
            node.status = 0
        elif dp[i][j].pre_i != i:
            node.val = a[i]
            node.status = -1
        elif dp[i][j].pre_j != j:
            node.val = b[j]
            node.status = 1
        i,j = dp[i][j].pre_i,dp[i][j].pre_j
        result.append(node)

    result.reverse()
    return result

def diff(a,b):
    lines1 = [None] + a.split('\n')
    lines2 = [None] + b.split('\n')
    #print lines1
    #print lines2
    dp = [[node() for i in xrange(len(lines2))] for j in xrange(len(lines1))]
    #__printDp(dp)

    dp[0][0].val = 0
    #__printDp(dp)
    for i in xrange(len(lines1)): dp[i][0].val=i;dp[i][0].pre_i=i-1
    for j in xrange(len(lines2)): dp[0][j].val=j;dp[0][j].pre_j=j-1

    for i in xrange(1,len(lines1)):
        for j in xrange(1,len(lines2)):
            ni = dp[i][j-1].val + 1 # 即 a[i] -1
            nj = dp[i-1][j].val + 1 # 即 b[j] +1
            if equal(lines1[i],lines2[j]):
                nij = dp[i-1][j-1].val + 1 #即不增不减
            else:
                nij = sys.maxsize
            minv = min(ni,nj,nij)
            dp[i][j].val = minv
            if minv == nij:
                dp[i][j].pre_i = i-1
                dp[i][j].pre_j = j-1
            elif minv == ni:
                dp[i][j].pre_i = i
                dp[i][j].pre_j = j-1
            elif minv == nj:
                dp[i][j].pre_i = i-1
                dp[i][j].pre_j = j

    #__printDp(dp)
    result = calc(lines1,lines2,dp)
    return result

