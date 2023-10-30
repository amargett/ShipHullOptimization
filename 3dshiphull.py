import rhinoscriptsyntax as rs 
import Rhino
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
pt2 = (lb, bwl*1/2, draft)
pt3 = (lb + lm, bwl*1/2, draft)
pt4 = (lb+lm+ls, bs/2, draft)
pt5 = (lb + lm+ ls, 0, draft)

# curve 1
x = (pt1[0] + pt2[0])/2
y = topy_dis_1
new_pt = (x, y, draft)
pivot = (pt2[0]-toppd, pt2[1], draft)
rs.AddCurve([pt1, new_pt, pivot, pt2])

# curve 2
rs.AddLine(pt2, pt3)

# curve 3
x = (pt3[0] + pt4[0])/2
y = pt4[1] + topy_dis_2
new_pt = (x, y, draft)
pivot = (pt3[0]+toppd, pt3[1], draft)
rs.AddCurve([pt3, pivot, new_pt, pt4])

# curve 4
if pt4[1] != pt5[1]:
    rs.AddLine(pt4, pt5)






## parallel midbody
i =lb
curves = []
while i <= lb+lm:
    # points along deck
    pt1 = [i, bwl/2, draft]
    pt2 = [i, 0, draft]

    # intersection point percentages
    isp = (0.95, 0.75) # y percentage, z percentage
    beta = 17 # deadrise angle, in degrees
    is_pt = (i, isp[0]*bwl/2, draft*isp[1]) # intersection point
    R_c = 1 # radius at chine
    R_k = 2.5 # radius at keel

    # finding point at keel
    h = is_pt[2] - depth 
    L = h/math.tan(beta)
    keel_pt = (i, is_pt[1]-L, depth)

    # finding reference curves
    l1 = rs.AddLine(pt1, is_pt)
    l2 = rs.AddLine(keel_pt, is_pt)
    ref_circle  = rs.AddCircle3Pt((i,0,0), keel_pt, (i, R_k*2, 0))
    cc = rs.CircleCenterPoint(ref_circle) # circle center for equation
    rs.ObjectColor([l1,l2, ref_circle], (0, 0, 225))

    # trimming circle
    ccx = rs.CurveCurveIntersection(ref_circle, l2)
    trim_t = ccx[0][5]
    interval = [0, trim_t]
    c1 = rs.TrimCurve(ref_circle, interval)

    # trimming top fillet 
    fillet = rs.AddFilletCurve(l1, l2, R_c) 
    rs.ObjectColor([fillet], (0,0,225))
    inter1 = rs.LineLineIntersection(fillet, l1)
    inter2 = rs.LineLineIntersection(fillet, l2)
    d1 = rs.Distance(inter1[0], is_pt)
    d2 = rs.Distance(inter2[0], is_pt)
    domain1 = rs.CurveDomain(l1)
    domain2 = rs.CurveDomain(l2)
    c2 = rs.TrimCurve(l1, [domain1[1],domain1[1]-d1])
    c3 = rs.TrimCurve(l2, [domain2[1], domain2[1]-d2])
    #curve = rs.JoinCurves([fillet, c1, c2, c3], True)
    #curves.append(curve)
    i+= lm/5
    
#rs.AddLoftSrf(curves)

def bezier_eqn(ctrl_pts):
    """
    input: a list of control points along a bezier curve
    output: a string representing the function of the curve.
    """
    k = length(ctrl_pts) # number of points
    n = num_pts-1 # degree of curve
    

print('keel equation:'+ '(x-'+str(cc[0])+')^2 + (y-' + str(cc[1]) + ')^2 = ' + str(R_k**2))
    
