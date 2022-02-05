from vpython import *
from base import Bd, controllers

scene = canvas(title='Simulation', width=1300, height=700)


def run():

    bodies = {}

    controllers.forces()

    for i in Bd.get_instances():

        pos_vector = vector(i.position[0], i.position[1], i.position[2])

        bodies[i.id] = sphere(make_trail=True, color=color.red, trail_color=color.cyan, trail_radius=5e5)
        bodies[i.id].pos = pos_vector
        bodies[i.id].radius = i.radius

    while True:

        rate(100)

        forces = controllers.forces()
        controllers.update_pos_vel(forces)

        for i in Bd.get_instances():

            pos_vector = vector(i.position[0], i.position[1], i.position[2])

            bodies[i.id].pos = pos_vector

