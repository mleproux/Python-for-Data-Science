import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load


def main():
    """Visualize the gross domestic product and life expectancy
    of every country in 1900"""
    life_path = "data/life_expectancy_years.csv"
    gross_path = "data/income_per_person_gdppercapita_ppp_\
inflation_adjusted.csv"
    life_data = load(life_path)
    gross_data = load(gross_path)
    if life_data is None:
        print(f"Error: Invalid path for life expectancy data. {life_path}")
        exit(1)
    if gross_data is None:
        print(f"Error: Invalid path for gross product data. {gross_path}")
        exit(1)
    try:
        # Cleaning Values
        life_data.dropna(inplace=True)
        gross_data.dropna(inplace=True)
        print(life_data.columns)
        print(gross_data.columns)
        merged = life_data[["country", "1900"]].merge(
            gross_data[["country", "1900"]],
            on="country",
            suffixes=("_life", "_gdp")
        ).dropna()
        # Plotting
        plt.plot(merged["1900_gdp"], merged["1900_life"], 'o')
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.xscale("log")
        ax = plt.gca()
        ax.xaxis.set_major_formatter(
            ticker.FuncFormatter(
                lambda x, pos: f"{int(x/1000)}k" if x >= 1000 else f"{int(x)}"
                )
        )
        plt.show()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
