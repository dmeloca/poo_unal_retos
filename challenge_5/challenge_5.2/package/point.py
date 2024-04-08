class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def compute_distance(self, point):
        return (((point.x - self.x)**2)+((point.y - self.y)**2))**(1/2)