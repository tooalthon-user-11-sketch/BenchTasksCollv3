# Expense Tracker Task

## Overview
Develop an expense tracking system that allows users to record, categorize, and analyze their spending habits.

## Requirements

### Core Features
1. **Expense Recording**: Users should be able to add new expenses with the following details:
   - Amount (numeric)
   - Category (predefined list: Food, Transport, Shopping, Entertainment, Bills, Other)
   - Date (YYYY-MM-DD format)
   - Description (optional)

2. **Expense Management**:
   - View all expenses
   - Filter expenses by category, date range, or amount
   - Edit or delete existing expenses

3. **Reporting**:
   - Daily, weekly, and monthly spending summaries
   - Category-wise breakdown
   - Trend analysis (e.g., spending increase/decrease over time)

4. **Budgeting**:
   - Set monthly budgets for each category
   - Track progress against budgets
   - Receive alerts when approaching or exceeding budget limits

5. **Data Persistence**:
   - Store expenses in a structured format (e.g., JSON, CSV, or database)
   - Load and save data seamlessly

## Evaluation Criteria
- All core features are implemented and functional
- Data is stored and retrieved correctly
- Reports are accurate and informative
- Budget alerts work as expected
- Code is well-structured and follows best practices

## Example Workflow
1. User adds an expense: "$25 for lunch at a restaurant"
2. System categorizes it as "Food" and records it
3. User requests a monthly report
4. System generates a summary showing total spending, category breakdown, and budget status
