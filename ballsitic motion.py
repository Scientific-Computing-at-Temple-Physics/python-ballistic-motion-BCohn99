#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 11:56:55 2018

@author: brandoncohn
"""
import math as ma
#input values
g=float(-9.81) 
int_vel= int(input("Enter starting velocity in m/s:"))
angle= int(input("Enter angle in degrees:"))
int_h= int(input("Enter starting height in m:"))
if int_h <0:
    print("input must be zero or greater, Try Again")
if int_h<0:
    int_h= int(input("Enter starting height in m:"))    
    

t_step= int(input("Enter time step in s:"))
float(t_step)
#deg to rad
theata = angle*ma.pi/180
#print("Theata:",theata,"rads")

#total flight time
tflight= t_step*10

#breaking down velocity into x and y components;
vel_x = int_vel*ma.cos(theata)
vel_y = int_vel*ma.sin(theata)
#print(vel_x)
#print(vel_y)


#equation for max height
Hmax = int_h + ((-vel_y**2 )/(2*g))
 #equation for range
x = vel_x+ tflight
float(x)

print("Max height is:",Hmax, "meters")
print("Range is:",x,"meters")
print("total time:",tflight, "s")