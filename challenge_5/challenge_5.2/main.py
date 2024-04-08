import package.point as point
import package.line as line
import package.trirectangle as trirectangle
import package.equilateral as equilateral
import package.isosceles as isosceles
import package.rectangle as rectangle
import package.scalene as scalene
import package.square as square


def main():
    point_1 = point.Point(0,0)
    point_2 = point.Point(3,0)
    point_3 = point.Point(3,4)
    edges = [
        line.Line(point_1, point_2, point_1.compute_distance(point_2)),
        line.Line(point_1, point_3, point_1.compute_distance(point_3)), 
        line.Line(point_2, point_3, point_2.compute_distance(point_3))]
    vertices = [point_1, point_2, point_3] 
    triangle_1 = trirectangle.TriRectangle(vertices, edges, [90,60,30])
    print(f"Área: {triangle_1.compute_area()},Perimetro: {triangle_1.compute_perimeter()}, Suma de ángulos internos: {triangle_1.compute_inner_angles()}")

if __name__ == "__main__":
    main()
