 #* POPULATION DATA VISUALIZER FROM CSV FILE

#? Showing Loadiing Text

print("Loading Program, Please Wait...")

#? Importing Libraries 

import os
import pandas as pd
import matplotlib.pyplot as plt
import random


#? Loading File

def load_data(filename):
    folder = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(folder, filename)

    try:
        data = pd.read_csv(path, header=None, usecols=[0, 1, 2],        #! Exception Handling
                           names=["City", "Year", "Population"])
    except Exception as e:
        print(f"Could not read {filename}")
        return pd.DataFrame()

    data["City"] = data["City"].str.strip()
    data["Year"] = pd.to_numeric(data["Year"], errors="coerce")
    data["Population"] = pd.to_numeric(data["Population"], errors="coerce")

    data = data.dropna()
    data = data[(data["City"] != "") & (data["Year"] > 0) & (data["Population"] > 0)]
    data = data.astype({"Year": int, "Population": int})

    return data.drop_duplicates().sort_values(["City", "Year"])


#? Calculating Growth of Cities

def calculate(data):
    first = data.groupby("City")["Population"].first()
    last = data.groupby("City")["Population"].last()
    growth = (last - first) / first * 100
    return last, growth


#? For Summary

def show_summary(data):
    last, growth = calculate(data)

    print(f"Total population: {last.sum()}")
    print(f"Largest city: {last.idxmax()} ({last.max()})")

    if data["Year"].nunique() < 2:
        print("Growth can't be worked out with only one year of data.")
        return

    fastest = growth.idxmax()
    print(f"Fastest growing city: {fastest} ({growth[fastest]:+.2f}%)")


#? For Showing Charts

def show_charts(data):
    if data["Year"].nunique() < 2:
        print("Growth can't be worked out with only one year of data.")
        return

    _, growth = calculate(data)                     #! Getting value for growth

    for city, value in growth.items():
        print(f"{city}: {value:+.2f}%")

    palette = list(plt.cm.tab20.colors)      #& For Random Colors
    colors = random.sample(palette, len(growth)) if len(growth) <= 20 \
        else random.choices(palette, k=len(growth))

    plt.figure()
    plt.bar(growth.index, growth.values, color=colors)
    plt.title("Population Growth by City")
    plt.xlabel("City")
    plt.ylabel("Growth in %")

    plt.figure()
    for city in data["City"].unique():
        rows = data[data["City"] == city]
        plt.plot(rows["Year"], rows["Population"], marker="o", label=city)
    plt.title("Population Trend")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.xticks(sorted(data["Year"].unique()))
    plt.legend()

    plt.show()


#? This is The Main Section Where We Get User Input and Showing Menu

def main():
    name = input("Enter CSV File Name: ").strip()
    data = load_data(name)

    if data.empty:                              #! Checking if data is empty
        print("No valid data found...!")
        return

    while True:
        print("1. Summary")
        print("2. Growth and charts")
        print("3. Exit")
        choice = input("Choose option: ").strip()

        if choice == "1":
            show_summary(data)
        elif choice == "2":
            show_charts(data)
        elif choice == "3":
            print("GoodBye..!  :)")
            break
        else:
            print("Invalid option...! Please enter 1, 2 or 3.")


#! Checking If The Modules Are Imported Form Another File

if __name__ == "__main__":
    main()