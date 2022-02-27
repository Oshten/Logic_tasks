

def solution_of_equation(coefficient_а, coefficient_b, coefficient_c):
    """Решение квадратного уравнения"""
    if coefficient_а == 0 and coefficient_b == 0:
        return {'x_1': 'no decision', 'x_2': 'no decision'}
    elif coefficient_а == 0:
        decision = (- coefficient_c)/coefficient_b
        return {'x_1': str(decision), 'x_2': str(decision)}
    elif coefficient_b**2 - 4 * coefficient_а * coefficient_c < 0:
        return {'x_1': 'no decision', 'x_2': 'no decision'}
    elif coefficient_b**2 - 4 * coefficient_а * coefficient_c == 0:
        decision = round((- coefficient_b) / (2 * coefficient_а), 2)
        return {'x_1': str(decision), 'x_2': str(decision)}
    elif coefficient_b**2 - 4 * coefficient_а * coefficient_c > 0:
        x_1 = round((- coefficient_b + (
                coefficient_b ** 2 - 4 * coefficient_а * coefficient_c)**(0.5)) / (2 * coefficient_а), 2)
        x_2 = round((- coefficient_b - (
                coefficient_b ** 2 - 4 * coefficient_а * coefficient_c)**(0.5)) / (2 * coefficient_а), 2)
        return {'x_1': str(x_1), 'x_2': str(x_2)}