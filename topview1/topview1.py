import rhinoscriptsyntax as rs 
import math

lb = 4
lm = 5
ls = 3
bs = 0
bwl = 5
y_dis_1 = 0.7
y_dis_2 = 1.7


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
rs.AddArc3Pt(pt1, pt2, new_pt)

# curve 2
rs.AddLine(pt2, pt3)

# curve 3
x = (pt3[0] + pt4[0])/2
y = pt4[1] - y_dis_2
new_pt = (x, y, 0)
rs.AddArc3Pt(pt3, pt4, new_pt) 

# curve 4
if pt4[1] != pt5[1]:
    rs.AddLine(pt4, pt5)

# curve 5
y = pt5[1] + y_dis_2
new_pt = (x, y, 0)
rs.AddArc3Pt(pt5, pt6, new_pt)

# curve 6
rs.AddLine(pt6, pt7)

# curve 7
x = pt7[0]/2
y = y_dis_1
new_pt = (x, y, 0)
rs.AddArc3Pt(pt1, pt7, new_pt)



