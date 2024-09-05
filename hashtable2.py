data_set =[
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

def hash_function (value) :
    sum_of_char = 0
    for cha in value:
        sum_of_char += ord(cha)
    
    return sum_of_char % 10

def add_function(value) :
    index = hash_function(value)
    data = data_set[index]

    if value not in data :
        data_set[index].append(value)

add_function('banana')
add_function('apple')
add_function('kiwi')
add_function('mango')

print(data_set)

def search_function(value):
    index = hash_function(value)
    data = data_set[index]

    if value in data :
        print('Found')
    else :
        print('Not Found')

search_function('banana')
search_function('apple')
search_function('banan')