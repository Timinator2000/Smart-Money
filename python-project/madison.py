################################################################################
#
# Madison's Roth IRA projection
#
#    • 2013 - 2025: year-end contributions based on Madison's earnings
#    • Two growth scenarios: 7 % (conservative) and 13 % (tech-heavy 20-yr avg)
#
################################################################################


################################################################################
#
# Assumed Rates of Return:
#
# You may make changes to the follow two rates of return. Any other changes might break the
# code if you are not familiar with Python. If you do break the code, click the button to
# the right of the code window that displays "reset code" when you hover over it.
# 
################################################################################

STANDARD_RETURN   = 7
TECH_HEAVY_RETURN = 13        # 13 % is an approximate 20‑yr annualized return of a tech‑heavy index (e.g., QQQ)

################################################################################
#
# Assumed Contribution Schedule:
#
# You may make changes to the following schedule. Try not to break the code, but
# if you do, click the button to the right of the code window that displays 
# "reset code" when you hover over it.
# 
################################################################################

# Year‑end contributions (dollars)
CONTRIBUTIONS = {
    2013: 1000,   # age 10
    2014: 1000,
    2015: 1000,
    2016: 1000,
    2017: 1000,
    2018: 3000,   # age 15 (adds babysitting)
    2019: 3000,
    2020: 6000-6000,   # age 17 (fast‑food job; Roth limit)
    2021: 6000-6000,
    2022: 6000-6000,
    2023: 6500-6500,   # age 20 (new Roth limit)
    2024: 7000-7000,
    2025: 7000-7000,   # age 22 (college graduation)
}



################################################################################
#
# The following code is used for all calculations and is provided so that you
# can verify anything you wish to verify.
#
# Any changes below here come with opportunity to break the code. If 
# you do break the code, click the button to the right of the code window that 
# displays "reset code" when you hover over it.
# 
################################################################################

START_AGE = 10           # Madison’s age in 2013
YEARS_TO_60 = 38         # From age 22 (end 2025) to age 60

GROWTH_RATES = {f'{rate} %' : rate / 100 for rate in [STANDARD_RETURN, TECH_HEAVY_RETURN]}


# Format number as a currency string.
def money(x):
    return f'${x:,.2f}'


# Return a list of (year, balance_after_contribution) for a given annual rate.
def year_by_year(contributions, rate_of_return):
    balance = 0.0
    schedule = []
    for year, contribution in sorted(contributions.items()):
        balance *= (1 + rate_of_return)      # growth on prior balance
        balance += contribution              # year‑end contribution
        schedule.append((year, balance))

    return schedule


# Return a simple calculation of compound growth for a certain number of years.
def future_value(present_value, rate, num_years):
    return present_value * (1 + rate) ** num_years


################################################################################
#
# All code below this point does nothing other than print results. The code is
# provided to fascilitate any verification you wish to do.
#
################################################################################


def print_projection_table(contributions, rates_of_return):

    # Calculate schedules for each rate
    schedules = {label: year_by_year(contributions, rate) for label, rate in rates_of_return.items()}

    # Table header
    header = ['Year', 'Age', 'Contribution'] + [f'Balance @ {label}' for label in rates_of_return]
    col_w = [6, 5, 14] + [18] * len(rates_of_return)
    line_fmt = ' '.join(f'{{:<{w}}}' if i < 2 else f'{{:>{w}}}' for i, w in enumerate(col_w))
    print(line_fmt.format(*header))

    # Rows
    for i, year in enumerate(sorted(contributions)):
        row = [str(year), str(START_AGE + i), money(contributions[year])]
        for label in rates_of_return:
            balance = schedules[label][i][1]
            row.append(money(balance))

        print(line_fmt.format(*row))

    # Return ending balances (year 2025)
    after_college_balances = {label: schedules[label][-1][1] for label in rates_of_return}

    return after_college_balances


def generate_madisons_projections():

    print('\nMadison\'s Roth IRA Projection (contributions made at year-end)\n')
    balances_after_graduation_year = print_projection_table(CONTRIBUTIONS, GROWTH_RATES)
    
    print(f'\n----------------- Madison graduates from college. -----------------')
    print(f'\nTotal contributions made to her Roth IRA = {money(sum(CONTRIBUTIONS.values()))}')
    print(f'\nValue at age 60 (no further contributions, {YEARS_TO_60} additional years of growth):')
    
    for label, rate in GROWTH_RATES.items():
        fv = future_value(balances_after_graduation_year[label], rate, YEARS_TO_60)
        print(f'  {label:>8} growth → {money(fv)}')
    
    print('\n')
