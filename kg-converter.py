def solution(kilograms):
    k_grams = float(kilograms)
    grams = k_grams * 1000
    pounds = round(k_grams*2.20462, 2)
    return f"Kilograms: {k_grams}\nGrams: {grams}\nPounds: {pounds}"

