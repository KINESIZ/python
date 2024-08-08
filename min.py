dataset = [int(input("input number 1: ")),int(input("input number 2: ")),int(input("input number 3: ")),int(input("input number 4: " )),int(input("input number 5: "))] 
# dataset = [1,2,5,8,9]
if not dataset:
    print("รายการว่างเปล่า")
else:
    print("ข้อมูลมากที่สุด")
    max = dataset[0]
    for x in dataset:
        if x > max:
            max = x
print(max)
