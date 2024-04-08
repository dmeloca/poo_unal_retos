import package.triangle as triangle

class Equilateral(triangle.Triangle):
    def __init__(self, vertices: list, edges: list, inner_angles: list = [60, 60, 60], is_regular: bool = True):
        super().__init__(vertices, edges, inner_angles, is_regular)
    
    def compute_area(self):
        height = ((self.edges[0].lenght)**2-(self.edges[0].lenght/2)**2)**(1/2)
        return height