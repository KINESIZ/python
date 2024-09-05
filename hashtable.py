data = [None,None,None,None,None,None,None,None,None,None,None]

def hash_function (value,a = 11,i = 5):
    sum_of_char = 0
    for char in value:
        print(ord(char))
        sum_of_char += ord(char) * (a + i)
    print(sum_of_char)
    index = sum_of_char % 10
    print(index)

    # เพิ่มข้อมูลลง hash table (array)
    data[index] = value

hash_function('PEACE')
hash_function('FIAT')
hash_function('FIW')
hash_function('KLA')
print(data)