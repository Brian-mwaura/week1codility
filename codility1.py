from datetime import datetime

def solution(A, D):
    balance = 0
    fee = 0
    total_income = 0
    prev_month = 0
    
    for i in range(len(A)):
        date = datetime.strptime(D[i], "%Y-%m-%d")
        current_month = date.month
        
        if A[i] < 0:
            balance += A[]
            fee += 1
        else:
            balance += A[i]
            total_income += A[i]
        
        if current_month != prev_month:
            if fee < 100 or abs(fee) < 3:
                balance -= 5
            fee = 0
            prev_month = current_month
    
    if fee < 100 or abs(fee) < 3:
        balance -= 5
    
    return balance - (5 * 12) + total_income