def clean_username(value):
    clean = value.strip().lower()
    return clean.replace(" ", "_")
