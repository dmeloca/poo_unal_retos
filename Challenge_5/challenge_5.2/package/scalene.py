import package.triangle as triangle

class Scalene(triangle.Triangle):
    def __init__(self, vertices: list, edges: list, inner_angles: list, is_regular: bool = True):
        super().__init__(vertices, edges, inner_angles, is_regular)

    def compute_area(self):
        semi_perimeter = self.compute_perimeter()/2
        return (semi_perimeter*(semi_perimeter - self.edges[0])*(semi_perimeter - self.edges[1])*(semi_perimeter -self.edges[2]))**(1/2)
