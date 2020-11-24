import numpy as np
# import math
# import matplotlib
import geneticalgorithm as ga


def f(x):
    res = 0
    for i in x:
        res = res + int(i)
    return res


varbound = np.array([[-5.12, 5.12]] * 5)

algorithm_param = {'max_num_iteration': 1000, 'population_size': 100, 'mutation_probability': 0.02, 'elit_ratio': 0.0,
                   'crossover_probability': 1, 'parents_portion': 0.3, 'crossover_type': 'two_point',
                   'max_iteration_without_improv': None}

model = ga.geneticalgorithm(function=f, dimension=5,
                            variable_type='real',
                            variable_boundaries=varbound,
                            algorithm_parameters=algorithm_param)

if __name__ == '__main__':
    k = model.run()
