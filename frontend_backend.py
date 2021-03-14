print("给定平面方程的参数，判断点在平面前方还是后方")
params = [int(x) for x in input("请输入平面方程的参数：").split(",")]
xyz = [int(x) for x in input("请输入点的坐标:").split(",")]
result = params[0]*xyz[0] + params[1]*xyz[1] + params[2]*xyz[2] + params[3]
if result < 0:
    print("在后方")
elif result > 0:
    print("在前方")