from collections import defaultdict
import weakref
import itertools


class KeepRefs(object):
    __refs__ = defaultdict(list)

    def __init__(self):
        self.__refs__[self.__class__].append(weakref.ref(self))

    @classmethod
    def get_instances(cls):
        for inst_ref in cls.__refs__[cls]:
            inst = inst_ref()
            if inst is not None:
                yield inst


class Body(KeepRefs):

    id_iter = itertools.count()

    def __init__(self, name="Default", mass=None, velocity=None, radius=None, position=None):
        super(Body, self).__init__()

        self.id = next(self.id_iter)

        if velocity is None:
            velocity = [1.0, 1.0, 1.0]
        if position is None:
            position = [0.0, 0.0, 0.0]

        self.name = name
        self.mass = mass
        self.velocity = velocity
        self.position = position
        self.radius = radius
