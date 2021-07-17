#hello

import itertools



def makegrid(n,m):

    Grid = set()
    for i in range(1,n+1):
        for j in range(1,m+1):
            Grid.add((i,j))
    return Grid


def findsubsets(s, n):

    return list(itertools.combinations(s, n))


def linindtest(v,w):

    if v[0]*w[1]!=w[0]*v[1]:
        return 1
    else:
        return 0


def checkfortriple(set):

    for point1 in set:
        for point2 in set:

            if linindtest(point1,point2)==1:

                sum = (point1[0] + point2[0], point1[1] + point2[1])

                for point3 in set:

                    if sum[0] == point3[0] and sum[1] == point3[1]:
                        return 1

    return 0



Grid = makegrid(2,2)

count = 0

for i in range(0,3):
    for C_1 in findsubsets(Grid,i):

        C_2=tuple(set(Grid).symmetric_difference(C_1))

        if checkfortriple(C_1)==1 or checkfortriple(C_2)==1:
            count=count+1
            print("triple found", count)
        else:
            print(C_1,C_2)
            quit()








































