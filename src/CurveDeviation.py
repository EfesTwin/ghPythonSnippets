"""
Solves Curve Deviation for two lists of curves. The amount of curves in each 
list has to be equal. Take care of the list order! The first curve in list A
is always compared to the first curve in list B and so on...
-
Author: Max Eschenbach
Updated: 151201
    Args:
        A: The first set of curves.
        B: The second set of curves
    Returns:
        MaxParamA: The parameter of the maximum deviation on curve A.
        MaxParamB: The parameter of the maximum deviation on curve B.
        MaxDist: The distance between A and B at the point of maximum deviation.
        MinParamA: The parameter of the minimum deviation on curve A.
        MinParamB: The parameter of the minimum deviation on curve B.
        MinDist: The distance between A and B at the point of minimum deviation.
"""
import Rhino
import rhinoscriptsyntax as rs
import scriptcontext
from scriptcontext import doc

ghenv.Component.Name = "CurveDeviation"
ghenv.Component.NickName = "CrvDev"

A = list(A)
B = list(B)

MaxParamA = []
MaxParamB = []
MaxDist = []
MinParamA = []
MinParamB = []
MinDist = []

if A != None and B != None and len(A) != 0 and len(B) != 0:
    if len(A) == len(B):
        
        for i in range(len(A)):
            tplCrvDev = rs.CurveDeviation(A[i], B[i])
            
            MaxParamA.append(tplCrvDev[0])
            MaxParamB.append(tplCrvDev[1])
            MaxDist.append(tplCrvDev[2])
            MinParamA.append(tplCrvDev[3])
            MinParamB.append(tplCrvDev[4])
            MinDist.append(tplCrvDev[5])
    else:
        raise ValueError("You have to supply equal amounts of curves for A and B!")