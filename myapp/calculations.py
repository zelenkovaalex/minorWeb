def calculate_x(a):
    """
    Дано вещественное число A. Вычислить х = a**2+4+5  при а < 62; в противном случае x = 1/(a**2) + 4a + 5).

    """
    try:
        a = float(a)  
        if a < 62:
            x = a**2 + 4 + 5
        else:
            x = 1 / (a**2) + 4 * a + 5
        return x
    except ValueError:
        return None 