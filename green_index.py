


current_emissions = input("Enter the city's current carbon emmissions:")
current_emissions = int(current_emissions)

emission_decrease_rate = input("Enter the city's historic rate of carbon emmissions decrease:")
emission_decrease_rate = int(emission_decrease_rate)

year_rate = current_emissions/emission_decrease_rate
year = 2022+year_rate
#test


if (year >= 2037 and year <= 2044):
    new_year = abs(year-2037)
    increment_val = 0.238
    end_val = 10.00
    derrived_val = end_val-(increment_val*new_year)
    derrived_val1 = derrived_val/10
    percentage = "{:.5%}".format(derrived_val1)
    print(percentage)
elif (year >= 2045 and year <= 2050):
    new_year = abs(year-2045)
    increment_val = 0.333
    end_val = 8.333
    derrived_val = end_val-(increment_val*new_year)
    derrived_val1 = derrived_val/10
    percentage = "{:.5%}".format(derrived_val1)
    print(percentage)
elif (year >= 2051 and year <= 2052):
    new_year = abs(year-2051)
    increment_val = 1.666
    end_val = 6.666
    derrived_val = end_val-(increment_val*new_year)
    derrived_val1 = derrived_val/10
    percentage = "{:.5%}".format(derrived_val1)
    print(percentage)
elif (year >= 2053 and year <= 2070):
    new_year = abs(year-2053)
    increment_val = 0.098
    end_val = 5.000
    derrived_val = end_val-(increment_val*new_year)
    derrived_val1 = derrived_val/10
    percentage = "{:.5%}".format(derrived_val1)
    print(percentage)
elif (year >= 2071 and year <= 2085):
    new_year = abs(year-2071)
    increment_val = 0.119
    end_val = 3.333
    derrived_val = end_val-(increment_val*new_year)
    derrived_val1 = derrived_val/10
    percentage = "{:.5%}".format(derrived_val1)
    print(percentage)
elif (year > 2085):
    percentage = "{:.5%}".format(0)
    print(percentage)
elif (year < 2037):
    percentage = "{:.5%}".format(1)
    print(percentage)

