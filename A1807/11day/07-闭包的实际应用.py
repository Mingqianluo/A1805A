def line_cone(a,b):
    def line(x):
        return a*x+b
    return line

line = line_cone(2,3)
print(line(5))
print(line(6))
print(line(7))
