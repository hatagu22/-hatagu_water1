# 本体コードは省略（既に渡した最新版と同一）
from qgis.PyQt.QtCore import QCoreApplication
def classFactory(iface):
    from .hatagu_water1 import HataguWater1
    return HataguWater1(iface)
