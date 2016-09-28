'''
Created on 2016-09-28

@author: Niranjan
'''

import pulp

def solve_lp():
    #create the LP object, set up as a maximization problem
    prob = pulp.LpProblem('XYZ', pulp.LpMaximize)
    
    #set up decision variables
    ships = pulp.LpVariable('ships', lowBound=0, cat='Integer')
    boats = pulp.LpVariable('boats', lowBound=0, cat='Integer')
    
    #model weekly production costs
    raw_material_costs = 10 * ships + 9 * boats
    variable_costs = 14 * ships + 10 * boats
    
    #model weekly revenues from toy sales
    revenues = 27 * ships + 21 * boats
    
    #use weekly profit as the objective function to maximize
    profit = revenues - (raw_material_costs + variable_costs)
    prob += profit  # here's where we actually add it to the obj function
    
    #add constraints for available labor hours
    carpentry_hours = ships + boats
    prob += (carpentry_hours <= 80)
    finishing_hours = 2*ships + boats
    prob += (finishing_hours <= 100)
    
    # add constraint representing demand for ships
    prob += (ships <= 40)
    print(prob)
    #solve the LP using the default solver
    optimization_result = prob.solve()
    #make sure we got an optimal solution
    assert optimization_result == pulp.LpStatusOptimal
    
    #display the results
    for var in (ships, boats):
        print('Optimal weekly number of {} to produce: {:1.0f}'.format(var.name, var.value()))

if __name__== '__main__':
    solve_lp()
    
