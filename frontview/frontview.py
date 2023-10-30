import rhinoscriptsyntax as rs 
import math

bwl = 2
draft = 2.5
depth = 1
chine = False
deadrise = False #False when deadrise is zero, True otherwise

pt1 = (0, 0, 0)
pt2 = (bwl, 0, 0)
pt3 = (0, depth-draft, 0)
pt4 = (bwl, depth-draft, 0)
pt5= (bwl/2, pt3[1]-depth, 0)

rs.AddLine(pt1, pt2)
if chine: 
    rs.AddLine(pt1, pt3)
    rs.AddLine(pt2, pt4)
    if deadrise: 
        rs.AddLine(pt3, pt5)
        rs.AddLine(pt5, pt4)
    else:
        pt6 = (pt3[0]+0.3, pt3[1]-0.3, 0)
        pt7 = (pt4[0]-0.3, pt4[1]-0.3, 0)
        rs.AddCurve([pt3, pt6, pt5, pt7, pt4])
else: 
    rs.AddCurve([pt1, pt5, pt2])

        
        

    

