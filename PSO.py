import numpy as np
import random
import math


class PSO(object):
    def __init__(self, distances, costs, n_particles):
        self.distances = distances
        self.costs = costs
        self.n_particles = n_particles
        positions = self._init_position()
        self.particle_dim = len(positions[0])
        self.particles_pos = np.array(positions)
        self.velocities = np.random.uniform(
            size=(n_particles, self.particle_dim))
        self.g_best = positions[0]
        self.p_best = self.particles_pos

    def update_position(self, x, v):
        x = np.array(x)
        v = np.array(v)
        new_x = []
        for idx, val in np.ndenumerate(x):
            i, = idx
            new = math.ceil(abs(x[i] + v[i]))
            while new in new_x or new > 20:
                new += 1
                if new > 20:
                    new = 1
            new_x.append(new)
        return new_x

    def update_velocity(self, x, v, p_best, g_best, c0=0.5, c1=1.5, w=0.75):
        x = np.array(x)
        v = np.array(v)
        r = np.random.uniform()
        p_best = np.array(p_best)
        g_best = np.array(g_best)
        new_v = v.copy()
        for i, val in np.ndenumerate(new_v):
            new_v[i] = w*val + c0 * r * \
                (p_best[i] - x[i]) + c1 * r * (g_best[i] - x[i])
        return new_v

    def _get_fitness_int(self, branches):
        z = 0
        for i in range(0, len(branches)):
            for j in range(i + 1, len(branches)):
                z += self.distances[branches[i]][branches[j]
                                                 ] * self.costs[branches[i]][branches[j]]
        return z

    def run(self, num_sims=150):
        for _ in range(num_sims):
            for i in range(self.n_particles):
                x = self.particles_pos[i]
                v = self.velocities[i]
                p_best = self.p_best[i]
                self.velocities[i] = self.update_velocity(
                    x, v, p_best, self.g_best)
                self.particles_pos[i] = self.update_position(x, v)
                if self._get_fitness_int(self.particles_pos[i]) < self._get_fitness_int(p_best):
                    self.p_best[i] = self.particles_pos[i]
                if self._get_fitness_int(self.particles_pos[i]) < self._get_fitness_int(self.g_best):
                    self.g_best = self.particles_pos[i]
        return self.g_best

    def ـrandom_branches(self):
        branches = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        return random.sample(branches, 20)

    def _init_position(self):
        positions = []
        for i in range(self.n_particles):
            positions.append(self.ـrandom_branches())
        return positions


