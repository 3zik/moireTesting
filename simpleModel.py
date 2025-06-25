import pybinding as pb
from pybinding.repository import graphene


# Example: build twisted bilayer graphene
model = pb.Model(
    graphene.bilayer(),
    pb.moire(angle=1.05),   # twist angle in degrees
    pb.rectangle(50, 50),   # system size (nm)
)
model.plot()

