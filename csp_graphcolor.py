class GraphColorCSP:
    """
        Variables is list of region names.
        Colors is list of colors (this will be domain for all variables).
        Adjacency is dictionary of key, val where key is a variable and value is list of its neighbor variables. 
    """
    def __init__(self, variables, colors, adjacency):
        self.variables = variables
        self.domains = {}
        for var in self.variables:
            self.domains[var] = [c for c in colors]
            
        self.adjacency = adjacency
        
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