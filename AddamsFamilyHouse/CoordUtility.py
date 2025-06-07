#*****************************************************************************
#
#  System        : 
#  Module        : 
#  Object Name   : $RCSfile$
#  Revision      : $Revision$
#  Date          : $Date$
#  Author        : $Author$
#  Created By    : Robert Heller
#  Created       : Thu Jun 5 16:19:56 2025
#  Last Modified : <250607.1431>
#
#  Description	
#
#  Notes
#
#  History
#	
#*****************************************************************************
#
#    Copyright (C) 2025  Robert Heller D/B/A Deepwoods Software
#			51 Locke Hill Road
#			Wendell, MA 01379-9728
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
# 
#
#*****************************************************************************


import FreeCAD as App
import Part, TechDraw, Mesh, MeshPart, TechDrawGui
from FreeCAD import Base

def Near(x,a,b):
    if x >= a and x <= b:
        return True
    else:
        return False

def ZextentsAtX(mesh,x):
    topo=mesh.Topology
    points, triangles = topo 
    minZ = None
    maxZ = None
    for p in points:
        if Near(p.x,x-2,x+2):
            if minZ == None:
                minZ = p.z
            if p.z < minZ:
                minZ = p.z
            if maxZ == None:
                maxZ = p.z
            if p.z > maxZ:
                maxZ = p.z
    return (minZ,maxZ)

def YextentsAtX(mesh,x):
    topo=mesh.Topology
    points, triangles = topo 
    minY = None
    maxY = None
    for p in points:
        if Near(p.x,x-2,x+2):
            if minY == None:
                minY = p.y
            if p.y < minY:
                minY = p.y
            if maxY == None:
                maxY = p.y
            if p.y > maxY:
                maxY = p.y
    return (minY,maxY)

def XextentsAtZ(mesh,z):
    topo=mesh.Topology
    points, triangles = topo 
    minX = None
    maxX = None
    for p in points:
        if Near(p.z,z-2,z+2):
            if minX == None:
                minX = p.x
            if p.x < minX:
                minX = p.x
            if maxX == None:
                maxX = p.x
            if p.x > maxX:
                maxX = p.x
    return (minX,maxX)
 
def allXAtZ(mesh,z):
    topo=mesh.Topology
    points, triangles = topo 
    XSet = set()
    for p in points:
        if Near(p.z,z-2,z+2):
            XSet.add(p.x)
    XList = list(XSet)
    XList.sort()
    return XList

def allYAtX(mesh,x):
    topo=mesh.Topology
    points, triangles = topo 
    YSet = set()
    for p in points:
        if Near(p.x,x-2,x+2):
            YSet.add(p.y)
    YList = list(YSet)
    YList.sort()
    return YList

def pointNearXY(mesh,x,y):
    topo=mesh.Topology
    points, triangles = topo 
    result = list()
    for p in points:
        if Near(p.x,x-2,x+2) and Near(p.y,y-2,y+2):
            result.append(p)
    return result

def pointNearXZ(mesh,x,z):
    topo=mesh.Topology
    points, triangles = topo 
    result = list()
    for p in points:
        if Near(p.x,x-2,x+2) and Near(p.z,z-2,z+2):
            result.append(p)
    return result

def pointNearXYZ(mesh,x,y,z):
    topo=mesh.Topology
    points, triangles = topo 
    nearpoint=Base.Vector(x,y,z)
    dist=None
    result=None
    for p in points:
        if dist == None:
            dist = nearpoint.distanceToPoint(p)
            result = p
        elif nearpoint.distanceToPoint(p) < dist:
            dist = nearpoint.distanceToPoint(p)
            result = p
    return result
