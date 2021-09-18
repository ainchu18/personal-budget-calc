import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('PersonalBudgetCalc')


def get_monthly_expenses_data():
    """
    Get users monthly expenses input.
    """
    while True:
        print("Please enter your monthly expenses from the last month.")
        print("This should be 3 numbers, separated by commas.")
        print("Example: 550,300,200\n")

        monthly_expenses_data = input("Enter your monthly expenses here:\n")
        
        monthly_expenses = monthly_expenses_data.split(',')
        
        if check_val(monthly_expenses):
            print("The values are valid!\n")
            break

    return monthly_expenses


def check_val(values):
    """
    Change all string datas to integeres.
    Raise a ValueError if strings cant be changed to integers
    or if there is not exactly 3 values entered by the user.
    """
    try:
        [int(value) for value in values]
        if len(values) != 3:
            raise ValueError(
                f"Exactly 3 values needed, you entered {len(values)}"
            )
    except ValueError as e:
        print(f"Incorrect data! {e}, please try again.\n")
        return False

    return True


def amend_monthly_expenses_worksheet(data):
    """
    Amend the monthly expenses worksheet.
    Add a new row with the data provided.
    """
    print("Amending monthly expenses worksheet...Please stand by!\n")

    expenses_worksheet = SHEET.worksheet('expenses')
    expenses_worksheet.append_row(data)

    print("Expenses worksheet amended successfully!\n")


def amend_monthly_loss_or_savings_worksheet(data):
    """
    Amend the monthly loss or savings worksheet.
    Add a new row with the data provided.
    """
    print("Amending monthly loss or savings worksheet...Please stand by!\n")

    loss_or_savings_worksheet = SHEET.worksheet('loss-or-savings')
    loss_or_savings_worksheet.append_row(data)

    print("Loss or savings worksheet amended successfully!\n")


def calculate_loss_or_savings_data(expenses_row):
    """
    Compare monthly budget to the monthly expenses,
    and calculate for loss or savings.
    A positive number indicates savings.
    On one hand, a negative result indicates that the user
    spent more than his monthly budget for that specific monthly budget.
    """
    print("Calculating loss or savings...Please standby!\n")
    budget = SHEET.worksheet('budget').get_all_values()
    budget_row = budget[-1]
    
    loss_savings_data = []

    for budget, expenses in zip(budget_row, expenses_row):
        loss_savings = int(budget) - expenses
        loss_savings_data.append(loss_savings)

    return loss_savings_data


def main():
    """
    Run all the program functions.
    """
    monthly_data = get_monthly_expenses_data()
    monthly_expenses = [int(num) for num in monthly_data]
    amend_monthly_expenses_worksheet(monthly_expenses)
    new_loss_savings_data = calculate_loss_or_savings_data(monthly_expenses)
    amend_monthly_loss_or_savings_worksheet(new_loss_savings_data)


print("Welcome to the Personal Budget Calculation Program\n")
main()