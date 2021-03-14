
dot = []
print("平面方程计算")
for i in range(3):
    x  = [int(i) for i in input().split(",")]
    dot.append(x)

A = dot[0][1]*(dot[1][2] - dot[2][2]) + dot[1][1]*(dot[2][2] - dot[0][2]) + dot[2][1]*(dot[0][2] - dot[1][2])
B = dot[0][2]*(dot[1][0] - dot[0][2]) + dot[1][2]*(dot[2][0] - dot[0][0]) + dot[2][2]*(dot[0][0] - dot[1][0])
C = dot[0][0]*(dot[1][1] - dot[2][1]) + dot[1][0]*(dot[2][1] - dot[1][1]) + dot[2][0]*(dot[0][1] - dot[1][1])
D = -dot[0][0]*(dot[1][1]*dot[2][2] - dot[2][1]*dot[1][2]) - dot[1][0]*(dot[2][1]*dot[0][1] - dot[0][1]*dot[2][2]) + dot[2][0]*(dot[0][1]*dot[1][2] - dot[1][1]*dot[0][1])
print("%dx + %dy + %dz + %d = 0" % (A,B,C,D))