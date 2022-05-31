
#Открываем 2 файла в режиме чтения
f1 = open('Text1.txt', 'r')
f2 = open('Text2.txt', 'r')
#Создаем два списка для хранения строк
f1_lines = []
f2_lines = []
#Заполняем списки строками из файлов
for line in f1:
    f1_lines.append(line)
for line in f2:
    f2_lines.append(line)
#Закрываем файлы
f1.close()
f2.close()
#Создаем новый файл на запись
f_res = open('Result.txt', 'w')
#Записываем в него строки из 2х файлов, согласно четности индекса строки(Запись идет построчно)
for i in range(0, max(len(f1_lines), len(f2_lines))):
    if i % 2 == 1: #Если счет начинается с 1, а не с 0, то поменять "==1" на "==0"
        f_res.write(f1_lines[i])
    else:
        f_res.write(f2_lines[i])
#Закрываем файл
f_res.close()

