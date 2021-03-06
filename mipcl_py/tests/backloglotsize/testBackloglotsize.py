#!/usr/bin/python
from mipcl_py.models.backloglotsize import Backloglotsize

d = [1000, 1000, 1000, 1000, 200]
u = [100, 600, 200, 1000, 400, 1000, 400,  600, 200]
f = [0, 0, 100000, 0, 100000, 0, 100000, 0, 100000]

c = [
  [   0,   50,  100,  150,  200],
  [1500, 1550, 1600, 1650, 1700],
  [2000, 2050, 2100, 2150, 2200],
  [2000, 1500, 1550, 1600, 1650],
  [2500, 2000, 2050, 2100, 2150],
  [  -1, 2000, 1500, 1550, 1600],
  [  -1, 2500, 2000, 2050, 2100],
  [  -1,   -1, 2000, 1500, 1550],
  [  -1,   -1, 2500, 2000, 2050],
]

prob = Backloglotsize("test1")
prob.model(d,u,f,c)
prob.optimize(False)
prob.printSolution()

