import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load


def convert_value(x):
    """Convert number abbreviations to float"""
    if pd.isna(x):
        return None
    x = x.strip().lower()
    if x.endswith('k'):
        return float(x[:-1]) * 1_000
    elif x.endswith('m'):
        return float(x[:-1]) * 1_000_000
    elif x.endswith('b'):
        return float(x[:-1]) * 1_000_000_000
    else:
        return float(x)


def main():
    """Visualize the population of France and a another country."""
    path = "data/population_total.csv"
    db = load(path)
    if db is None:
        print(f"Error: Invalid path. {path}")
        exit(1)
    try:
        # Input
        main_country = "France"
        other_country = input("Please provide a country : ")
        main_country = main_country.lower().capitalize()
        other_country = other_country.lower().capitalize()
        # Cleaning and Converting the values
        db.dropna(inplace=True)
        main_data = db[db['country'].str.lower() ==
                       main_country.lower()].iloc[:, 1:]
        other_data = db[db['country'].str.lower() ==
                        other_country.lower()].iloc[:, 1:]
        years_data = main_data.columns.astype(int)
        main_data = main_data.map(convert_value)
        other_data = other_data.map(convert_value)
        valid_years = years_data <= 2050
        years_data = years_data[valid_years]
        main_values = main_data.values.flatten()[valid_years]
        other_values = other_data.values.flatten()[valid_years]
        # Plotting
        plt.plot(
                years_data,
                other_values,
                label=other_country,
                color='b',
            )
        plt.plot(
                years_data,
                main_values,
                label=main_country,
                color='g',
            )
        plt.legend(loc='lower right')
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        # Adjusting tick locator
        ax = plt.gca()
        ax.locator_params(axis='y', nbins=4)
        ax.yaxis.set_major_formatter(
            ticker.FuncFormatter(lambda x, pos: f'{x/1_000_000:.0f}M'))
        ax.xaxis.set_major_locator(ticker.MultipleLocator(40))
        years_tick = years_data[:40]
        plt.xticks = years_tick
        plt.show()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
