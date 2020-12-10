bill = float(input("What is yout bill sub-total ").strip('$'))
tip = float(input("Percentage of tip: ").strip('%'))
total = float(bill*tip/100)

print(f"Your tip is $ {total}")