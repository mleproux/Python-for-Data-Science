import matplotlib.pyplot as plt
from load_csv import load


def main():
    """Visualize the life expectancy years of France"""
    path = "data/life_expectancy_years.csv"
    db = load(path)
    if db is None:
        print(f"Error: Invalid path. {path}")
        exit(1)
    try:
        db.dropna(inplace=True)
        france_data = db[db['country'] == "France"].iloc[:, 1:]
        years_data = france_data.columns.astype(int)
        plt.plot(years_data, france_data.values.flatten(), label="France")
        years_tick = years_data[::40]
        plt.xticks(years_tick)
        plt.title("France Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.show()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
