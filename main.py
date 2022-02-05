from base import models, view
import math

planet = models.Body(name="taylor", mass=5.9735e24, position=[-50e6, 0, 0], radius=6.378e6, velocity=[1e3, -1e3, 0])
planet2 = models.Body(name="mommy", mass=4.8675e24, position=[50e6, 0, 0], radius=6.051e6, velocity=[1.2e3, 1e3, -1e3])
planet3 = models.Body(name="matt", mass=6.4171e24, position=[0, math.sqrt(100e6 ** 2 - 50e6 ** 2), 0], radius=3.3895e6, velocity=[-2e3, 1e3, 1e3])

view.run()
