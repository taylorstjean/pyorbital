from base import Bd, constants, time
import numpy as np


def forces():
    force = {}
    for i in Bd.get_instances():
        force[i.id] = np.array([0, 0, 0])
        for j in Bd.get_instances():
            if j != i:

                try:
                    r = np.subtract(np.array(i.position), np.array(j.position))
                except Exception:
                    raise TypeError("position attribute must be a horizontal position vector [float, float, float]")

                f = -constants.G * ((i.mass * j.mass) / (np.linalg.norm(r) ** 3)) * r
                force[i.id] = np.add(force[i.id], f)
    return force


def update_pos_vel(force: dict):

    for i in Bd.get_instances():
        p_prime = np.add(i.mass * np.array(i.velocity), force[i.id] * time.dt)
        r_prime = np.array(i.position) + (p_prime/i.mass) * time.dt
        i.position = r_prime.tolist()
        i.velocity = p_prime / i.mass




