
from gurobipy import *

model = Model()
nFood = ["f1","f2","f3","f4"]
nMed = ["m1","m2","m3","m4"]
nSurg = ["s1","s2","s3","s4"]
nCloth = ["c1","c2","c3","c4"]
xFood = model.addVars(nFood, ub=5.0,vtype=GRB.INTEGER).values()
xMed = model.addVars(nMed, ub=5.0,vtype=GRB.INTEGER).values()
xSurg = model.addVars(nSurg, ub=5.0,vtype=GRB.INTEGER).values()
xCloth = model.addVars(nCloth, ub=5.0,vtype=GRB.INTEGER).values()
xBin = model.addVar(lb = 0.0,vtype="B", name="xBin")
model.update()
n = 0
sums = 0
while n <= 3:
    sums += xFood[n] + xMed[n] + xSurg[n] + xCloth[n]
    n+=1
print(sums)
obj = model.setObjective(sums, GRB.MAXIMIZE)
con = []
con.append(model.addConstr(sum(xFood)<=12))
con.append(model.addConstr(sum(xMed)<=17))
con.append(model.addConstr(sum(xSurg)<=11))
con.append(model.addConstr(sum(xCloth)<=18))
con.append(model.addConstr((xFood[0] + xMed[0] + xSurg[0] + xCloth[0]) <= 9))
con.append(model.addConstr((xFood[1] + xMed[1] + xSurg[1] + xCloth[1]) <= 9))
con.append(model.addConstr((xFood[2] + xMed[2] + xSurg[2] + xCloth[2]) <= 10))
con.append(model.addConstr((xFood[3] + xMed[3] + xSurg[3] + xCloth[3]) <= 10))
c = 0
while c <= 3:
    con.append(model.addConstr(xMed[c] + 4*xBin >= + 4))
    con.append(model.addConstr(xSurg[c] +2*xBin <= 5 ))
    model.update()
    c+=1


model.optimize()

print('Sensitivity Analysis ', model.ObjVal)

#model.printAttr(['X','RC', 'Obj', 'SAObjUp', 'SAObjLow'])

#model.printAttr(['RHS','Slack', 'Pi','SARHSUp','SARHSLow'])
print(xFood)
print(xCloth)
print(xSurg)
print(xMed)
print(xBin)

