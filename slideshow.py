from helpers import *


listOfInputs = open('a_example.txt', 'r').read().splitlines()

photosNumber = int(listOfInputs[0])
photosList = []

for i in range(photosNumber):
    photo = listOfInputs[i+1].split()
    photosList.append({
        'id': i,
        'direction': photo[0],
        'tags': photo[2:]
    })

# Separating photos into V list and H list
vPhotos = []
hPhotos = []

for i in range(photosNumber):
    if(photosList[i]['direction'] == 'H'):
        hPhotos.append(photosList[i])
    else:
        vPhotos.append(photosList[i])


# Filling slidesList
slidesList = hPhotos[:]


for i in range(0, len(vPhotos)):
    if(i+1 > len(vPhotos)):
        continue
    minSim = Get_Similarity(vPhotos[i], vPhotos[i+1])
    bestCompanionPhoto = vPhotos[i+1]
    bestCompanionPhotoIndex = i+1
    if(len(vPhotos) <= 2):
        slidesList.append({
            'id': str(vPhotos[i]['id']) + ' ' + str(bestCompanionPhoto['id']),
            'direction': 'V',
            'tags': list(dict.fromkeys(vPhotos[i]['tags']+bestCompanionPhoto['tags']))
        }
        )
        break

    for j in range(0, len(vPhotos)):

        currentSim = Get_Similarity(vPhotos[i], vPhotos[j])
        if (currentSim < minSim):
            minSim = currentSim
            bestCompanionPhoto = vPhotos[j]
            bestCompanionPhotoIndex = j
            flag = True

    slidesList.append({
        'id': str(vPhotos[i]['id']) + ' ' + str(bestCompanionPhoto['id']),
        'direction': 'V',
        'tags': list(dict.fromkeys(vPhotos[i]['tags']+bestCompanionPhoto['tags']))
    })

    vPhotos = list(filter(lambda x: x['id'] != vPhotos[i]['id']
                          and x['id'] != bestCompanionPhoto['id'], vPhotos))


def diff_similarity_diff(list1, list2):
    count = 0
    for i in list1:
        if i in list2:
            count = count + 1
    return (len(list1) - count), count, (len(list2) - count)


def Order_slides(L):
    orderedList = []
    for i in range(0, len(L)):
        if L[i] not in orderedList:
            orderedList.append(L[i])
            score = 0
            index = 0
            flag1 = 0
            flag2 = 0
            for j in range(i+1, len(L)):
                flag1 = 1
                diff1, common, diff2 = diff_similarity_diff(
                    L[i]["tags"], L[j]["tags"])
                Min = min(diff1, common, diff2)
                if(Min > score):
                    flag2 = 1
                    score = Min
                    index = j

            if flag1 == 1 and flag2 == 1:
                if L[index] not in orderedList:
                    orderedList.append(L[index])
                #del L[index]
            elif flag1 == 1 and flag2 == 0:
                if L[index] not in orderedList:
                    orderedList.append(L[i+1])
            #del L[index]

    return orderedList


fileresult = open('a_example_ans.txt', 'w')
print(len(Order_slides(slidesList)), file=fileresult)

for i in Order_slides(slidesList):
    print(i['id'], file=fileresult)
