while True:
    try:
        number = int(input('What is your favourite number'))
        print('The number 36 divided by, number,   result is', (36/number))
        break

    except ValueError:
        print('Please enter a number')

    except ZeroDivisionError:
        print('The number should not be a zero')

    finally:
        print('Loops end')


