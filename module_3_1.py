def count_calls():
    global calls
    calls += 1
    return f'{calls}'

# 2. string_info принимает аргумент - строку и возвращает кортеж из:
# длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
def string_info(string):

    res = (f'{len(string)},{string.upper()},{string.lower()}')
    res1 = tuple((item) for item in res.split(','))
    count_calls()
    return res1

# 3. is_contains возвращает True, если строка находится в этом списке, False - если отсутствует.
def is_contains(string, list_to_search):
    string = string.lower()
    list_to_search = list(map(str.lower, list_to_search))
    count_calls()
    if string in list_to_search:
        return True
    else:
        return False



calls = 0

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
# print(is_contains('cycle', ['recycle', 'Cycl'])) # No matches
# print(is_contains('banan', ['ban', 'BaNaN', 'eeyyy']))
# print(is_contains('ban', ['ban', 'BaNaN', 'urBAN']))
# print(is_contains('Rec', ['ban', 'BaNaN', 'urBAN', 'reCl']))
print(calls)