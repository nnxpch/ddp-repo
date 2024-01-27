"""
Compound Interest Calculator Function

Objective:
Write a function named 'compound_interest_calculator' to calculate compound interest.

Function Parameters:
1. P (float): Principal amount.
2. r (float): Annual interest rate in decimal.
3. n (integer): Number of times interest is compounded per year.
4. t (integer): Number of years for investment.

Instructions:
- Use the formula: A = P(1 + r/n)^(nt) to calculate compound interest.
- Return the accumulated amount A after t years.
- Handle edge cases for inputs.

Example Test Cases:
1. compound_interest_calculator(1000, 0.05, 12, 5) should calculate the amount.
2. compound_interest_calculator(500, 0.07, 4, 10) should calculate the amount.
3. compound_interest_calculator(1500, 0.03, 6, 7) should calculate the amount.
"""


def compound_interest_calculator(P, r, n, t):
    # Your code goes here
    # Implement the compound interest calculation
    # Calculate compound interest using the formula A = P(1 + r/n)^(nt)
    if P >= 1 and t >= 1:
        A = P * (1 + r/n)**(n*t)
        return round(A, 2)
        
        # Check for edge cases: negative principal amount or negative time
    elif P < 0 or t < 0:
        return "Invalid input. Principal amount and time must be non-negative."

        # Check for edge case: zero interest rate
    elif r == 0:
        return P

       

# Test cases
print(compound_interest_calculator(1000, 0.05, 12, 5))  # Expected: Amount after 5 years
print(compound_interest_calculator(500, 0.07, 4, 10))  # Expected: Amount after 10 years
print(compound_interest_calculator(1500, 0.03, 6, 7))  # Expected: Amount after 7 years