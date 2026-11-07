# Написать функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text, состоящую из символов ( и ) и возвращает значение True. 
# Если поступившая на вход строка является правильной скобочной последовательностью, или False в противном случае.


def is_correct_bracket(text):
    balance = 0
    for c in text:
        if c == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False
    return balance == 0

txt = input()
print(is_correct_bracket(txt))