import gspread
from google.oauth2.service_account import Credentials

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
    print("Please enter your monthly expenses from the last month.")
    print("This should be 3 numbers, separated by commas.")
    print("Example: 550,300,200\n")

    monthly_expenses_data = input("Enter your monthly expenses here:\n")
    
    monthly_expenses = monthly_expenses_data.split(',')
    check_val(monthly_expenses)


def check_val(values):
    """
    Change all string datas to integeres.
    Raise a ValueError if strings cant be changed to integers
    or if there is not exactly 3 values entered by the user.
    """
    try:
        if len(values) != 3:
            raise ValueError(
                f"Exactly 3 values needed, you entered {len(values)}"
            )
    except ValueError as e:
        print(f"Incorrect data! {e}, please try again.")


get_monthly_expenses_data()