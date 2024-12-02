import cd_account as cd
import savings_account as sa
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    savings_balance = float(input('What is the remaining balance of your savings account: '))
    print(f'${round(savings_balance, 2)}')
    savings_interest = float(input('Please provide the current interest earned of your savings account: '))
    print(f'current interest: {round(savings_interest, 2)}%')
    savings_maturity = int(input('Please provide the maturity date: '))
    print(f'maturity date: {savings_maturity}')
    updated_savings_balance, interest_earned = sa.create_savings_account(savings_balance, savings_interest, savings_maturity)
    print(f'Your account has accumulated ${interest_earned} in interest, and updated Savings account Balance: ${updated_savings_balance}')
    cd_balance = float(input('What is the remaining balance of your cd account: '))
    print(f'${round(cd_balance, 2)}')
    cd_interest = float(input('Please provide the current interest earned of your cd account: '))
    print(f'current interest: {round(cd_interest, 2)}')
    cd_maturity = int(input('Please provide the maturity date: '))
    print(f'maturity date: {cd_maturity}')
    updated_cd_balance, interest_earned = cd.create_cd_account(cd_balance, cd_interest, cd_maturity)
    print(f'Your account has accumulated ${round(interest_earned,2)} in interest, and updated CD Account Balance: ${updated_cd_balance}')

if __name__ == "__main__":
    main()