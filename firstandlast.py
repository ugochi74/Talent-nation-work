def last_and_first(value):
    if len(value) == 0:
        retrun {"first": "", "last": ""}
    return {
        "first": value[0]
        "last": value[-1]
    }