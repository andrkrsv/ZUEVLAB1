def greatestCD(number):
    number = number<<0
    GCD = 1
    while(number&1==0):
        number  = number >> 1
        print(f"DEBUG: Number = {number}")
        GCD = GCD << 1 
        print(f"DEBUG: GCD = {GCD}")
    return GCD
    
