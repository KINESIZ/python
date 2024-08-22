def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = int(input("ใส่อุณหภูมิ : "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius} องศาเซลเซียส เท่ากับ {fahrenheit} องศาฟาเรนไฮต์")