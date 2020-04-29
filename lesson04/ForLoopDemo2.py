# dict 字典結構
salary = {'John': 50000, 'Mary': 60000}
print(salary)
print(salary['John']) # 取得 John 的薪資
for name in salary:
    print("%s 的薪資 %d" % (name, salary[name]))


