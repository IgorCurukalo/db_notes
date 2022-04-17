#Перемешать список

# def perm_lets(s):
#     s = list(s)
#     while True:
#         random.shuffle(s)
#         p = ''.join(str(s))
#         if '  ' in p: continue                            
#         if p.startswith(' ') or p.endswith(' '): continue 
#         if re.search(r'[aeiou]{2}',p): continue           
#         return p


all = [i for i in range(32, 127)] + [i for i in range(1040, 1103)]
# print(all)
# print(perm_lets(all))

# #ключ для проверки
# with open('config.txt', 'r', encoding='utf-8') as file:
#         TOKEN = file.read().strip()
keys = [74, 54, 60, 1096, 64, 1078, 105, 1093, 50, 1099, 1087, 101, 1088, 75, 1083, 1054, 114, 1097, 1073, 119, 1056, 103, 55, 1074, 73, 83, 1077, 1043, 1042, 1059, 66, 81, 42, 53, 1057, 82, 1076, 78, 117, 106, 97, 104, 1091, 1101, 48, 1041, 71, 1098, 41, 109, 86, 100, 1086, 63, 65, 1047, 89, 1051, 1064, 107, 1044, 51, 115, 124, 1040, 58, 80, 1045, 91, 69, 72, 1081, 85, 123, 93, 88, 1069, 40, 1072, 125, 67, 1075, 68, 1071, 59, 98, 1053, 33, 36, 1095, 113, 62, 84, 1090, 1061, 102, 108, 45, 122, 57, 1063, 96, 1066, 1052, 1055, 79, 38, 1068, 44, 1085, 52, 1050, 1049, 1094, 1062, 1084, 34, 90, 56, 1082, 77, 1089, 1079, 1060, 39, 35, 94, 120, 1092, 95, 112, 92, 118, 1100, 110, 1058, 46, 99, 1065, 1048, 49, 1046, 43, 126, 61, 47, 1102, 1070, 76, 70, 1067, 116, 37, 32, 111, 121, 1080, 87]

#соединение двух списков
list_word  = dict(zip(keys, all))
# print(list_word)

#получить значение списка
def get_key(d, value):
    for k, v in d.items():
        if k == value:
            return v

#получить ключ списка
def get_key2(d, value):
    for k, v in d.items():
        if str(v) == str(value):
            return int(k)

#Закодировать
def schifr_on(text,list_word):
    nl = []
    endspisok = []
    for i in text: 
        nl.append(ord(i))
    for i in list(nl):
        endspisok.append(str(get_key(list_word,i)))
    result = ','.join(endspisok)
    return result

#Тест зашифровали
txt = 'Домик72'
print(schifr_on(txt,list_word))

#Раскодировать
def schifr_off(text,list_word):
    result = ''
    listt = text.split(',')
    for i in listt:
        result += ''.join(chr(get_key2(list_word,i)))
    return result

#Тест Расшифровали
txt2 = schifr_on(txt,list_word)
print(schifr_off(txt2,list_word))