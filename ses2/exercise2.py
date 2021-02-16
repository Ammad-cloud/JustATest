a = ['Hello', 'World', 'Huston', 'we', 'are', 'here'];
print('before slice: ', a)
print('after slice: ', a[1:5])

print('before slice: ', a)
print('after slice: ', a[:2])

print('before slice: ', a)
print('after slice: ', a[-2:])

print('before slice: ', a)
print('after slice: ', a[-2:-1])

print('before slice: ', a)
print('after slice: ', a[::2])

print('before slice: ', a)
print('after slice: ', a[::-1])

t = ('Hello', 'World', 'Huston', 'we', 'are', 'here')
print('before slice on tuple: ', t)
newList = list(t[1:5])
print('after slice and convertion: ', newList)

string = ' Hello World Huston we are here'
print('before slice of string: ', string)
extractedWords = string.split()[1:4];
print('after extraction: ', extractedWords)

def removeVowelsAndSortByConsonant(string):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for c in string.lower():
        if c in vowels:
            string = string.replace(c, '')
    return list(sorted(string.split()))

print(removeVowelsAndSortByConsonant('hey my guy'))


i = ['zeze','claus', 'ib', 'per']
print('before sort', i)
print('after sort', sorted(i))

print('reversed', sorted(i, reverse=True))

print(sorted(i, key=len))

def lastChar(word):
    return word[::-1]

print(sorted(i, key=lastChar))

f = open('songs.docx')
print('by read()')
print(f.read())

f = open('songs.docx')
print('by readline() x3')
print(f.readline())
print(f.readline())
print(f.readline())


f = open('songs.docx')
print('by readlines()')
print(f.readlines())

listToSort = [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]

#def secondIndex(tuple):
#    return tuple[1]

print(sorted(listToSort, key=lambda x: x[1])) #Not working yet.

