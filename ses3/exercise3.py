#Assignment 1
boardOfDirectors = set(('Benny', 'Hans', 'Tine', 'Mille','Torben', 'Troels', 'Søren'))
management = set(('Tine', 'Trunte', 'Rane'))
employees = set(('Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent', 'Rane',
 'Allan', 'Stine', 'Claus', 'James', 'Lars'))

def membersInBothSet(set1, set2):
    result = set()
    for element in set1:
        if element in set2:
            result.add(element)
    return result

def membersNotInBothSet(set1, set2):
    result = set()
    for element in set1:
        if element not in set2:
            result.add(element)
    return result

directorButNotEmployeeList = membersNotInBothSet(boardOfDirectors, employees)
print('Director but not employee: ', directorButNotEmployeeList)

directorAndAlsoEmployeeList = membersInBothSet(boardOfDirectors, employees)
print('Director and also employee: ', directorAndAlsoEmployeeList)

managmentAndAlsoDirectorList = membersInBothSet(management, boardOfDirectors)
print('Manament and also director: ', len(managmentAndAlsoDirectorList))

managmentAndAlsoEmployeeList = membersInBothSet(management, employees)
print('Management and also employee: ', managmentAndAlsoEmployeeList)

print('Mnagement and board: ', managmentAndAlsoDirectorList)

print('Management, board and employee: ', membersInBothSet(membersInBothSet(boardOfDirectors, management), employees))

print('Just employee: ', membersNotInBothSet(membersNotInBothSet(employees, management), boardOfDirectors))


#Assignment 2
listOfTuples = []
dictionary = {'a':'Alpha', 'b':'Beta', 'g': 'Gamma'}

for k,v in dictionary.items():
    listOfTuples.append(tuple((k,v)))

print('From dictionary to list of tuples: ', listOfTuples)


#Assignment 3
setA = {'a', 'e', 'i', 'o', 'u', 'y'}
setB = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

def disjoint(set1,set2):
    disjointSet = set()
    for element in set1:
        for i in set2:
            if element == i:
                disjointSet.add(i)
    return disjointSet

print('Union: ', setA.union(setB))
print('Symmetric difference: ', setA.symmetric_difference(setB))
print('Difference: ', setA.difference(setB))
print('Disjoint: ', disjoint(setB,setA))

#Assignment 4
months = {
    "JAN" : 1,
    "FEB" : 2,
    "MAR" : 3,
    "APR" : 4,
    "MAY" : 5,
    "JUN" : 6,
    "JUL" : 7,
    "AUG" : 8,
    "SEP" : 9,
    "OKT" : 10,
    "NOV" : 11,
    "DEC" : 12
}

def getFormatDate(str):
    splittedDate = str.split('-')
    day = splittedDate[0]
    month = splittedDate[1]
    year = splittedDate[2]

    monthToInt = months[month]

    year = ('19' + year) if int(year) > 21 else ('20' + year)

    return tuple((year,monthToInt, day))


print((getFormatDate('12-MAR-19')))