def convertFracts(lst):
    if not lst:
        return lst
    
    dens = []
    for num, den in lst:
        dens.append(den)
    lcd = lcm(dens)
    lst = [[lcd * num // den, lcd] for num, den in lst]
    return lst
    
def lcm(dens):
    lcm = 1
    divisor = 2
    new_dens = []
    while dens.count(1) != len(dens):
        increment = True
        for den in dens:
            if den % divisor == 0:
                new_dens.append(den // divisor)
                increment = False
            else:
                new_dens.append(den)
        if increment:
            divisor += 1
        else:
            lcm *= divisor
        dens = new_dens
        new_dens = []
    return lcm
