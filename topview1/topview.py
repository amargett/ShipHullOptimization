import rhinoscriptsyntax as rs 
import random
import math
# parameters = {'lwl': 5, 'lb': 1, 'lm': 3, 'ls': 2, 'bs': 1, 'bwl': 3}
lwl = 5
lb = 1
lm = 3
ls = 2
bs = 1
bwl = 3

bow_quad = True
stern_quad = True

pt1 = (0,0,0)
pt2 = (lb, bwl*-1/2, 0)
pt3 = (lb + lm, bwl*-1/2, 0)
pt4 = (lwl, bs*-1/2, 0)
pt5 = (lb + lm, bwl/2)
pt6 = (lb, bwl/2)

    

if bow_quad: 
    x = (pt1[0] + pt2[0])/2
    # finding quadratic equation from two points
    a = (pt2[1] - pt1[1])/(pt2[0] - pt1[1])**2
    # finding new y of point
    y = a*(x-pt1[0]) + pt1[1]
    x = 0.5
    y = -1.2
    new_pt = (x, y, 0)
    
    print(x)
    print(y)
    rs.AddArc3Pt(pt1, pt2, new_pt)
        