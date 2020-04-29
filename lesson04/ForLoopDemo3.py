e1 = {'name': 'John', 'salary': 50000}
e2 = {'name': 'Mary', 'salary': 60000}
e3 = {'name': 'Bob', 'salary': 70000}
emps = [e1, e2, e3]
print(emps)
# 求薪資總和 ?
sum = 0
for emp in emps:
    sum = sum + emp['salary']
print(sum)

salary = []  # 建立一個 salary 的數組
for emp in emps:
    salary.append(emp['salary'])  # 將 salary內容 放入數組中
print(salary)
print(max(salary))  # 求最大值
print(min(salary))  # 求最小值
