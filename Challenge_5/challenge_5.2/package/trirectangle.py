import package.triangle as triangle

class TriRectangle(triangle.Triangle):
    def __init__(self, vertices: list, edges: list, inner_angles: list, is_regular: bool = True):
        super().__init__(vertices, edges, inner_angles, is_regular)
    
    def compute_area(self):
        a_base = self.edges[0].lenght
        b_base = self.edges[1].lenght
        for edge in self.edges:
            if edge.lenght < a_base and edge.lenght < b_base:
                a_base = edge.lenght
            elif edge.lenght > a_base and edge.lenght < b_base:
                b_base = edge.lenght
        return (a_base * b_base)/2
