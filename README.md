# Personal Budget Calculation Program
---
Developer : JKCC

[Go to the website](https://personal-budget-calculation.herokuapp.com/)

---
![App Image](docs/images/readme/app-image.png)

---
## Table of Contents
---
1. [Goals](#goals)
    * [Users Goals](#user-goals)
    * [Developer Goals](#owner-goals)
2. [User Experience](#user-experience)
    * [Target Crowd](#target-crowd)
    * [User Requirements and Expectation](#user-requirements-expectation)
    * [User Stories](#user-stories)
    * [Site Owner Story](#site-owner)
3. [Technical Design](#technical-design)
    * [Flow Chart](#flow-chart)
4. [Technologies Used](#technology)
    * [Languages](#languages)
    * [Frameworks and Tools](#frameworks)
5. [Features](#features)
    * [Get Monthly Expenses Data](#get-monthly-expenses)
    * [Check Values Entered](#check)
    * [Amend Worksheets](#amend)
    * [Calculate Loss or Savings](#loss-savings)
    * [Calculate and Adjust Budget for the Next Month](#budget)
6. [Validation](#validation)
    * [PEP8 Validation](#pep)
    * [User Stories Testing](#stories)
7. [Bugs](#bugs)
8. [Deployment](#deployment)
9. [Credits](#credits)
10. [Acknowledgement](#acknowledgement)

---
## Goals<a name=goals></a>
Personal Budget Calculation app is a program that helps people properly budget their expenses. People can also track their expenses as it is saved in a google sheet.  Futhermore, it can calculate loss or savings every month by deducting the expenses per month to your alloted budget for that month. Lastly, the app can adjust the budget where it is more needed for the next month depending on the expenditure over the last 5 months.

### User Goals<a name=user-goals></a>
* To be able to monitor expenditures.
* To be able to get some help on how to budget their monthly allowance and help to adjust budget allocation where it is more needed.

### Developer Goals<a name=owner-goals></a>
* To help people allocate, monitor their expenses and adjust their budgets.

---

## User Experience<a name=user-experience></a>

---
### Target Crowd<a name=target-crowd></a>
* Employees having trouble budgeting their income.
* Students that wants to monitor their expenses and allocate their allowance properly.

### User Requirements and Expectations<a name=user-requirements-expectation></a>
* Ability to input data.
* Easy to use
* Easy set up
* Google account for the spreadsheet, cloud platform
### User Stories<a name=user-stories></a>
1. As a user, I want to easily know how to use the app.
2. As a user, I want to know what the app is doing and what the app had done.
3. As a user, I want to see where my data is going to be saved.
### Site Owner Story<a name=site-owner></a>
1. As the site owner, I want the user to get feedbacks or prompts in case user entered an invalid data.

---
## Technical Design<a name=technical-design></a>
* Flow Chart<a name=flow-chart></a>
![Flow Chart](docs/images/readme/app-flowchart.png)

---
## Technologies Used<a name=technology></a>
### Languages<a name=languages></a>
* Python

### Framework and Tools<a name=frameworks></a>
* diagrams.net - To create the flow char
* Github
* Gitpod
* Google Spreadsheet
* Google Cloud Platform
* Heroku - where the app is deployed
---
## Features<a name=features></a>
### Get Monthly Expenses Data<a name=get-monthly-expenses-data></a>
* This feature let the user input their monthly expenses for rent/bills, food and extras.
![Input](docs/images/readme/input-data.png)

### Check Values Entered<a name=check></a>
* This feature will give feedback to users if the data provided is invalid.
![Check](docs/images/readme/feedback1.png)
![Check](docs/images/readme/feedback2.png)

### Amend Worksheets<a name=amend></a>
* This feature will automatically amend the user worksheets and save data when valid values are entered on the app.
![Amend](docs/images/readme/amend-exp.png)

### Calculate Loss or Savings<a name=loss-savings></a>
* This feature will automatically calculate loss or savings. This is attained by deducting users monthly expenses for rent/bills, food and extras to the users budget for that month. Positive result means the user did not use all the allocated budget for that month. On one hand, a negative result means that the user spent more than the allocated budget for that month.
![Calculate](docs/images/readme/loss-savings.png)

### Calculate and Adjust Budget for the Next Month<a name=budget></a>
* This feature will automatically calculate and adjust the users budget for the next month where budget is more needed depending on the users expenditures for the last 5 months.
![Budget](docs/images/readme/new-budget.png)

---
## Validation<a name=validation></a>
### PEP8 Validation
* PEP8 online was use to validate the python code written. Result came back with no warnings or errors.
![Pep8](docs/images/readme/pep8-validation.png)

### User Stories Testing<>