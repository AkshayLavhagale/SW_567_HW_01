""" Name - Akshay Lavhagale
    HW 01: Testing triangle classification
    The function returns a string that specifies whether the triangle is scalene, isosceles, or equilateral,
    and whether it is a right triangle as well. """


def classify_triangle(a, b, c):
    # This function will tell us whether the triangle is scalene, isosceles, equilateral or right triangle
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        raise ValueError("The input value is not number")
    else:
        [a, b, c] = sorted([a, b, c])  # sorting the values of a, b and c so it would always remain in order
        if (a + b < c and a + c < b and b + c < a) or (a or b or c) <= 0:
            """ The Triangle Inequality Theorem states that the sum of any 2 sides of a triangle must be greater
                than the measure of the third side. Also none of the side should be equal to zero """
            return "This is not a triangle"
        elif a ** 2 + b ** 2 == c ** 2:
            if a != b or a != c or b != c:
                return "Right and Scalene Triangle"
            if a == b or a == c or b == c:
                return "Isosceles and Right Triangle"
        elif a == b == c:
            return "Equilateral"
        if a == b or a == c or b == c:
            return "Isosceles"
        else:
            return "Scalene"


def run_classify_triangle(a, b, c):
    # Invoke classify_triangle with the specified arguments and print the result
    print('classify_triangle(', a, ',', b, ',', c, ')=', classify_triangle(a, b, c), sep="")

