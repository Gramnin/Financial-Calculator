def pv(payment: float, rate: float, periods: float) -> float:
    payment = float(payment)
    rate = float(rate)
    periods = float(periods)
    compound = (1 + rate) ** periods
    numerator = compound - 1
    denominator = rate * compound
    factor = numerator / denominator
    return payment * factor

def fv(payment: float, rate: float, periods: float) -> float:
    payment = float(payment)
    rate = float(rate)
    periods = float(periods)
    compound = (1 + rate) ** periods
    numerator = compound - 1
    factor = numerator / rate
    return payment * factor

def get_value(func):
    payment = input("Payment value: ")
    rate = input("Interest rate: ")
    periods = input("Number of periods: ")
    out = func(payment, rate, periods)
    print("%.4f" % out)

if __name__ == '__main__':
    from menu_utils import menu_loop
    
    menu_loop([
        (1, "Present Value", get_value, pv),
        (2, "Future Value", get_value, fv),
    ])
