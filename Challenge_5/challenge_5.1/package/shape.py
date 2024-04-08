class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def compute_distance(self, point):
        return (((point.x - self.x)**2)+((point.y - self.y)**2))**(1/2)

class Line:
    def __init__(self, start_point: Point , end_point: Point , lenght: float ):
        self.start_point = start_point
        self.end_point = end_point
        self.lenght = start_point.compute_distance(end_point)

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

    
class Rectangle(Shape):
    def __init__(self, vertices, edges, inner_angles = [90,90,90,90], is_regular = True):
        super().__init__(vertices, edges, inner_angles, is_regular)
    
    def find_base_n_height(object):
        sides_lenght = []
        for edge in object.edges:
            sides_lenght.append(edge.lenght)
        return max(sides_lenght), min(sides_lenght)
    
    def compute_area(self):
        base, height = self.find_base_n_height(self)
        return base * height
    
    def compute_perimeter(self):
        base,height = self.find_base_n_height(self)
        return 2*(base+height)

class Square(Rectangle):
    def __init__(self, vertices: list, edges: list, inner_angles: list = [90,90,90,90] , is_regular: bool = True):
        super().__init__(vertices, edges, inner_angles, is_regular)

    def compute_area(self):
        base = self.edges[0].lenght
        return base**2
    
    def compute_perimeter(self):
        base = self.edges[0].lenght
        return 4*base

class Triangle(Shape):
    def __init__(self, vertices: list, edges: list, inner_angles: list, is_regular: bool = True ):
        super().__init__(vertices, edges, inner_angles, is_regular)
    
    def compute_perimeter(self):
        perimeter: int = 0
        for edge in self.edges:
            perimeter += edge.lenght
        return perimeter
    
class Equilateral(Triangle):
    def __init__(self, vertices: list, edges: list, inner_angles: list = [60, 60, 60], is_regular: bool = True):
        super().__init__(vertices, edges, inner_angles, is_regular)
    
    def compute_area(self):
        height = ((self.edges[0].lenght)**2-(self.edges[0].lenght/2)**2)**(1/2)
        return height

class TriRectangle(Triangle):
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

class Isosceles(Triangle):
    def __init__(self, vertices: list, edges: list, inner_angles: list, is_regular: bool = True):
        super().__init__(vertices, edges, inner_angles, is_regular)

    def compute_area(self):
        a_base = self.edges[0].lenght
        b_base = self.edges[1].lenght
        for edge in self.edges:
            if a_base > edge.lenght and b_base > edge.lenght:
                a_base = edge.lenght
            elif a_base < edge.lenght:
                b_base = edge.lenght
        return (a_base*b_base)/2
    
class Scalene(Triangle):
    def __init__(self, vertices: list, edges: list, inner_angles: list, is_regular: bool = True):
        super().__init__(vertices, edges, inner_angles, is_regular)

    def compute_area(self):
        semi_perimeter = self.compute_perimeter()/2
        return (semi_perimeter*(semi_perimeter - self.edges[0])*(semi_perimeter - self.edges[1])*(semi_perimeter -self.edges[2]))**(1/2)

