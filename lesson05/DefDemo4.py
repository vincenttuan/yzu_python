def my_home(name, *people, **mask):
    print(name)
    print(people)
    print(mask)

my_home('我的家',
        '爸爸', '媽媽', '哥哥', '姊姊',
        成人=100, 孩童=50)