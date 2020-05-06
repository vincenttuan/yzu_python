# 利用 lambda 製作出 switch 的運行邏輯
sex = 1
{
    1:lambda :print('男'),
    2:lambda :print('女')
}.get(sex, lambda :print('錯誤'))()

sex_info = {1:lambda x :print('男', x), 2:lambda x :print('女', x)}
sex_info.get(1)(20)