def split():
    t = (1, 2, 3, 4, 5, 6)

    def split_tuple(t):
        
        if (int(len(t) % 2) == 0):
            size_each = int(len(t)//2)
            t_result_1 = t[:size_each]
            t_result_2 = t[size_each:]
        else:
            size_each = int(len(t)//2)
            t_result_1 = t[:size_each]
            t_result_2 = t[size_each:-1]

        return print(f'\nResultado: Tupla 1: {t_result_1} | Tupla 2: {t_result_2}')

    split_tuple(t)

split()
    
    
#    import numpy as np

#arr = np.array((1, 2, 3, 4, 5))

#print(arr)