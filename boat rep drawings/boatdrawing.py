import rhinoscriptsyntax as rs 
import math


Design_Vec = [43.215, -8.55, 0.0, 8.464500000000001, 8.464500000000001, 1.6666666666666667, 496567.5349583333, 74.25150000000001, -8.017769627840144, 0.0, 8.464500000000001, 8.464500000000001, 1.6666666666666667, 993135.0699166666, 46.036500000000004, -0.08549999999999969, 3.3333333333333335, 8.464500000000001, 8.464500000000001, 1.6666666666666667, 1489702.604875, 65.787, -7.150535665135747, 0.0, 8.464500000000001, 8.464500000000001, 1.25, 496567.5349583333, 91.18050000000001, -1.0027399656241736, 3.3333333333333335, 8.464500000000001, 8.464500000000001, 1.25, 993135.0699166666, 40.3935, -0.08549999999999969, 10.0, 8.464500000000001, 8.464500000000001, 1.25, 1489702.604875, 15.0, -0.08549999999999969, 3.3333333333333335, 8.464500000000001, 8.464500000000001, 0.8333333333333334, 496567.5349583333, 15.0, -8.55, 3.3333333333333335, 8.464500000000001, 8.464500000000001, 0.8333333333333334, 993135.0699166666, 34.7505, -8.55, 6.666666666666667, 8.464500000000001, 8.464500000000001, 0.8333333333333334, 1489702.604875, 82.71600000000001, -8.55, 0.0, 5.643000000000001, 8.464500000000001, 1.6666666666666667, 496567.5349583333, 57.322500000000005, -0.08549999999999969, 10.0, 8.464500000000001, 5.643000000000001, 1.6666666666666667, 993135.0699166666, 46.036500000000004, -8.55, 10.0, 5.643000000000001, 8.464500000000001, 1.6666666666666667, 1489702.604875, 34.7505, -0.08549999999999969, 10.0, 5.643000000000001, 8.464500000000001, 1.25, 496567.5349583333, 79.89450000000001, -8.549730221947279, 10.0, 5.643000000000001, 8.464500000000001, 1.25, 993135.0699166666, 74.25150000000001, -7.474511706972994, 6.666666666666667, 8.464500000000001, 5.643000000000001, 1.25, 1489702.604875, 15.0, -8.47457380461441, 6.666666666666667, 8.464500000000001, 5.643000000000001, 0.8333333333333334, 496567.5349583333, 37.572, -0.08549999999999969, 6.666666666666667, 5.643000000000001, 8.464500000000001, 0.8333333333333334, 993135.0699166666, 74.25150000000001, -3.684748275925954, 3.3333333333333335, 8.464500000000001, 5.643000000000001, 0.8333333333333334, 1489702.604875, 57.322500000000005, -8.55, 6.666666666666667, 2.8215000000000003, 8.464500000000001, 1.6666666666666667, 496567.5349583333, 65.787, -4.442197592141254, 6.666666666666667, 8.464500000000001, 2.8215000000000003, 1.6666666666666667, 993135.0699166666, 23.4645, -3.90641856868448, 6.666666666666667, 8.464500000000001, 2.8215000000000003, 1.6666666666666667, 1489702.604875, 40.3935, -8.55, 3.3333333333333335, 2.8215000000000003, 8.464500000000001, 1.25, 496567.5349583333, 44.71823105000328, -0.08549999999999969, 6.666666666666667, 2.8215000000000003, 8.464500000000001, 1.25, 993135.0699166666, 15.0, -0.08549999999999969, 10.0, 2.8215000000000003, 8.464500000000001, 1.25, 1489702.604875, 23.4645, -8.55, 6.666666666666667, 8.464500000000001, 2.8215000000000003, 0.8333333333333334, 496567.5349583333, 96.82350000000001, -4.811845440329152, 0.0, 2.8215000000000003, 8.464500000000001, 0.8333333333333334, 993135.0699166666, 57.322500000000005, -8.55, 10.0, 2.8215000000000003, 8.464500000000001, 0.8333333333333334, 1489702.604875, 91.18050000000001, -8.548572467182128, 6.666666666666667, 5.643000000000001, 8.464500000000001, 1.6666666666666667, 496567.5349583333, 82.71600000000001, 0.5308332143693558, 6.666666666666667, 8.464500000000001, 5.643000000000001, 1.6666666666666667, 993135.0699166666, 46.036500000000004, -8.55, 3.3333333333333335, 5.643000000000001, 8.464500000000001, 1.6666666666666667, 1489702.604875, 48.858000000000004, -0.08549999999999969, 10.0, 8.464500000000001, 5.643000000000001, 1.25, 496567.5349583333, 65.787, -7.104389261050564, 3.3333333333333335, 5.643000000000001, 8.464500000000001, 1.25, 993135.0699166666, 29.1075, -0.078646640168065, 6.666666666666667, 5.643000000000001, 8.464500000000001, 1.25, 1489702.604875, 48.858000000000004, -8.55, 6.666666666666667, 8.464500000000001, 5.643000000000001, 0.8333333333333334, 496567.5349583333, 29.1075, -0.08549999999999969, 0.0, 8.464500000000001, 5.643000000000001, 0.8333333333333334, 993135.0699166666, 23.4645, -8.55, 10.0, 8.464500000000001, 5.643000000000001, 0.8333333333333334, 1489702.604875, 91.18050000000001, -4.834864177507248, 0.0, 5.643000000000001, 5.643000000000001, 1.6666666666666667, 496567.5349583333, 31.929000000000002, -8.55, 10.0, 5.643000000000001, 5.643000000000001, 1.6666666666666667, 993135.0699166666, 60.144000000000005, -8.55, 3.3333333333333335, 5.643000000000001, 5.643000000000001, 1.6666666666666667, 1489702.604875, 88.35900000000001, -8.55, 10.0, 5.643000000000001, 5.643000000000001, 1.25, 496567.5349583333, 15.0, -0.08549999999999969, 6.666666666666667, 5.643000000000001, 5.643000000000001, 1.25, 993135.0699166666, 29.1075, -0.04723337496078514, 10.0, 5.643000000000001, 5.643000000000001, 1.25, 1489702.604875, 23.4645, -0.11060436745337814, 6.666666666666667, 5.643000000000001, 5.643000000000001, 0.8333333333333334, 496567.5349583333, 57.322500000000005, 0.35535641785996097, 0.0, 5.643000000000001, 5.643000000000001, 0.8333333333333334, 993135.0699166666, 23.4645, -0.08480054937211375, 3.3333333333333335, 5.643000000000001, 5.643000000000001, 0.8333333333333334, 1489702.604875, 15.0, -8.55, 0.0, 2.8215000000000003, 5.643000000000001, 1.6666666666666667, 496567.5349583333, 26.286, 0.6058686807202782, 0.0, 2.8215000000000003, 5.643000000000001, 1.6666666666666667, 993135.0699166666, 34.7505, -3.050271095184538, 0.0, 5.643000000000001, 2.8215000000000003, 1.6666666666666667, 1489702.604875, 43.215, -8.492057582394553, 6.666666666666667, 2.8215000000000003, 5.643000000000001, 1.25, 496567.5349583333, 31.929000000000002, -8.55, 6.666666666666667, 2.8215000000000003, 5.643000000000001, 1.25, 993135.0699166666, 20.747541856779655, -0.08549999999999969, 0.0, 2.8215000000000003, 5.643000000000001, 1.25, 1489702.604875, 20.643, -0.08549999999999969, 6.666666666666667, 2.8215000000000003, 5.643000000000001, 0.8333333333333334, 496567.5349583333, 74.25150000000001, -8.55, 10.0, 2.8215000000000003, 5.643000000000001, 0.8333333333333334, 993135.0699166666, 31.929000000000002, -8.511446221016435, 0.0, 2.8215000000000003, 5.643000000000001, 0.8333333333333334, 1489702.604875, 82.71600000000001, -5.854058168592957, 3.3333333333333335, 8.464500000000001, 2.8215000000000003, 1.6666666666666667, 496567.5349583333, 20.643, -8.55, 0.0, 2.8215000000000003, 8.464500000000001, 1.6666666666666667, 993135.0699166666, 65.787, -3.467679074573378, 10.0, 2.8215000000000003, 8.464500000000001, 1.6666666666666667, 1489702.604875, 57.322500000000005, -8.55, 0.0, 2.8215000000000003, 8.464500000000001, 1.25, 496567.5349583333, 15.0, -6.369248374724489, 10.0, 8.464500000000001, 2.8215000000000003, 1.25, 993135.0699166666, 31.929000000000002, -8.55, 3.3333333333333335, 2.8215000000000003, 8.464500000000001, 1.25, 1489702.604875, 94.00200000000001, -8.549271685298477, 10.0, 2.8215000000000003, 8.464500000000001, 0.8333333333333334, 496567.5349583333, 37.572, -8.55, 10.0, 8.464500000000001, 2.8215000000000003, 0.8333333333333334, 993135.0699166666, 102.5458370358404, 3.3202691885773667, 3.3333333333333335, 8.464500000000001, 2.8215000000000003, 0.8333333333333334, 1489702.604875, 96.82350000000001, -8.542324122696275, 6.666666666666667, 2.8215000000000003, 5.643000000000001, 1.6666666666666667, 496567.5349583333, 54.501000000000005, -8.55, 3.3333333333333335, 5.643000000000001, 2.8215000000000003, 1.6666666666666667, 993135.0699166666, 15.0, -0.08549999999999969, 0.0, 5.643000000000001, 2.8215000000000003, 1.6666666666666667, 1489702.604875, 29.1075, -8.415346769679589, 0.0, 2.8215000000000003, 5.643000000000001, 1.25, 496567.5349583333, 40.3935, -8.55, 0.0, 2.8215000000000003, 5.643000000000001, 1.25, 993135.0699166666, 37.572, 1.2595757578554623, 3.3333333333333335, 2.8215000000000003, 5.643000000000001, 1.25, 1489702.604875, 26.286, -8.55, 0.0, 2.8215000000000003, 5.643000000000001, 0.8333333333333334, 496567.5349583333, 60.144000000000005, 1.4785156128057104, 6.666666666666667, 2.8215000000000003, 5.643000000000001, 0.8333333333333334, 993135.0699166666, 26.286, -0.08549999999999969, 10.0, 2.8215000000000003, 5.643000000000001, 0.8333333333333334, 1489702.604875, 23.4645, -0.04625546337663963, 10.0, 2.8215000000000003, 2.8215000000000003, 1.6666666666666667, 496567.5349583333, 43.118998986707666, 1.9672639881267242, 0.0, 2.8215000000000003, 2.8215000000000003, 1.6666666666666667, 993135.0699166666, 43.215, 0.7408701841952097, 3.3333333333333335, 2.8215000000000003, 2.8215000000000003, 1.6666666666666667, 1489702.604875, 54.501000000000005, -6.905753322298148, 0.0, 2.8215000000000003, 2.8215000000000003, 1.25, 496567.5349583333, 47.921663915893184, -0.08549999999999969, 6.666666666666667, 2.8215000000000003, 2.8215000000000003, 1.25, 993135.0699166666, 54.501000000000005, 4.954846790306749, 0.0, 2.8215000000000003, 2.8215000000000003, 1.25, 1489702.604875, 23.4645, -8.55, 0.0, 2.8215000000000003, 2.8215000000000003, 0.8333333333333334, 496567.5349583333, 51.679500000000004, -8.55, 0.0, 2.8215000000000003, 2.8215000000000003, 0.8333333333333334, 993135.0699166666, 54.501000000000005, -3.8861065440704525, 10.0, 2.8215000000000003, 2.8215000000000003, 0.8333333333333334, 1489702.604875]
N = 81 
m = 4

