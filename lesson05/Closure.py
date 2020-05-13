def make(n):
    def mult(x):
        return n * x
    return mult

m3 = make(3)
m5 = make(5)

print(m3(6))
print(m3(m5(6)))


