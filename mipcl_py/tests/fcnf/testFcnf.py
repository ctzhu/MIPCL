#!/usr/bin/python
from mipcl_py.models.fcnf import Fcnf

H = {
   'Demands': (-4, -3, -5, 0, 5, 4, 3),
   'Arcs': [(0,1,5,7,2), (0,2,4,4,4), (1,2,3,6,2), (1,3,6,4,1),
            (1,4,7,7,2), (2,0,8,5,1), (2,3,3,4,1), (2,5,4,6,2),
            (3,2,5,8,2), (3,4,2,7,2), (3,5,4,5,1), (4,6,7,6,2),
            (4,6,7,6,2), (5,4,5,9,2), (6,3,4,6,1), (6,5,6,8,2)
   ]
}

prob = Fcnf("test1")
prob.model(H)
prob.optimize(False)
prob.printSolution()

