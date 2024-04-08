import package.shape as shape
class Triangle(shape.Shape):
    def __init__(self, vertices: list, edges: list, inner_angles: list, is_regular: bool = True ):
        super().__init__(vertices, edges, inner_angles, is_regular)
    
    def compute_perimeter(self):
        perimeter: int = 0
        for edge in self.edges:
            perimeter += edge.lenght
        return perimeter