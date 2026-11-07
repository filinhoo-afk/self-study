# Написать функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2.
# Функция должна возвращать значение True, если слова имеют одинаковую длину и отличаются одним символом на одной и той же позиции, или False в противном случае.


def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False
    diff = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff += 1
    return diff == 1

txt1 = input()
txt2 = input()
print(is_one_away(txt1, txt2))