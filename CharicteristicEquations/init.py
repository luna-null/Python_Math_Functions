# Initial Conditions
def initialConditions():
    t0Init = float(input("What are the initial conditions, if they exist?\nt0 = "))
    y_t0_Init = float(input("y(t0) = "))
    dy_t0_Init = float(input("y`(t0) = "))
    
    if type(t0Init) == float and type(y_t0_Init) == float and type(dy_t0_Init) == float:
        return t0Init, y_t0_Init, dy_t0_Init
    else:
        actuallyNoInit = input("Are you sure there are initial conditions? ").lower()
    if actuallyNoInit == "y" or actuallyNoInit == "yes" or actuallyNoInit == "true" or actuallyNoInit == "1":
        initialConditions()
    else:
        initCond = False
        return initCond