if __name__ == '__main__':
    distances = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        [1, 1, 9, 17, 25, 33, 42, 50, 58, 66, 74,
         82, 8, 12, 19, 26, 34, 42, 50, 59, 66],
        [2, 9, 2, 9, 17, 25, 33, 41, 50, 58, 66,
         74, 12, 8, 12, 18, 26, 34, 42, 50, 58],
        [3, 17, 9, 3, 8, 16, 25, 33, 41, 49, 58,
         66, 74, 12, 8, 11, 18, 26, 33, 42, 50],
        [4, 25, 17, 8, 4, 8, 17, 25, 33, 41, 49,
         57, 26, 18, 11, 8, 11, 18, 26, 34, 42],
        [5, 33, 25, 16, 8, 5, 9, 17, 25, 33, 41,
         49, 34, 26, 18, 11, 8, 12, 18, 26, 34],
        [6, 42, 33, 25, 17, 9, 6, 8, 17, 25, 33,
            41, 42, 34, 26, 18, 12, 8, 11, 18, 26],
        [7, 50, 41, 33, 25, 17, 8, 7, 9, 17, 25,
         33, 50, 42, 33, 26, 18, 11, 8, 12, 18],
        [8, 58, 50, 41, 33, 25, 17, 9, 8, 8, 16,
         24, 59, 50, 42, 34, 26, 18, 12, 8, 11],
        [9, 66, 58, 49, 41, 33, 25, 17, 8, 9, 8,
         16, 66, 58, 52, 42, 34, 26, 18, 11, 8],
        [10, 74, 66, 58, 49, 41, 33, 25, 16, 8, 10,
         8, 74, 66, 58, 50, 42, 33, 26, 18, 11],
        [11, 82, 74, 66, 57, 49, 41, 33, 24, 16, 8,
         11, 82, 74, 65, 58, 50, 41, 33, 25, 18],
        [12, 8, 12, 74, 26, 34, 42, 50, 59, 66, 74,
         82, 12, 9, 17, 25, 33, 42, 50, 58, 66],
        [13, 12, 8, 12, 18, 26, 34, 42, 50, 58, 66,
         74, 9, 13, 9, 17, 25, 33, 41, 50, 58],
        [14, 19, 12, 8, 11, 18, 26, 33, 42, 52, 58,
         65, 17, 9, 14, 8, 16, 25, 33, 41, 49],
        [15, 26, 18, 11, 8, 11, 18, 26, 34, 42, 50,
         58, 25, 17, 8, 15, 8, 17, 25, 33, 41],
        [16, 34, 26, 18, 11, 8, 12, 18, 26, 34, 42,
         50, 33, 25, 16, 8, 16, 9, 17, 25, 33],
        [17, 42, 34, 26, 18, 12, 8, 11, 18, 26, 33,
         41, 42, 33, 25, 17, 9, 17, 8, 17, 25],
        [18, 50, 42, 33, 26, 18, 11, 8, 12, 18, 26,
         33, 50, 41, 33, 25, 17, 8, 18, 9, 17],
        [19, 59, 50, 42, 34, 26, 18, 12, 8, 11, 18,
         25, 58, 50, 41, 33, 25, 17, 9, 19, 8],
        [20, 66, 58, 50, 42, 34, 26, 18, 11, 8, 11,
         18, 66, 58, 49, 41, 33, 25, 17, 8, 20],
    ]
costs = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, 1, 10, 0, 0, 0, 0, 0, 11, 14, 0,
     0, 12, 9, 10, 0, 0, 0, 12, 0, 11],
    [2, 10, 2, 10, 11, 0, 0, 0, 0, 18, 0,
     10, 13, 0, 14, 0, 0, 0, 9, 0, 12],
    [3, 0, 10, 3, 0, 0, 0, 10, 0, 11, 0, 9, 17, 0, 9, 0, 0, 0, 10, 0, 0],
    [4, 0, 11, 0, 4, 0, 9, 0, 0, 0, 0, 0, 11, 0, 12, 0, 0, 0, 9, 0, 0],
    [5, 0, 0, 0, 0, 5, 0, 0, 0, 0, 10, 0, 0, 0, 10, 0, 0, 0, 9, 0, 0],
    [6, 0, 0, 0, 9, 0, 6, 0, 9, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 0, 0, 10, 0, 0, 0, 7, 0, 0, 9, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0],
    [8, 11, 0, 0, 0, 0, 9, 0, 8, 12, 13, 0, 12, 0, 0, 0, 0, 0, 0, 0, 10],
    [9, 14, 18, 11, 0, 0, 0, 0, 12, 9, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 21],
    [10, 0, 0, 0, 0, 10, 9, 9, 13, 0, 10, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0],
    [11, 0, 10, 9, 0, 0, 0, 0, 0, 10, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 11],
    [12, 12, 13, 17, 11, 0, 0, 7, 12, 0,
     0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0],
    [13, 9, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 13, 0, 0, 0, 0, 0, 0, 0],
    [14, 10, 14, 9, 12, 10, 0, 0, 0, 0, 0,
     0, 0, 0, 14, 0, 0, 0, 0, 13, 12],
    [15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0],
    [16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0],
    [17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0, 0, 9],
    [18, 12, 9, 10, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 0, 0],
    [19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 19, 0],
    [20, 11, 12, 0, 0, 0, 0, 0, 10, 21, 0,
     11, 0, 0, 12, 0, 0, 9, 0, 0, 20],
]
PSO_s = PSO(distances, costs,  n_particles=50)
res_s = PSO_s.run()
print(res_s)
