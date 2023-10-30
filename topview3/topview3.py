import rhinoscriptsyntax as rs 
import math

lb = 4
lm = 5
ls = 3
bs = 2
bwl = 5
y_dis_1 = 1.3
y_dis_2 = 0.9
pd = 0.5 # pivot distance


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
new_pt = (x, y, 0)
pivot = (pt2[0]-pd, pt2[1], 0)
rs.AddCurve([pt1, new_pt, pivot, pt2])

# curve 2
rs.AddLine(pt2, pt3)

# curve 3
x = (pt3[0] + pt4[0])/2
y = pt4[1] - y_dis_2
new_pt = (x, y, 0)
pivot = (pt3[0]+pd, pt3[1], 0)
rs.AddCurve([pt3, pivot, new_pt, pt4])

# curve 4
if pt4[1] != pt5[1]:
    rs.AddLine(pt4, pt5)

# curve 5
y = pt5[1] + y_dis_2
new_pt = (x, y, 0)
pivot = (pt6[0]+pd, pt6[1], 0)
rs.AddCurve([pt5, new_pt, pivot,pt6])

# curve 6
rs.AddLine(pt6, pt7)

# curve 7
x = pt7[0]/2
y = y_dis_1
new_pt = (x, y, 0)
pivot = (pt7[0]-pd, pt7[1], 0)
rs.AddCurve([pt1, new_pt, pivot, pt7])