ship_inputs = [118.1, 15,88.1, 15, 17.1, 13, 4.3, 10]
lwl = ship_inputs[0]
lb = ship_inputs[1]
lm = ship_inputs[2]
ls = ship_inputs[3]
bwl = ship_inputs[4]
bs = ship_inputs[5]

for i in range(m): 
    z = (i * (10/(m-1))) * 2
    print(z)
    pt1 = (0,0, z)
    pt2 = (lb, bwl/2, z)
    pt3 = (lb+lm, bwl/2, z)
    pt4 = (lwl, bs/2, z)
    pt5 = (lwl, -bs/2, z)
    pt6 = (lb+lm, -bwl/2, z)
    pt7 = (lb, -bwl/2, z)
    
    rs.AddLine(pt1, pt2)
    rs.AddLine(pt2, pt3)
    rs.AddLine(pt3, pt4)
    if bs != 0: 
        rs.AddLine(pt4, pt5)
    rs.AddLine(pt5, pt6)
    rs.AddLine(pt6, pt7)
    rs.AddLine(pt7, pt1)
    
for i in range(N): 
    color_val = Design_Vec[7*i + 6]
    length = Design_Vec[7*i + 3] # x dir
    width = Design_Vec[7*i + 4] # y dir
    height = Design_Vec[7*i + 5] # z dir
    x1 = Design_Vec[7*i]
    y1 = Design_Vec[7*i + 1]
    z1 = Design_Vec[7*i + 2] * 2
    
    c1 = (x1, y1, z1)
    c2 = (x1, y1+ width, z1)
    c3 = (x1 + length, c2[1], z1)
    c4 = (c3[0], y1, z1)
    c5 = (x1, y1, z1+ height)
    c6 = (c2[0], c2[1], c5[2])
    c7 = (c3[0], c3[1], c5[2])
    c8 = (c4[0], c4[1], c5[2])
    
    box = rs.AddBox([c1, c2, c3, c4, c5, c6, c7, c8])
    
    if color_val < 500000: 
        color = (0, 0 , 255)
    elif color_val < 1000000: 
        color = (0, 255, 0)
    else: 
        color = (255, 0, 0)
    rs.ObjectColor(box, color)