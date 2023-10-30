import rhinoscriptsyntax as rs 
import math

###parameters
bd = 0.7
sdy = 1.2
sdx = 0.6
ypiv1 = -1.2
ypiv2 = 1.3
draft = 3
depth = 1
deadrise = False #False when deadrise is zero, True otherwise
lb = 4
lm = 5
ls = 3
bs = 2
bwl = 5
topy_dis_1 = 1.3
topy_dis_2 = 0.9
toppd = 0.5 # pivot distance
frontpd = 1.2 # pivot distance

lwl = lb + lm + ls


##top view
# set pivot points with given dimensions
pt1 = (0,0,draft)
pt2 = (lb, bwl*-1/2, draft)
pt3 = (lb + lm, bwl*-1/2, draft)
pt4 = (lb+lm+ls, bs*-1/2, draft)
pt5 = (lb + lm+ ls, bs/2, draft)
pt6 = (lb+lm, bwl/2, draft)
pt7 = (lb, bwl/2, draft)

rs.AddNurbsSurface([5,2], [pt1, pt2, pt3, pt4, pt5], [1,1,2,2,3,4,5,6,7], [pt6,pt7], [3,1])


ctrlpts = [pt1, pt2, pt3, pt4, pt6, pt7]

# curve 1
x = (pt1[0] + pt2[0])/2
y = -topy_dis_1
new_pt = (x, y, draft)
pivot = (pt2[0]-toppd, pt2[1], draft)
rs.AddCurve([pt1, new_pt, pivot, pt2])

# curve 2
rs.AddLine(pt2, pt3)

# curve 3
x = (pt3[0] + pt4[0])/2
y = pt4[1] - topy_dis_2
new_pt = (x, y, draft)
pivot = (pt3[0]+toppd, pt3[1], draft)
rs.AddCurve([pt3, pivot, new_pt, pt4])

# curve 4
if pt4[1] != pt5[1]:
    rs.AddLine(pt4, pt5)
    ctrlpts.append(pt5)

# curve 5
y = pt5[1] + topy_dis_2
new_pt = (x, y, draft)
pivot = (pt6[0]+ toppd, pt6[1], draft)
rs.AddCurve([pt5, new_pt, pivot,pt6])

# curve 6
rs.AddLine(pt6, pt7)

# curve 7
x = pt7[0]/2
y = topy_dis_1
new_pt = (x, y, draft)
pivot = (pt7[0]-toppd, pt7[1], draft)
rs.AddCurve([pt1, new_pt, pivot, pt7])


## front view
pt1 = (0, -bwl/2 , draft)
pt2 = (0, bwl/2, draft)

rs.AddLine(pt1, pt2)

if deadrise:
    pt3 = (0, pt1[1], depth)
    pt4 = (0, pt2[1], depth)
    pt5= (0, 0, 0)
    rs.AddLine(pt1, pt3)
    rs.AddLine(pt2, pt4)
    if frontpd == 0: 
        rs.AddLine(pt3, pt5)
        rs.AddLine(pt5, pt4)

    else:
        pt6 = (0, (pt3[1]+ pt5[1])/2 - frontpd, (pt3[2]+pt5[2])/2 -frontpd)
        pt7 = (0, (pt5[1] + pt4[1])/2 + frontpd, (pt5[2] + pt4[2])/2 -frontpd)
        rs.AddArc3Pt(pt3, pt5, pt6)
        rs.AddArc3Pt(pt5, pt4, pt7)
    
else: 
    pt3 = (0, pt1[1], 0)
    pt4 = (0, pt2[1], 0)
    
    piv1 = (0, pt3[1], pt3[2]+frontpd)
    piv2 = (0, pt3[1] + frontpd, pt3[2])
    
    piv3 = (0, pt4[1]-frontpd, pt4[2])
    piv4 = (0, pt4[1], pt4[2]+frontpd)

    
    rs.AddLine(pt1, piv1)
    rs.AddLine(pt2, piv4)
    
    rs.AddCurve([piv1, pt3, piv2])
    rs.AddCurve([piv3, pt4, piv4])
    rs.AddLine(piv2, piv3)
    
    
## side view

pt1 = (0, bwl/2, draft)
pt2 = (lwl, bwl/2, draft)
pt3 = (bd, bwl/2, 0)
pt4 = (lwl-sdx, bwl/2, draft-sdy)

quarter_dist = (pt4[0]-pt3[0])/4
pt5 = (pt3[0]+quarter_dist, pt3[1], pt3[2]+ypiv1)
pt6 = (pt4[0]-quarter_dist, pt4[1], pt3[2]+ypiv2)

rs.AddLine(pt1, pt2)
rs.AddLine(pt1, pt3)
rs.AddLine(pt2, pt4)
rs.AddCurve([pt3,pt5, pt6, pt4])



