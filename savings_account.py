"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account as acct
# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    acct(0.00, 0)
    interest_earned = round(float(balance * (interest_rate/100 * months/12)),2)
    balance = round(float(balance + interest_earned), 2)
    acct(0, 0).set_balance(balance=balance)
    acct(0,0).set_interest(interest=interest_earned)
    return balance, interest_earned
