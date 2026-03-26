from load_csv import load

print("TEST 01 | Valid Path", load("data/life_expectancy_years.csv"), sep='\n')

print("TEST 02 | Empty string", load(""), sep='\n')

print("TEST 03 | None value", load(None), sep='\n')

print("TEST 04 | Bad path", load("bad_path.csv"), sep='\n')

print("TEST 05 | Wrong format", load("data/data.json"), sep='\n')
