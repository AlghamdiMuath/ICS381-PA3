# helper function to generate random graphs and random tour for graph
def gen_rand_graph(N=8, edge_prob=0.95):
    adj_matrix = np.zeros((N, N))
    
    for i in range(N):
        for j in range(N):
            if i == j:
                adj_matrix[i, j] = np.nan
               
            # sample a random u
            u = np.random.uniform()
            ij_edge_cost = np.nan
            if u <= edge_prob:
                # sample a random cost
                ij_edge_cost = np.random.randint(low=10, high=100)
                
            adj_matrix[i, j] = ij_edge_cost
            adj_matrix[j, i] = ij_edge_cost
            
    return adj_matrix
        
def sample_valid_tour(adj_matrix):
    N = adj_matrix.shape[0]
    # keep sampling random tours until we get a valid one
    rnd_tour = list(np.random.permutation(N))
    while np.isnan(tour_cost(rnd_tour, adj_matrix)):
        rnd_tour = list(np.random.permutation(N))
        
    return rnd_tour
    
if __name__ == "__main__":
    import numpy as np
    from local_search import *
    
    # set random seed for reproducibility
    rand_seed=735122311
    np.random.seed(rand_seed)
    
    # tests 1
    N = 20
    adj_matrix = gen_rand_graph(N=N)
    state1 = sample_valid_tour(adj_matrix)
    tcost = tour_cost(state1, adj_matrix)
    
    print('TSP state: {}'.format(state1))
    print('f(s) = {}'.format(tcost))
    print('_______________________________________________________________________')
    
    state2 = sample_valid_tour(adj_matrix)
    tcost = tour_cost(state2, adj_matrix)
    print('TSP state: {}'.format(state2))
    print('f(s) = {}'.format(tcost))
    print('_______________________________________________________________________')
    
    # tests run simulated annealing
    N = 20
    adj_matrix = gen_rand_graph(N=N)
    initial_state = sample_valid_tour(adj_matrix)
    initial_tcost = tour_cost(initial_state, adj_matrix)
    initial_T = 1000
    final_state, iters = simulated_annealing(initial_state, adj_matrix, initial_T=initial_T)
    final_tcost = tour_cost(final_state, adj_matrix)
    print('Initial state objective value: {}'.format(initial_tcost))
    print('Final state objective value: {}'.format(final_tcost))
    print('# iterations: {}'.format(iters)) 
    print('_______________________________________________________________________')
    
    N = 100
    adj_matrix = gen_rand_graph(N=N)
    initial_state = sample_valid_tour(adj_matrix)
    initial_tcost = tour_cost(initial_state, adj_matrix)
    initial_T = 50000
    final_state, iters = simulated_annealing(initial_state, adj_matrix, initial_T=initial_T)
    final_tcost = tour_cost(final_state, adj_matrix)
    print('Initial state objective value: {}'.format(initial_tcost))
    print('Final state objective value: {}'.format(final_tcost))
    print('# iterations: {}'.format(iters)) 