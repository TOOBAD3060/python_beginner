numbers = [4, 17, 4, 3, 22, 3, 5]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)
    
print(unique)