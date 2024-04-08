import package.point as point

class Line:
    def __init__(self, start_point: point.Point , end_point: point.Point , lenght: float ):
        self.start_point = start_point
        self.end_point = end_point
        self.lenght = start_point.compute_distance(end_point)