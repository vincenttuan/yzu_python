file = open('salary.txt', 'r', encoding='UTF-8')
rows = file.readlines()
print(rows)
# 求總薪資
# 進行資料整理
employees = []
for row in rows:
    data = row.split(", ")
    dict = {'name':data[0], 'salary':int(data[1].strip('\n'))}
    employees.append(dict)

print(employees)

sum = 0
for emp in employees:
    sum = sum + emp['salary']

print(sum)