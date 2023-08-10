#!/usr/bin/env python
# coding: utf-8

# In[20]:

import numpy as np
import copy

def tour_cost(state, adj_matrix):
    Sum = 0
    for i in range(len(state)-1):
        if not np.isnan(adj_matrix[state[i], state[i+1]]):
            Sum += adj_matrix[state[i], state[i+1]]
        else:
            return np.nan
    return Sum

def random_swap(state):
    #self.state = state
    state_copy = copy.deepcopy(state)
    idx1, idx2 = np.random.choice(len(state), size=2, replace=False)
    state_copy[idx1], state_copy[idx2] = state_copy[idx2], state_copy[idx1]
    return state_copy

def simulated_annealing(initial_state, adj_matrix, initial_T=1000):
    T = initial_T
    current = initial_state
    iters = 0
    while True:
        T = T * 0.99
        if T < 1e-14:
            break
        final_state = random_swap(current)
       # print(current)
       # print(final_state)
        deltaE = tour_cost(current , adj_matrix) - tour_cost(final_state,adj_matrix)
        if deltaE > 0:
            current = final_state
        elif deltaE <= 0:
            u =  np.random.uniform()
            if u <= np.exp(deltaE / T):
                current = final_state
        iters += 1
    return current, iters


# In[ ]: