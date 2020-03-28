import statistics
text = input("Zadaj text: ")
array = []
array.append(text)

stringe = ''

for i in array[0]:
    if i == 'A':
        stringe += '1'
    if i == 'B':
        stringe += '11'
    if i == 'C':
        stringe += '111'
    if i == 'D':
        stringe += '2'
    if i == 'E':
        stringe += '22'
    if i == 'F':
        stringe += '222'
    if i == 'G':
        stringe += '3'
    if i == 'H':
        stringe += '33'
    if i == 'I':
        stringe += '333'
    if i == 'J':
        stringe += '4'
    if i == 'K':
        stringe += '44'
    if i == 'L':
        stringe += '444'
    if i == 'M':
        stringe += '5'
    if i == 'N':
        stringe += '55'
    if i == 'O':
        stringe += '555'
    if i == 'P':
        stringe += '6'
    if i == 'Q':
        stringe += '66'
    if i == 'R':
        stringe += '666'
    if i == 'S':
        stringe += '7'
    if i == 'T':
        stringe += '77'
    if i == 'U':
        stringe += '777'
    if i == 'V':
        stringe += '8'
    if i == 'W':
        stringe += '88'
    if i == 'X':
        stringe += '888'
    if i == 'Y':
        stringe += '9'
    if i == 'Z':
        stringe += '99'
    if i == ' ':
        stringe += '0'
print(stringe)

print(statistics.mode(stringe))
