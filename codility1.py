from collections import defaultdict


'''
   Pseudo code 

   Initialize variables:

balance to keep track of the account balance, starting at 0.
card_payments to count the number of card payments made in each month, starting at 0 for all months.
card_costs to keep track of the total cost of card payments made in each month, starting at 0 for all months.
fee to keep track of the total fee deducted each month, starting at 0.
last_month to keep track of the last month encountered, starting at 0.
Iterate over the transactions:

For each transaction, extract the amount and date.

Update the balance by adding the amount to it.

Check if the transaction is within the same month or a new month:

Extract the month from the date.
If it's a new month, check if the last month had at least three card payments totaling at least 100:
If not, deduct the monthly fee of 5 from the balance and increment the fee variable.
Reset card_payments and card_costs to 0 for the new month.
Update the last_month variable to the current month.
If the transaction amount is negative, it represents a card payment:

Increment the card_payments count for the current month.
Subtract the absolute value of the amount from the card_costs for the current month.
After the loop ends, check if the last month had at least three card payments totaling at least 100:

If not, deduct the monthly fee of 5 from the balance and increment the fee variable.
Calculate the final balance by subtracting the total fee (fee * 12) from the balance.

Return the final balance as the result.

'''
def solution(A, D):
    balance = 0
    card_payments = defaultdict(int)  # Keeps track of the number of card payments made in each month
    card_costs = defaultdict(int)  # Keeps track of the total cost of card payments made in each month
    fee = 0  # Total fee deducted each month
    last_month = 0  # Keeps track of the last month encountered

    for amount, date in zip(A, D):
        year, month, _ = date.split('-')
        month = int(month)

        balance += amount

        # Check if it's a new month
        if month != last_month:
            # Check if the last month had at least three card payments totaling at least 100
            if card_payments[last_month] < 3 or card_costs[last_month] < 100:
                fee += 5
                balance -= 5
            # Reset card payments and costs for the new month
            card_payments[month] = 0
            card_costs[month] = 0
            last_month = month

        if amount < 0:
            card_payments[month] += 1
            card_costs[month] -= amount

    # Check if the last month had at least three card payments totaling at least 100
    if card_payments[last_month] < 3 or card_costs[last_month] < 100:
        fee += 5
        balance -= 5

    return balance - (fee * 12)