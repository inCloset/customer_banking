# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
import cd_account as cd
import savings_account as sa
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input('What is the remaining balance of your savings account: '))
    print(f'${round(savings_balance, 2)}')
    savings_interest = float(input('Please provide the current interest earned of your savings account: '))
    print(f'current interest: {round(savings_interest, 2)}%')
    savings_maturity = int(input('Please provide the maturity date: '))
    print(f'maturity date: {savings_maturity}')

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = sa.create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f'Your account has accumulated {interest_earned} and new Savings account Balance $:{updated_savings_balance}')

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input('What is the remaining balance of your cd account: '))
    print(f'${round(cd_balance, 2)}')
    cd_interest = float(input('Please provide the current interest earned of your cd account: '))
    print(f'current interest: {round(cd_interest, 2)}')
    cd_maturity = int(input('Please provide the maturity date: '))
    print(f'maturity date: {cd_maturity}')
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = cd.create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f'Your account has accumulated {round(interest_earned,2)} and new CD Account Balance $:{updated_cd_balance}')


if __name__ == "__main__":
    # Call the main function.
    main()