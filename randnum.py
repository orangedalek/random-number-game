random_integer = randint(1, 10)

    while True:
        print "Guess the random number between 1 and 10!"

    guess = raw_input

    if raw_input == random_integer:
        print "YAAAYYYY, you got it!"
    elif raw_input > random_integer:
        print "too high!"
    elif raw_input < random_integer:
        print "Too low!"