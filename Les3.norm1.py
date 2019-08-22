names = ('ivan', 'vasiliy', 'semen', 'fyodor', 'denis')
maney = (50000, 30000, 500000, 700000, 150000)

file = open('salary.txt', 'w', encoding='utf=8')
for names, maney in zip(names, maney):
    if maney < 500000:
        maney = maney*(1 - 0.13)
        file.write('{0} - {1}\n'.format(names.title(), maney))
file.close()

file = open('salary.txt')
for line in file:
    print(line.strip())