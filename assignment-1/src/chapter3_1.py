#   Point(1) Atlanta, Georgia; 51.5138505182,-0.15690922737098845
#   Point(2) Orlando, Florida; 28.5383355,-81.37923649999999
#   Point(3) Savannah, Georgia; 32.0835407,-81.09983419999998
#   Point(4) Charlotte, North Carolina;35.2270869,-80.84312669999997
#  
import math
point_x1 = 51.5138505182;
point_y1 = -0.15690922737098845;
point_x2 = 28.5383355;
point_y2 = -81.37923649999999;
point_x3 = 32.0835407;
point_y3 = -81.09983419999998;
 
point_x4 = 35.2270869;
point_y4 = -80.84312669999997;
def dis(x1,y1,x2,y2):
    radius= 6371.01
    d = radius * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))
    return d
def area(s1,s2,s3):
    s=(s1+s2+s3)/2
    areaTriangle=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
    return areaTriangle

side1=dis(point_x1,point_y1,point_x2,point_y2)
side2=dis(point_x1,point_y1,point_x3,point_y3)
side3=dis(point_x3,point_y3,point_x2,point_y2)
area1=area(side1,side2,side3)
 
 
side1=dis(point_x1,point_y1,point_x4,point_y4)
side2=dis(point_x1,point_y1,point_x3,point_y3)
side3=dis(point_x3,point_y3,point_x4,point_y4)
area2=area(side1,side2,side3)
print("area is:",area1+area2)

 
