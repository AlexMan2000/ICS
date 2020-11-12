#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 00:12:40 2020

@author: xg7
"""

class Point:
    """A class to represent a two-dimensional point"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def distance(self, point2):
        dx = self.x - point2.x
        dy = self.y - point2.y
        return (dx**2 + dy**2)**0.5
    
    def equals(self, point2):
        return (self.x == point2.x) and (self.y == point2.y)

    def __str__(self):
        return 'point at ({}, {})'.format(self.x, self.y)


p1 = Point()
p1.move(2, 3)

p2 = Point()
p2.move(5, 7)

print(p1.distance(p2))