class Shape:
    def __init__(self, vertices: list , edges: list, inner_angles: list, is_regular: bool):
        self.vertices = vertices
        self.edges = edges
        self.inner_angles = inner_angles
        self.is_regular = is_regular

    def print_vertices(self):
        for i in range(len(self.vertices)):
            print(f"({self.vertices[i].x},{self.vertices[i].y})")
    
    def print_edges(self):
        for i in range(len(self.edges)):
            print(f"({self.edges[i].start_point.x},{self.edges[i].start_point.y})({self.edges[i].end_point.x},{self.edges[i].end_point.y})-->{self.edges[i].lenght}")
    
    def compute_area(self):
        raise NotImplementedError("Area")
    
    def compute_perimeter(self):
        raise NotImplementedError("Perimetro")

    def compute_inner_angles(self):
        angle_sum: int = 0
        for angle in self.inner_angles:
            angle_sum += angle
        return angle_sum