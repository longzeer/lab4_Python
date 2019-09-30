from Yong_Shao_library import cDBP

a, b = map(int, input("Please enter the coordinate(integer) of point A, separate by the space bar ").split())
a1, b1 = map(int, input("Please enter the coordinate(integer) of point B, separate by the space bar ").split())
print("The distance between A and B is ", cDBP(a,b,a1,b1))
