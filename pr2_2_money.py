def expression2(scholarship, expenses):
    total_needed = 0
    expenses_current = expenses
    months = 10

    for i in range(months):
        total_needed += expenses_current - scholarship
        expenses_current *= 1.05

    return total_needed