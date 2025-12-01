import sqlite3
import random
import os

DATABASE_NAME = 'population_SR.db'
CITIES_FLORIDA = [
    "Jacksonville", "Miami", "Tampa", "Orlando", "North Port",
    "Port Charlotte", "Sarasota", "Fort Myers", "Tallahassee", "Naples"
]
START_YEAR = 2023
END_YEAR = START_YEAR + 20


def create_database_and_table(db_name):

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS population (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            year INTEGER NOT NULL,
            population INTEGER NOT NULL
        );
    ''')
    conn.commit()
    conn.close()
    print(f"Database '{db_name}' and table 'population' ensured to exist.")


def simulate_population_change(initial_population):

    population_data = []
    current_population = initial_population

    for year in range(START_YEAR, END_YEAR + 1):
        population_data.append((year, int(current_population)))

        growth_rate = random.uniform(-0.01, 0.03)
        current_population *= (1 + growth_rate)
        if current_population < 0:
            current_population = 0

    return population_data


def populate_initial_data(db_name):

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    initial_populations = {
        "Jacksonville": 1645707, "Miami": 455924, "Tampa": 393389,
        "Orlando": 311732, "North Port": 88934, "Port Charlotte": 64971,
        "Sarasota": 469013, "Fort Myers": 91730, "Tallahassee": 395143,
        "Naples": 19421
    }

    for city, pop_2023 in initial_populations.items():
        # Get all 21 years of data for this city
        city_data = simulate_population_change(pop_2023)

        # Insert all simulated data into the database
        cursor.executemany(
            'INSERT INTO population (city, year, population) VALUES (?, ?, ?)',
            [(city, year, pop) for year, pop in city_data]
        )

    conn.commit()
    conn.close()
    print("Population data for all 10 cities over 21 years inserted successfully.")


def display_city_growth(db_name, selected_city):

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT year, population 
        FROM population 
        WHERE city = ? 
        ORDER BY year ASC
    ''', (selected_city,))

    results = cursor.fetchall()
    conn.close()

    if not results:
        print(f"No data found for {selected_city}.")
        return

    print(f"\n--- Population Growth/Decline for {selected_city} (2023-2043) ---")
    print(f"{'Year':<10} | {'Population':<15}")
    print("-" * 30)
    for year, pop in results:
        print(f"{year:<10} | {pop:<15,}")
    print("-" * 30)


if __name__ == "__main__":
    if os.path.exists(DATABASE_NAME):
        os.remove(DATABASE_NAME)

    create_database_and_table(DATABASE_NAME)

    populate_initial_data(DATABASE_NAME)

    print("\nAvailable cities to view:")
    for i, city in enumerate(CITIES_FLORIDA):
        print(f"{i + 1}. {city}")

    while True:
        try:
            choice = input(f"\nEnter the number (1-10) or name of the city to view its growth (or 'quit' to exit): ")
            if choice.lower() == 'quit':
                break

            try:
                city_index = int(choice) - 1
                if 0 <= city_index < len(CITIES_FLORIDA):
                    selected_city_name = CITIES_FLORIDA[city_index]
                else:
                    print("Invalid number. Please enter a number between 1 and 10.")
                    continue
            except ValueError:
                selected_city_name = choice.strip().title()
                if selected_city_name not in CITIES_FLORIDA:
                    print(f"'{selected_city_name}' not in the list of available cities.")
                    continue

            display_city_growth(DATABASE_NAME, selected_city_name)

        except Exception as e:
            print(f"An error occurred: {e}")

