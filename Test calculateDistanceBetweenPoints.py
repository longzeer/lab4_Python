from Yong_Shao_library import cDBP

x, y = map(int, input("Please enter the coordinate(integer) of point A, separate by the space bar ").split())
x1, y1 = map(int, input("Please enter the coordinate(integer) of point B, separate by the space bar ").split())
print("The distance between A and B is ", cDBP(x,y,x1,y1))
