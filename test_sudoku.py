if __name__ == "__main__":    
    from csp import *
    
    # tests 1: sudoku constructor implementation
    partial_assignment = {(9,2):3, (9,3):5, (9,5):8, (9,9):9,
                          (8,7):6, (8,9):3,
                          (7,3):8, (7,4):3, (7,7):7,
                          (6,2):1, (6,4):4, (6,9):2,
                          (5,2):7, (5,4):9, (5,6):3, (5,8):6,
                          (4,1):3, (4,6):2, (4,8):5,
                          (3,3):3, (3,6):5, (3,7):2,
                          (2,1):7, (2,3):9,
                          (1,1):4, (1,5):7, (1,7):8, (1,8):3, (1,9):6}
    sudoku = SudokuCSP(partial_assignment)
    
    print(len(sudoku.variables))
    print('_______________________________________________________________________')
    print(sudoku.variables) 
    print('_______________________________________________________________________')
    print(sudoku.domains[(1,1)]) 
    print('_______________________________________________________________________')
    print(sudoku.domains[(5,7)]) 
    print('_______________________________________________________________________')
    print(sudoku.domains[(7,3)]) 
    print('_______________________________________________________________________')
    print(sudoku.adjacency[(1,1)]) 
    print('_______________________________________________________________________')
    print(sudoku.adjacency[(6,2)]) 
    print('_______________________________________________________________________')
    print(sudoku.adjacency[(3,9)]) 
    print('_______________________________________________________________________')
    
    # tests 2: run backtracking search on soduku
    import time
    start_time = time.time()
    sol_assignment = backtracking(sudoku)
    end_time = time.time()
    is_complete_and_consistent = sudoku.is_goal(sol_assignment)
    print('Sol: {}'.format(sol_assignment))
    print('Is sol complete and consistent: {}'.format(is_complete_and_consistent))
    print('Time taken: {} sec'.format(end_time - start_time))
    print('_______________________________________________________________________')