#with open("RLE_input2.txt", 'r', encoding='utf_8') as file:
#    l = (file. read())

#print(l)

l='11a3b7c'   # если принудительно присваивать - работает.  А из файла берет с ошибкой - не понятно.
r=''
result=''
for i in l:
    if i.isdigit():
        r+=i
    else:
        r = int(r)
        while r > 0:
            r-=1
            result+=i
        else:
            r=''



print(result)
with open('RLE_output2.txt', 'w', encoding='utf8') as file:
    file.write(result)
