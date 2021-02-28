"""
Даны две строки. Выведите на экран символы, которые есть в обоих строках.
"""
str1 = 'This is the text'
str2 = 'Write some text, it is very simply'
s1 = set(str1)
s2 = set(str2)

s1.intersection_update(s2)
print(s1)
