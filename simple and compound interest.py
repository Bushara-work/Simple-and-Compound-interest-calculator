import math
from decimal import *

def get_rounded_input(prompt):
    user_input = input(prompt)
    try:
        number = Decimal(user_input)
        rounded_number = (number * 20).quantize(Decimal('1'), rounding=ROUND_HALF_UP) / 20
        print(f"Rounded number: {rounded_number}")
    except Exception as e:
        print(f"Invalid input: {e}")

def get_int_input(prompt):
    while True:
        try:
            return Decimal(int(input(prompt)))
        except ValueError:
            print("Please enter a valid integer.")


def main():
    print("Choose the type of interest calculation:")
    print("1. Simple Interest")
    print("2. Compound Interest")
    while True:
        choice = get_int_input("Enter 1 or 2: ")
        if choice in [1, 2]:
            break

    if choice == 1:
        print("Simple Interest Calculation")
        print("Choose the variable to solve for:")
        print("1. Principal Value")
        print("2. Interest Earned")
        print("3. Interest Rate")
        print("4. Time")
        while True:
            variable = get_int_input("Enter 1, 2, 3, or 4: ")
            if variable in [1, 2]:
                break
        

        if variable == 1:
            interest = get_rounded_input("Enter the interest amount (in dollars): ")
            rate = get_rounded_input("Enter the rate of interest (in percentage): ")
            time = get_rounded_input("Enter the time period (in years): ")
            principal = interest / ((rate/100) * time)

            print(f"Principal: {principal:.2f} dollars")
        
        elif variable == 2:
            principal = get_rounded_input("Enter the principal amount (in dollars): ")
            rate = get_rounded_input("Enter the rate of interest (in percentage): ")
            time = get_rounded_input("Enter the time period (in years): ")
            interest = principal * (rate/100) * time
            print(f"Interest: {interest:.2f} dollars")

        elif variable == 3:
            principal = get_rounded_input("Enter the principal amount (in dollars): ")
            interest = get_rounded_input("Enter the interest amount (in dollars): ")
            time = get_rounded_input("Enter the time period (in years): ")
            rate = interest / (principal * time)
            print(f"Rate: {rate:.2f} %")

        elif variable == 4:
            principal = get_rounded_input("Enter the principal amount (in dollars): ")
            interest = get_rounded_input("Enter the interest amount (in dollars): ")
            rate = get_rounded_input("Enter the rate of interest (in percentage): ")
            time = interest / (principal * (rate/100))
            print(f"Time: {time:.2f} years")


    elif choice == 2:
        print("Compound Interest Calculation")
        print("Choose the variable to solve for:")
        print("1. Principal/Initial Value")
        print("2. Final/Total Value")
        print("3. Interest - Earned")
        print("4. Interest - Rate/Percent")
        print("5. Time - In years")
        print("6. Compounding Period - Yearly")

        while True:
            variable = get_int_input("Enter 1, 2, 3, 4, 5, or 6: ")
            if variable in [1,2,3,4,5,6]:
                break

        #Principal/Initial Value
        if variable == 1:
            while True:
                have_interest_earned = input("Do you have the interest earned? (yes/no) ").lower()
                if have_interest_earned in ['yes', 'no']:
                    break

            final = get_rounded_input("Enter the Final/Total amount (in dollars): ")

            if have_interest_earned == 'yes':
                interest_earned = get_rounded_input("Enter the amount of interest earned (in dollars): ")
                principal = final - interest_earned
                          
            elif have_interest_earned == 'no':
                rate = get_rounded_input("Enter the rate of interest (in percentage): ")
                time = get_rounded_input("Enter the time period (in years): ")
                compound = get_rounded_input("Enter the number of compounding periods per year: ")
                    
                principal = final / (1+((rate/100)/compound))**(compound*time)
                    
            print(f"Principal Value: {principal:.2f} dollars")
        
        #Final/Total Value
        elif variable == 2:
            while True:
                have_interest_earned = input("Do you have the interest earned?")
                have_interest_earned = have_interest_earned.lower()
                if have_interest_earned in ['yes', 'no']:
                    break

            principal = get_rounded_input("Enter the principal amount (in dollars): ")

            if have_interest_earned == 'yes':
                interest_earned = get_rounded_input("Enter the amount of interest earned (in dollars): ")
                
                final = principal + interest_earned
            
            elif have_interest_earned == 'no':
                rate = get_rounded_input("Enter the rate of interest (in percentage): ")
                time = get_rounded_input("Enter the time period (in years): ")
                compound = get_rounded_input("Enter the number of compounding periods per year: ")
                
                final = principal * (1 + (rate/compound))**(compound*time)
            
            print(f"Final/Total Value: {final:.2f} dollars")
        
        #Interest earned
        elif variable == 3:
            while True:
                have_final_or_principal_or_both = input("Do you have the principal value, the final value or both?").lower()

                if have_final_or_principal_or_both in ['both', 'principal value', 'final value']:
                    break
            
            if have_final_or_principal_or_both == 'both':
                principal = get_rounded_input("Enter the principal amount (in dollars): ")

                final = get_rounded_input("Enter the Final/Total Value (in dollars): ")
                interest_earned = final - principal

            elif have_final_or_principal_or_both == 'principal value':
                principal = get_rounded_input("Enter the principal amount (in dollars): ")
                rate = get_rounded_input("Enter the rate of interest (in percentage): ")
                time = get_rounded_input("Enter the time period (in years): ")
                compound = get_rounded_input("Enter the number of compounding periods per year: ")
                interest_earned = principal * (1 + rate/100 / compound)**(compound*time) - principal

             
            elif have_final_or_principal_or_both == 'final value':
                final = get_rounded_input("Enter the Final/Total Value (in dollars): ")
                rate = get_rounded_input("Enter the rate of interest (in percentage): ")
                time = get_rounded_input("Enter the time period (in years): ")
                compound = get_rounded_input("Enter the number of compounding periods per year: ")

                principal = final / (1+((rate/100)/compound))**(compound*time)

                interest_earned = final - principal
    
            print(f"Interest Earned: {interest_earned:.2f}")        
        
        #pythons math.sqrt(x) could also work here
        elif variable == 4:
            while True:
                have_principal_or_final_or_earned_interst = input("Which value do you NOT have,the principal value, the final value, or the interest earned?").lower()

                if have_principal_or_final_or_earned_interst in ['principal value', 'final value', 'interest earned']:
                    break

            time = get_rounded_input("Enter the time period (in years): ")
            compound = get_rounded_input("Enter the number of compounding periods per year: ")

            if have_principal_or_final_or_earned_interst == 'principal value':
                final = get_rounded_input("Enter the Final/Total Value (in dollars): ")
                interest_earned = get_rounded_input("Enter the interest amount (in dollars): ")

                rate = compound * ((final/(final-interest_earned)) ** (1 / (compound * time )) - 1)
            
            elif have_principal_or_final_or_earned_interst == 'final value':
                principal = get_rounded_input("Enter the principal amount (in dollars): ")
                interest_earned = get_rounded_input("Enter the interest amount (in dollars): ")

                rate = compound * (((principal + interest_earned)/principal) ** (1 / (compound * time )) - 1)

            elif have_principal_or_final_or_earned_interst == 'interest earned':
                principal = get_rounded_input("Enter the principal amount (in dollars): ")
                final = get_rounded_input("Enter the Final/Total Value (in dollars): ")

                rate = compound * ((final/principal) ** (1 / (compound * time)) - 1)
        
            rate = rate * 100
            print(f"Rate: {rate:.2f} %")
        



        elif variable == 5:
            while True:
                have_principal_or_final_or_earned_interst = input("Which value do you NOT have,the principal value, the final value, or the interest earned?").lower()

                if have_principal_or_final_or_earned_interst in ['principal value', 'final value', 'interest earned']:
                    break
            
            rate = get_rounded_input("Enter the rate of interest (in percentage): ")
            compound = get_rounded_input("Enter the number of compounding periods per year: ")

            if have_principal_or_final_or_earned_interst == 'principal value':
                final = get_rounded_input("Enter the Final/Total Value (in dollars): ")
                interest_earned = get_rounded_input("Enter the interest amount (in dollars): ")

                time = math.log(final/(final - interest_earned)) / (compound * math.log(1 + rate/100 /compound))
            
            elif have_principal_or_final_or_earned_interst == 'final value':
                principal = get_rounded_input("Enter the principal amount (in dollars): ")
                interest_earned = get_rounded_input("Enter the interest amount (in dollars): ")

                time = math.log((principal + interest_earned)/principal) / (compound * math.log(1 + rate/100 /compound))

            elif have_principal_or_final_or_earned_interst == 'interest earned':
                principal = get_rounded_input("Enter the principal amount (in dollars): ")
                final = get_rounded_input("Enter the Final/Total Value (in dollars): ")

                time = math.log(final/principal) / (compound * math.log(1 + rate/100 /compound))
            
            print(f"Time: {time:.2f} years")
        
        
        
        
        elif variable == 6:
            principal = get_rounded_input("Enter the principal amount (in dollars): ")
            final = get_rounded_input("Enter the Final/Total Value (in dollars): ")
            interest_earned = get_rounded_input("Enter the interest amount (in dollars): ")
            rate = get_rounded_input("Enter the rate of interest (in percentage): ")
            time = get_rounded_input("Enter the time period (in years): ")

            
            while True:
                print("A tolerance value must be larger than 0, and include one '.'")
                tolerance = input("What tolerance do you want (for the difference between real and approximate/rounded final value)")

                if tolerance.count('.') == 1:
                    parts = tolerance.split('.')
                    if parts[0].isdigit() and parts[1].isdigit():
                        if int(parts[0]) > 0 or int(parts[1]) > 0 or int(parts[1]) > 28:
                            break
                    #print("Invalid input. Please try again.")

            tolerance= parts[0] + '.' + parts[1]
            tolerance = Decimal(tolerance)

            # Initialize n
            compound = Decimal(0.01)

            # Iterate to find the correct n
            while True:
                calculated_final = principal * (1 + (rate / compound)) ** (compound * time)
                if abs(calculated_final - final) < tolerance:  # Check if the calculated A is close enough to the given A   
                    break


                if compound >= 1000:
                    print("The N value is rather incredibly high and cannot be computed")
                    print("or")
                    print("The n value does not fit in any specified tolerance")
                    print("or")
                    print("This program cannot calculate the compounding periods due to issues with the values recieved (n will never result in a negative even if the values require it)")
                    print("Otherwise:")
                    break
                
                compound += Decimal(0.01)

            # Print the result
            print(f"The value of n is approximately: {compound:.2f}")


if __name__ == "__main__":
    main()
