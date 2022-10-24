#Напишите программу, удаляющую из текста все слова, содержащие "абв".

path = r'C:\Users\E5450\Desktop\Homework Python\file.txt'
datatxt=''
with open(path, 'r', encoding= 'utf_8') as file:
    datatxt = file. read()

datatxt=datatxt.split()
print(datatxt) 

findtxt= input('Введите текст для проверки: ')

resulttxt =[]

for word in datatxt:
    if findtxt not in word:
        resulttxt.append(word)
print (resulttxt)       