tip_scale = {"low":.15, "average":.18, "high":.20}
def tip_calculator(subtotal, quality):
    if quality not in tip_scale:
        print("Unrecognized Service Quality.")
        print("Available options are: low, average, high.")
        return -1, -1
    rate = tip_scale[quality]
    tip = subtotal * rate
    total = subtotal + tip
    return tip, total