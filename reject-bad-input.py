def solution(value):
    try:
        float_number = float(value)
        return round(float_number * 2, 2)
    except ValueError:
        return "Invalid number"
