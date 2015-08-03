
list1 = []
list2 = []
# open the the input file and seperate two list1 and list2
f = open('input.txt', 'r')
f2 = open('output.txt', 'w')
# append all elements in list1
for ch in iter(lambda: f.read(1), ' '):
    if ch != ',':
        list1.append(ch)
print "List1 elements are\n" , list1

# append elements in list2
for ch in iter(lambda: f.read(1), ' '):
    if ch != ',':
        list2.append(ch)
# f2.write(ch)
print "List2 elements are\n", list2

# seperate the element from the file for which predecessor need to be searched
temp = []
n = 1
assert n > 0
for ch in iter(lambda: f.read(n), ''):
    # if ch != ',' : 
        temp.append(ch)
print  "element from 1st list and element from 2nd list respectively given :\n", temp[1] , temp[3]


# create dictionary and insert the elements with index
def enumdict(listed):
    myDict = {}
    for i, x in enumerate(listed):
        myDict[x] = i

    return myDict

d1 = {}
d2 = {}
d1 = enumdict(list1)
d2 = enumdict(list2)
# print"element  which is before the given:"

l1 = []    

for item in d2.keys():
    if item in d1.keys():
        l1.append(d2[item])
        pos = max(l1)
        print pos
    else:
         None

for element, i in d2.items():
    if element == temp[3]:
        pos1 = i
        
for element, j in d1.items():
    if element == temp[1]:
        pos2 = j


def common_predecessor(pos1, pos2, pos):
    if pos1 and pos2 > pos:
        return pos
    elif pos1 == pos2 and pos2 < pos:
        return pos1
    else:
        None 
    
value = common_predecessor(pos1, pos2, pos)


for name, i in d2.items():
    if i == value:
        print "common predecessor:" , name
        f2.write("\ncommon predecessor:")
        f2.write(name)
    else:
        None
f.close()
f2.close()
