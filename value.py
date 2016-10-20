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

if __name__ == '__main__':
    import sys
    
    type = None
    if len(sys.argv) > 1:
        type = sys.argv[1]
    eq = {
        'pv': pv,
        'fv': fv,
    }
    while type not in eq:
        try:
            type = input('Type (%s): ' % ', '.join(sorted(eq.keys())))
        except KeyboardInterrupt:
            print()
            sys.exit(0)
    eq = eq[type]
    if len(sys.argv) >= 5:
        payment, rate, periods = sys.argv[2:5]
    else:
        try:
            payment = input('Payment: ')
            rate = input('Rate: ')
            periods = input('Periods: ')
        except KeyboardInterrupt:
            print()
            sys.exit(0)
    
    print(eq(payment, rate, periods))
