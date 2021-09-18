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


monthly_data = get_monthly_expenses_data()
monthly_expenses = [int(num) for num in monthly_data]
amend_monthly_expenses_worksheet(monthly_expenses)
