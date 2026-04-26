import sqlite3
import random
import matplotlib.pyplot as plt

# Create database and insert initial data
def create_database():
    conn = sqlite3.connect("population_AW.db")
    cursor = conn.cursor()

    # Create table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS population (
        city TEXT,
        year INTEGER,
        population INTEGER
    )
    """)

    # Florida cities with estimated 2025 population
    cities = {
        "Sarasota": 58405,
        "Bradenton": 58776,
        "Apollo Beach": 30546,
        "Miami": 498060,
        "Tampa": 421042,
        "Ocala": 71842,
        "Lakeland": 127767,
        "North Port": 97219,
        "Melbourne": 888181,
        "Jupiter": 63438,
    }

    for city, pop in cities.items():
        cursor.execute("INSERT INTO population VALUES (?,?,?)", (city, 2025, pop))

    conn.commit()
    conn.close()

    print("Database created successfully")

# Simulate population growth/decline
def simulate_growth():
    conn = sqlite3.connect("population_AW.db")
    cursor = conn.cursor()

    cursor.execute("SELECT city, population FROM population WHERE year = 2025")
    rows = cursor.fetchall()

    for city, base_population in rows:
        current_population = base_population

        for year in range(2026, 2046): # next 20 years
            # Random growth/decline rate between -2% and +5%
            rate = random.uniform(-0.02, 0.05)
            current_population = int(current_population * (1 + rate))

            cursor.execute(
                "INSERT INTO population VALUES (?,?,?)",
                (city, year, current_population)
            )

    conn.commit()
    conn.close()
    print("Population growth simulated successfully")

 # Plot population for a chosen city
def plot_population():
    conn = sqlite3.connect("population_AW.db")
    cursor = conn.cursor()

    # Get list of cities
    cursor.execute("SELECT DISTINCT city FROM population")
    cities = [row[0] for row in cursor.fetchall()]

    # Show options
    print("\nAvailable cities:")
    for i, city in enumerate(cities, 1):
        print(f"{i}. {city}")

    # User choice
    choice = int(input("Select a city by number: "))
    selected_city = cities[choice - 1]

    # Get data for selected city
    cursor.execute(
        "SELECT * FROM population WHERE city = ? ORDER BY year",
        (selected_city,)
    )

    data = cursor.fetchall()

    years = [row[0] for row in data]
    populations = [row[1] for row in data]

    conn.close()

    # Plot
    plt.figure()
    plt.plot(years, populations)
    plt.title("Population Growth for {selected_city}")
    plt.xlabel("Years")
    plt.ylabel("Population")
    plt.grid()

    plt.show()

    conn.close()

# Main program
def main():
    create_database()
    simulate_growth()
    plot_population()

if __name__ == "__main__":
    main()



