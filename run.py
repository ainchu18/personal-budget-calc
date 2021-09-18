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
    Change all string datas to integers.
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


def amend_worksheet(data, worksheet):
    """
    Obtains a list of integers to be amended into the worksheets,
    it also updates the relevant worksheet with the data provided.
    """
    print(f"Amending {worksheet} worksheet...Please stand by!\n")
    worksheet_to_amend = SHEET.worksheet(worksheet)
    worksheet_to_amend.append_row(data)
    print(f"{worksheet} worksheet amended successfully!\n")


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
    print("Loss or savings data calculated successfully!\n")
    loss_savings_data = []
    for budget, expenses in zip(budget_row, expenses_row):
        loss_savings = int(budget) - expenses
        loss_savings_data.append(loss_savings)

    return loss_savings_data


def get_last_5_entries_expenses():
    """
    Retrieves columns of data from the expenses worksheet,
    retrieves the last 5 entries from each column and
    returns data as list of lists.
    """
    expenses = SHEET.worksheet("expenses")

    columns = []
    for col in range(1, 4):
        column = expenses.col_values(col)
        columns.append(column[-5:])

    return columns


def calculate_budget_for_next_month(data):
    """
    Calculates and adjust the average budget for each expenses per month
    and budget to to expenses where money is more needed
    depending on the data in the last five months.
    """
    print("Calculating and adjusting budget for the next month...\n")
    new_budget_data = []

    for column in data:
        int_col = [int(num) for num in column]
        average_expenses = sum(int_col) / len(int_col)
        budget_data = average_expenses * 1.1

        new_budget_data.append(round(budget_data))
    return new_budget_data


def main():
    """
    Run all the program functions.
    """
    monthly_data = get_monthly_expenses_data()
    monthly_expenses = [int(num) for num in monthly_data]
    amend_worksheet(monthly_expenses, "expenses")
    new_loss_savings_data = calculate_loss_or_savings_data(monthly_expenses)
    amend_worksheet(new_loss_savings_data, "loss-or-savings")
    expenses_columns = get_last_5_entries_expenses()
    budget_allowance = calculate_budget_for_next_month(expenses_columns)
    amend_worksheet(budget_allowance, "budget")

    print("Thank you for using this program!\n")
    print("Budget wisely!")


print("Welcome to the Personal Budget Calculation Program\n")
main()
