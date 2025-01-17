'''
Вовочка подготовил одно очень важное письмо, но везде указал неправильное время. 
Поэтому нужно заменить все вхождения времени на строку (TBD). 
Время — это строка вида HH:MM:SS или HH:MM, в которой HH — число от 00 до 23, а MM и SS — число от 00 до 59. 
(ВВОД: Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю. 
ВЫВОД: Уважаемые! Если вы к (TBD) не вернёте чемодан, то уже в (TBD) я за себя не отвечаю. )
'''

import re

text = str(input("Введите текст с указанием времени:"))
repltime = r'\b\d{2}:\d{2}(:\d{2})?\b'
newtext = re.sub(repltime, '(TBD)', text)
print(newtext)

'''
Владимир устроился на работу в одно очень важное место. 
И в первом же документе он ничего не понял, там были сплошные ФГУП НИЦ ГИДГЕО, ФГОУ ЧШУ АПК и т.п. 
Тогда он решил собрать все аббревиатуры, чтобы потом найти их расшифровки на http://sokr.ru/. 
Помогите ему. 
Будем считать аббревиатурой слова только лишь из заглавных букв (как минимум из двух). 
Если несколько таких слов разделены пробелами, то они считаются одной аббревиатурой.
'''

import re
d = str(input("Введите текст с аббревиатурами:"))
A = re.findall('[А-Я]{2,}', d)
print(*A)


