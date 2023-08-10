if __name__ == "__main__":    
    from csp_graphcolor import *
    from csp import *
    import pickle, time
    
    # tests on large graphs. 
    for i in range(5):
        fname = './large_graph_{}.pickle'.format(i)
        with open(fname, 'rb') as handle:
            graphcolorcsp = pickle.load(handle) # read in the graphcolorcsp object
        
        # solve using backtracking and time it
        start_time = time.time()
        sol_assignment = backtracking(graphcolorcsp)
        end_time = time.time()
        if sol_assignment is not None:
            is_complete_and_consistent = graphcolorcsp.is_goal(sol_assignment)
        else:
            is_complete_and_consistent = False
                                    
        print('Is sol complete and consistent: {}'.format(is_complete_and_consistent))
        print('Time taken: {} sec'.format(end_time - start_time))
        print('_______________________________________________________________________')