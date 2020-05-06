def check_score(score):
    return "pass" if score >= 60 else "fail"

max = lambda x, y : x if x > y else y
print("max=", max(70, 20))
print(check_score(max(70, 20)))

bmi = lambda h, w : w / (h/100)**2
print("bmi=", bmi(170, 60))
