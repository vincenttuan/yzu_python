# -*- coding:UTF-8 -*-
score = 75
print("score", score)
print("score", score, sep="=")
print("score", score, sep=",")
print("score", score, sep="&")

print("a")  # 預設 end="\n"
print("b")  # 預設 end="\n"

print("a", end="")
print("b")  # 預設 end="\n"

print("A", end="")
print("B", end="")
print("C", end="\n")
