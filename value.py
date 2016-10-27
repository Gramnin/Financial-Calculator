def pv(payment, rate, periods):
    payment = float(payment)
    rate = float(rate)
    periods = float(periods)
    compound = (1 + rate) ** periods
    numerator = compound - 1
    denominator = rate * compound
    factor = numerator / denominator
    return payment * factor

def fv(payment, rate, periods):
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
    return True

if __name__ == '__main__':
    import menu
    
    mainmenu = menu.Menu("Select a calculation: ")
    mainmenu.add_option({
        "title": "Present Value",
        "function": get_value,
        "arguments": [pv],
    })
    mainmenu.add_option({
        "title": "Future Value",
        "function": get_value,
        "arguments": [fv],
    })
    
    valid = True
    while valid:
        valid = mainmenu.run()
