#Indentation and Logic Errors
birds = ["crow","finch","wren"]
for i, bird in enumerate(birds):
    print(f'Bird {i+1}:')
    print(f'     {bird}')
    print()

for i, bird in enumerate(birds):
    print(f'Bird {i+1}:')
    print(f'     {bird}')