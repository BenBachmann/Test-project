# print multiplication table

number = int(input("number: "))

# create list of numbers according to user input
ls = []
for i in range(1, number+1):
    ls.append(i)

# create dictionary- each item in ls should map to a list ie. should be {1: [1], 2: [2, 4], 3: [3, 6, 9]...
m_table = {}
for i in ls:
    list = []
    for j in ls:
        list.append(i*j)
    m_table[i] = list

print(m_table)