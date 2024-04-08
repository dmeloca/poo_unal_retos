import package.rectangle as rectangle
class Square(rectangle.Rectangle):
    def __init__(self, vertices: list, edges: list, inner_angles: list = [90,90,90,90] , is_regular: bool = True):
        super().__init__(vertices, edges, inner_angles, is_regular)

    def compute_area(self):
        base = self.edges[0].lenght
        return base**2
    
    def compute_perimeter(self):
        base = self.edges[0].lenght
        return 4*base