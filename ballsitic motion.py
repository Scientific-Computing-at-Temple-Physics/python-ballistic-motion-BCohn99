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
angle= int(input("Enter angle:"))
int_h= int(input("Enter starting height in m:"))
t_step= int(input("Enter time step in s:"))
float(t_step)
#deg to rad
theata = angle*ma.pi/180
print(theata)

#starting time
t0 = 0.0

#total flight time
tflight= t0+t_step

#breaking down velocity into x and y components;
vel_x = int_vel*ma.cos(theata)
vel_y = int_vel*ma.sin(theata)
#print(vel_x)
#print(vel_y)

# equation for vy
vel_y = g*t_step

#equation for y
y= g*vel_y
float(y)
#print(y)
 #range
x = vel_x+ tflight
float(x)

print("Max height is:", y, "meters")
print("Range is:",x,"meters")
print("total time:",tflight, "s")