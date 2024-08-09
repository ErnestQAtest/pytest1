def test_for_Point_init(self):
    point1=Point(1,0)
    point2=Point("1","0")
    assert point1.x == float(1.0) and point1.y == float(0.0)
    assert point2.x == float(1.0) and point2.y == float(0.0)