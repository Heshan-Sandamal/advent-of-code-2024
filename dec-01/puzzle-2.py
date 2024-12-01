file = open("input.txt")
lines = file.read().splitlines()

total = 0
list1 , map2 = [] , {}
for text in lines:
    values = text.split("   ")
    a, b = int(values[0]), int(values[1])
    list1.append(a)

    if(b in map2):
        map2[b] = map2[b] + 1
    else:
        map2[b] = 1

# calculate similarity
distance = 0
for x in list1:
    if(x in map2):
        val = map2[x]
        distance += (x * val)

print(distance)



