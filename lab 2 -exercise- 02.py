

def long_division_tool():
    try:
        num = int(input('Enter a numerator:'))

        den = int(input('Enter a denominator:'))



        if den == 0:
                  print('Sorry, you may not devide by zero.')
                  print('Exiting...')
        else:
            quotient = num // den
            remainder = num % den
            
            
        print(f"{num} / {den} = {quotient} Remainder {remainder}")

    except ValueError:
            print("Invalid input. Please enter integers only.")
            
    print("Exiting...")

if __name__ == "__main__":
    long_division_tool()
