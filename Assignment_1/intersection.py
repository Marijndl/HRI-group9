# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 13:52:07 2020

@author: rcuijper
"""

import numpy as np
import math

def footpoint(p, line_segment):
    # a line segment is a list of two points
    # p is point, which is a 2-element list
    a=np.array(line_segment[0])
    b=np.array(line_segment[1])
    w=b-a
    pp=np.array(p)

    mu=np.dot((pp-a),w)/np.dot(w,w)
    f=a+mu*w
    
    return f, mu

def intersection(p, v, line_segment):
    # p is a point, v is a vector, line_segment is a list of 2 points
    
    foot, mu_f = footpoint(p, line_segment)
    
    # line l:p + lam * v
    fp = foot - np.array(p)
    vv=np.array(v)
    #-np.array(line_segment[0])
        
    h=np.dot(fp, vv)
    if h==0:
        return None, 0, 0
    
    lam= np.dot(fp,fp)/h
    s = p + lam*vv
    
    #if s is on the segmentthen  0<mu<1
    a=np.array(line_segment[0])
    b=np.array(line_segment[1])
    w=b-a
    mu_s=np.dot(s-a, w)/np.dot(w,w)
    #verify correctness
    #s2 = a + mu_s*w
    #print s==s2
    return s, lam, mu_s

def intersect_poly(p, v, point_list):
    
    n=len(point_list)
    result=[]
    for i in range(n):
        q1=point_list[i]
        q2=point_list[(i+1)%n]
        s, lam, mu = intersection(p,v,[q1,q2])
 #       print s, mu
        if not s is None:
            if (0<=mu<=1) and (lam>=0): #forward rays only
                result.append(s)
    return result

def compute_distance(p,point_list):
    dist=[]
    for q in point_list:
        x=np.array(p)-np.array(q)
        dist.append(np.linalg.norm(x))

    return dist

def min_distance(p,point_list):
    dist=compute_distance(p,point_list)
    
    return np.min(dist)
        
if __name__=="__main__":
    a=[2.0,3.0] # make sure doubles are used
    b=[4.0,1.0]
    c=[5.0,2.0]
    d=[3.0,4.0]
    
    p=[0.0,0.0]
    v=[1.5,1]
    
    print footpoint(p,[a,b])
    print intersection(p,v,[a,b])
    
    my_list = [a,b,c,d]
    
    for i in range(len(my_list)):
        n=len(my_list)
        q1=my_list[i]
        q2=my_list[(i+1)%n]
        s, lam, mu = intersection(p,v,[q1,q2])
        print s, lam , mu, 0<=mu<=1
        
    result=intersect_poly(p, v, my_list)
    print result
    
    print min_distance(p, result)
        
        