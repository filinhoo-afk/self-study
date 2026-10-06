# На вход программе подаются натуральное число n, затем n-строк 
# Для каждого комментария программа должна вывести его текст 
# или сообщение «COMMENT SHOULD BE DELETED» (без кавычек), если комментарий должен быть удалён.


n = int(input())
for i in range(1,n+1):
    s = input()
    if s.strip() == '':
        print(f'{i}: COMMENT SHOULD BE DELETED')
    else:
        print(f'{i}: {s}')


