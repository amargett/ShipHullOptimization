import rhinoscriptsyntax as rs 
import math

lb = 4
lm = 5
ls = 3
bs = 2
bwl = 6
y_dis_1 = 1.8
y_dis_2 = 0.9
pd = 0.3 # pivot distance


# set pivot points with given dimensions
pt1 = (0,0,0)
pt2 = (lb, bwl*-1/2, 0)
pt3 = (lb + lm, bwl*-1/2, 0)
pt4 = (lb+lm+ls, bs*-1/2, 0)
pt5 = (lb + lm+ ls, bs/2, 0)
pt6 = (lb+lm, bwl/2, 0)
pt7 = (lb, bwl/2, 0)

# curve 1
x = (pt1[0] + pt2[0])/2
y = -y_dis_1
new_pt1 = (x, y, 0)

# find pivots
new_x = pt2[0]- pd
new_x2 = pt3[0]+ pd
new_y = pt2[1] + pd
new_y2 = pt3[1] + pd
pivot1 = (new_x, new_y, 0)
pivot2 = (new_x2, new_y2, 0)

# curve 2
x = (pt3[0] + pt4[0])/2
y = pt4[1] - y_dis_2
new_pt2 = (x, y, 0) 

# curve 3
if pt4[1] != pt5[1]:
    rs.AddLine(pt4, pt5)

# curve 4
y = pt5[1] + y_dis_2
new_pt3 = (x, y, 0)

# find pivots
new_x = pt6[0] + pd
new_x2 = pt7[0] - pd
new_y = pt6[1] - pd
new_y2 = pt7[1] - pd
pivot3 = (new_x, new_y, 0)
pivot4 = (new_x2, new_y2, 0)

# curve 5
x = pt7[0]/2
y = y_dis_1
new_pt4 = (x, y, 0)

    
rs.AddCurve([pt1, new_pt1, pivot1, pt2, pt3, pivot2, new_pt2, pt4])
rs.AddCurve([pt5, new_pt3, pivot3, pt6, pt7, pivot4, new_pt4, pt1])



    

