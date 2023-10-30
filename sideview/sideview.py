import rhinoscriptsyntax as rs 
import math

lwl = 7
draft = 1.5
bd = 0.7
sdy = 1.2
sdx = 0.6
ypiv1 = -1.2
ypiv2 = 1.3


pt1 = (0, 0, 0)
pt2 = (lwl, 0, 0)
pt3 = (bd, -draft, 0)
pt4 = (lwl-sdx, -sdy, 0)

quarter_dist = (pt4[0]-pt3[0])/4
pt5 = (pt3[0]+quarter_dist, pt3[1]+ ypiv1, 0)
pt6 = (pt4[0]-quarter_dist, pt3[1] + ypiv2, 0)

rs.AddLine(pt1, pt2)
rs.AddLine(pt1, pt3)
rs.AddLine(pt2, pt4)
rs.AddCurve([pt3,pt5, pt6, pt4])

