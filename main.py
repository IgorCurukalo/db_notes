from datetime import datetime
import os
import json
from data.schifr_on_off import schifr_on, schifr_off, list_word

#Начало программы
def main():
    while True:
        temp = False
        temp2 = False
        choice = str(input('БД Заметки\n1. Вход\n2. Регистрация\n3. Выход\n\nВаш выбор:'))
        if choice == '1':
            os.system('cls||clear')
            while temp == False:
                if chek_user(user(choice)) == 'Yes':
                    temp == True
                    menu_notes()    
                else:
                    temp == False
        elif choice == '2':
            os.system('cls||clear')
            while temp2 == False:
                if chek_user_new(user(choice)) == 'No':
                    temp2 = False
                else:
                    temp2 = True
                    main()
        elif choice == '3':
            return False
        else:
            main()

#Ввод данных пользователя
def user(n):
    if n == '2':
        print('Регистрация пользователя\n')
    else:
        print('Вход пользователя:\n')
    name_user = input('Введите Имя пользователя: ')
    global us
    us = name_user
    pas = schifr_on(input('Введите пароль: '),list_word)
    os.system('cls||clear')
    print(f'Создали нового пользовтеля: {name_user}\n')
    return [name_user,pas]

#Проверка пользователя при входе
def chek_user(text):
    list_user = read_file('data\logpas.txt')
    if list_user == '':
        os.system('cls||clear')
        print('Список пользователей пустой')
        main()
    else:
        list_user = list_user.split('\n')
        for i in range(len(list_user)):
            if f'{list_user[i]}' == f'{text}':
                return 'Yes'
        os.system('cls||clear')
        print('Вы ввели не верно логин и пароль')
        return 'No' 

#Проверка при создании нового пользователя
def chek_user_new(text):
    list_user = read_file('data\logpas.txt')
    if list_user == '':
        write_to_file('data\logpas.txt',text)
        return 'Yes'
    else:
        list_user = list_user.split('\n')
        for i in range(len(list_user)):
            if f'{list_user[i]}' == f'{text}':
                os.system('cls||clear')
                print('Такой пользователь уже есть, попробуйте сново.')
                return 'No'
        write_to_file('data\logpas.txt',text)
        return 'Yes'   
      
#запись в файл
def write_to_file(file,text):
    with open(file, 'a+', encoding='utf-8') as new_user:
                new_user.write(f'{text}\n')
                new_user.close

#Чтение из файла
def read_file(file):
    with open(file, 'r', encoding='utf-8') as new_user:
        list_user = new_user.read()
        new_user.close
    return list_user

#Меню заметки
def menu_notes():
    while True:
        os.system('cls||clear')
        choice = str(input('БД Заметки\n1. Просмотр заметок\n2. Новая заметка\n3. Выход\n\nВаш выбор:'))
        if choice == '1':
            os.system('cls||clear')
            print('Заметки:')
            open_notes()
        if choice == '2':
            write_to_file(f'data\notes\{us}.txt',new_zametka())
        if choice == '3':
            os.system('cls||clear')
            main()

#Просмотр заметок: отсортированный по названию и дате, поиск по названию
def open_notes():
    os.system('cls||clear')
    choice = str(input('БД Заметки\n1. Отсортированные по названию\n2. Отсортированные по дате\n3. Поиск заметки по названию\n4. Выход\n\nВаш выбор:'))
    if choice == '1':
        Sorted_value('Заметка') 
    elif choice == '2':
        Sorted_value('Дата')
    elif choice == '3':
        Fild_name()
    elif choice == '4':
        menu_notes()
    else:
        open_notes()

#Новая заметка
def new_zametka():
    os.system('cls||clear')
    print('Создать заметку:\n')
    return schifr_on('{'+f'"Заметка":"{input("Название заметки: ")}", "Текст заметки":"{input("Текст заметки: ")}", "Дата":"{datetime.now().strftime("%d.%m.%Y")}"'+'}',list_word)

#Сортировка по дате и названию
def Sorted_value(text_value):
    os.system('cls||clear')
    print(f'Просмотр заметок с сортировкой по: {text_value}\n')
    list_z = read_file(f'data\notes\{us}.txt').split('\n')
    list_spisok = []
    for i in list_z:
        if i != '':
            list_reload = json.loads(schifr_off(i,list_word))
            list_spisok.append(list_reload)
    list_spisok = sorted(list_spisok, key=lambda d: d[text_value])
    for i in list_spisok:
        print('Заметка: '+i['Заметка']+'\nТекст заметки: '+i['Текст заметки']+'\nДата: '+i['Дата']+'\n')
    if input(f"1. Выход\n") == '1':
        open_notes()
    else:
        Sorted_value()

#Поиск по названию заметки
def Fild_name():
    os.system('cls||clear')
    print('Поиск по названию заметки\n')
    f = input("Введите текст, для поиска: ")
    list_z = read_file(f'data\notes\{us}.txt').split('\n')
    list_spisok = []
    for i in list_z:
        if i != '':
            list_reload = json.loads(schifr_off(i,list_word))
            list_spisok.append(list_reload)
    kol = 0
    for i in list_spisok:    
        # if i['Заметка'] == f:
        words = f.split(' ')
        kol_words = 0
        for s in words:
            if i['Заметка'].lower().find(s.lower()) != -1:
                kol_words += 1
                # break
        if kol_words == len(words):
            kol += 1
            print('Заметка: '+i['Заметка']+'\nТекст заметки: '+i['Текст заметки']+'\nДата: '+i['Дата']+'\n')  
    print(f'Найдено заметок, количество: {kol}\n') 
    if input(f"1. Выход\n") == '1':
        open_notes()
    else:
        Fild_name()          

if __name__ == "__main__":
    main()