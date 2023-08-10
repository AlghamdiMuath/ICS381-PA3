#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import copy

def ac3(csp, arcs_queue=None, current_domains=None, assignment=None):
    if current_domains is None:
        current_domains = {var: copy.deepcopy(csp.domains) for var in csp.variables}
        
    if arcs_queue is None:
        arcs_queue = {(xi, xj) for xi in csp.adjacency for xj in csp.adjacency[xi]}
    else:
        arcs_queue = set(arcs_queue)
    if assignment is not None:
        for var, val in assignment.items():
            if len(current_domains[var]) == 1 and val not in current_domains[var]:
                return False, current_domains
            current_domains[var] = [val]

            for neighbor in csp.adjacency[var]:
                if neighbor != var:
                    arcs_queue.add((neighbor, var))

    while arcs_queue:
        var1, var2 = arcs_queue.pop()
        if revise(csp, current_domains, var1, var2):
            if not current_domains[var1]:
                return False, current_domains
            for neighbor in csp.adjacency[var1]:
                if neighbor != var2:
                    arcs_queue.add((neighbor, var1))

    return True, current_domains


def revise(csp, current_domains, var1, var2):
    revised = False
    for val1 in list(current_domains[var1]):
        satisfies = False
        for val2 in current_domains[var2]:
            if csp.constraint_consistent(var1, val1, var2, val2):
                satisfies = True
                break
        if not satisfies:
            print(type(current_domains))
            print(type(current_domains[var1]))
            print(var1,current_domains[var1])
            current_domains[var1].remove(val1)
            revised = True
    return revised

def backtracking(csp):
    current_domains = {var: copy.deepcopy(list(csp.domains.values())[0]) for var in csp.variables}
    print("HERE")
    print(current_domains)
    return backtracking_helper({} , csp , current_domains)

def backtracking_helper(assignment, csp , current_domains):
    if len(assignment) == len(csp.variables):
        return assignment
    var = select_unassigned_variable(current_domains,assignment,csp)
    
    for val in order_domain_values(csp, var, assignment, current_domains):
        if csp.check_partial_assignment(assignment):
            assignment[var] = val
            new_domains = copy.deepcopy(current_domains)
            new_domains[var] = [val]
            arcs_queue = get_unassigned_neighbors(var, assignment, current_domains, csp)
            if ac3(csp, arcs_queue,new_domains, assignment):
                print("HERE LINE 73")
                result = backtracking_helper(assignment, csp, new_domains)
                if result is not None:
                    return result
            del assignment[var]
    return None

def select_unassigned_variable(current_domains, assignment, csp):
    unassigned = []
    for var in csp.variables:
        if var not in assignment:
            unassigned.append(var)
    min_var = unassigned[0]
    min_size = len(current_domains[min_var])
    for var in unassigned:
        if len(current_domains[var]) < min_size:
            min_var = var
            min_size = len(current_domains[var])
    return min_var


def order_domain_values(csp, var, assignment, current_domains):
    domain = current_domains[var]
    sorted_values = []
    for val in domain:
        conflicts = 0
        for neighbor in csp.adjacency[var]:
            if neighbor not in assignment:
                for neighbor_val in current_domains[neighbor]:
                    if not csp.constraint_consistent(var, val, neighbor, neighbor_val):
                        conflicts += 1
        sorted_values.append((val, conflicts))
    sorted_values.sort(key=lambda x: x[1])
    return [val[0] for val in sorted_values]


def count_conflicts(csp, var, val, assignment, current_domains):
    conflicts = 0
    for neighbor in csp.adjacency[var]:
        if neighbor not in assignment:
            for n_val in current_domains[neighbor]:
                if not csp.constraint_consistent(var, val, neighbor, n_val):
                    conflicts += 1
    return conflicts

def get_unassigned_neighbors(var, assignment, current_domains, csp):
    unassigned = [neighbor for neighbor in csp.adjacency[var] if neighbor not in assignment]
    arcs_queue = []
    for neighbor in unassigned:
        for val in current_domains[neighbor]:
            arcs_queue.append((neighbor, var))
        break
    return arcs_queue


class SudokuCSP:

    def __init__(self, partial_assignment):
        self.variables = [(i, j) for i in range(1, 10) for j in range(1, 10)]
       # print(self.variables)
        self.domains = {}
        size = 3 # square size
        self.adjacency = {}
        
        for var in self.variables:

            self.domains[var] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
           # print(self.domains)

            if var in partial_assignment:
                self.domains[var] = [partial_assignment[var]]
            
            neighbors = []
            
            for j in range(1, 10):
                if j != var[1]:
                    neighbors.append((var[0], j))
            
            for i in range(1, 10):
                if i != var[0]:
                    neighbors.append((i, var[1]))
           # print(neighbors)
            rstart = 1 + ((var[0] - 1) // size) * size
            #print(rstart)
            cstart = 1 + ((var[1] - 1) // size) * size
           # print(cstart)
            for i in range(rstart, rstart + size):
                for j in range(cstart, cstart + size):
                    if (i, j) != var and (i, j) not in neighbors:
                        neighbors.append((i, j))
            
            self.adjacency[var] = neighbors
    # checks constraint between two variables. for graph-color this is inequality constraint.
    def constraint_consistent(self, var1, val1, var2, val2):
        if var2 in self.adjacency[var1] and var1 in self.adjacency[var2]: # neighbors
            return val1 != val2
        else: # not neighbors
            return True
    
    # to check if a partial assignment is consistent, 
    # we check if assigned variables and their assigned neighbors are consistently assigned. 
    def check_partial_assignment(self, assignment):
        if assignment is None:
            return False
        for var in assignment:
            assigned_neighbors = [n for n in self.adjacency[var] if n in assignment]
            for n in assigned_neighbors:
                if not self.constraint_consistent(var, assignment[var], n, assignment[n]):
                    return False
        return True
    
    # a solution is (1) completely assigned variables and (2) consistently assigned. 
    def is_goal(self, assignment):
        if assignment is None:
            return False
        # check complete assignment
        for var in self.variables:
            if var not in assignment:
                return False 
        # check consistency
        for var in self.variables:
            neighbors = self.adjacency[var]
            for n in neighbors:
                if not self.constraint_consistent(var, assignment[var], n, assignment[n]):
                    return False
        return True
    

