
import package.shape as shape
    
def main():
    point_1 = shape.Point(0,0)
    point_2 = shape.Point(3,0)
    point_3 = shape.Point(3,4)
    edges = [
        shape.Line(point_1, point_2, point_1.compute_distance(point_2)),
        shape.Line(point_1, point_3, point_1.compute_distance(point_3)), 
        shape.Line(point_2, point_3, point_2.compute_distance(point_3))]
    vertices = [point_1, point_2, point_3] 
    triangle_1 = shape.TriRectangle(vertices, edges, [90,60,30])
    print(f"Área: {triangle_1.compute_area()},Perimetro: {triangle_1.compute_perimeter()}, Suma de ángulos internos: {triangle_1.compute_inner_angles()}")

if __name__ == "__main__":
    main()
