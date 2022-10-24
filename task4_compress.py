
with open("RLE_input1.txt", 'r', encoding='utf_8') as file:
    s = (list(file. read()))




list = []
li = []
count = 1
for i in s:
    list.append(i)
i = 0
while i < (len(list)-1):
    if list[i] == list[i+1]:
        count += 1
    else:
        li.append(str(count) + str(list[i]))
        count = 1
    i += 1
else: li.append(str(count) + str(list[i]))

a = ''.join(li)

print(a)


with open('RLE_output1.txt', 'w', encoding='utf8') as file:
    file.write(a)

 