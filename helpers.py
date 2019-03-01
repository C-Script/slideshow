def Take_2D_array(rows):
    L=list()
    for i in range(0,rows):
        x=input()
        L.append(x)
    return L


def Get_Similarity(list1, list2):
    count=0
    for i in list1:
        if(i in list2):
            count=count+1
    return count



# print(Get_Difference([2,4,6],[3,6,2,1,10,11,12]))