# Local
from .base import BaseManifold as Manifold
from .euclidean import Euclidean
from .stereographic import Stereographic

euclidean = Euclidean()
stereographic = Stereographic()


__all__ = [
    "Manifold",
    "Euclidean",
    "euclidean",
    "Stereographic",
    "stereographic",
]
