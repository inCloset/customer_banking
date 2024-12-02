# Module 3 - Customer Banking App

## Folder Structure

In the folder labeled **`module_3`**, you will find the following Python files:
- `Account.py`
- `cd_account.py`
- `saving_account.py`
- `customer_banking.py`

## Overview

The **`customer_banking.py`** file serves as the main program of the project. It manages interactions with users and calls the necessary classes to fetch data, perform mathematical computations, and display the results. Specifically, it computes and displays the interest earned on the user's current balance over a specified period. The project utilizes an **Object-Oriented Programming (OOP)** approach.

---

## File Details

### `cd_account.py`

This file handles computations related to CD (Certificate of Deposit) accounts.  
It calculates the interest earned using the formula:

**`interest = balance * (apr / 100 * months / 12)`**

**Key Features:**
- Overrides (updates) the initial balance and interest with user inputs.
- Computes the total balance and interest to two decimal places.
- Outputs the updated information to the user.

---

### `saving_account.py`

This file manages savings account computations.  
It uses the same formula as `cd_account.py` for interest calculation:

**`interest = balance * (apr / 100 * months / 12)`**

**Key Features:**
- Updates the initial balance and interest based on user input.
- Calculates and outputs the total balance and interest to two decimal places.

---

### `customer_banking.py`

This class serves as the entry point for the application. It:
- Prompts the user for basic account information, such as:
    - Current balance
    - Date of maturity
    - Current APR
- Calls external classes (`cd_account` and `saving_account`) to process data and compute updated account details.
- Displays the computed results to the user.

**Note:**  
This implementation does not include error checking for user inputs. Users are advised to input accurate data to ensure proper functionality.

---

## Resources

- **Bootcamp:** OSU-VIRT-AI-PT
- **Module:** 3
- **Challenge Files Version:** 1.0
- **Programming Language:** Python
- **Date:** November 2024
- **Bootcamp Portal:** [OSU Bootcamp](https://bootcampspot.instructure.com/calendar#view_name=month&view_start=2024-12-02:~:text=Background,3%20Challenge%20files)
