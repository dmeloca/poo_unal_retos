import package.shape as shape

class Rectangle(shape.Shape):
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