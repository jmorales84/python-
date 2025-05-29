import pulp as p 
Lp_prob=p.LpProblem('Problem1',p.LpMaximize)

#Decision variables
x1=p.LpVariable("x1",lowBound=0)#CREATE A VARIABLE X1 >=0
x2=p.LpVariable("x2",lowBound=0)#CREATE A VARIABLE X2 >=0
x3=p.LpVariable("x3",lowBound=0)#CREATE A VARIABLE X3 >=0

#OBJETIVE FUCTION 
Lp_prob+=1600*x1+1300*x2+600*x3

#CONSTRAINTS
Lp_prob+=2*x1+1.5*x2+x3<=20
Lp_prob+=2*x1+x2+1.5*x3<=24
Lp_prob+=x1+2*x2+0.5*x3<=20
print(Lp_prob)

#solving the linear programming problem
status=Lp_prob.solve()
print(p.LpStatus[status])

#solution
p.value(x1)
