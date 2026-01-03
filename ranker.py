import pandas as pd

def rank_getaways(source_city):
    df = pd.read_csv("data/travel_places.csv")

    city_df = df[df["source_city"].str.lower() == source_city.lower()]

    if city_df.empty:
        print("No data found for the given city.")
        return

    city_df["score"] = (
        (1 / city_df["distance_km"]) * 100 +
        city_df["rating"] * 10 +
        city_df["popularity"]
    )

    ranked = city_df.sort_values(by="score", ascending=False)

    print(f"\nTop Weekend Getaways from {source_city}:\n")
    for i, row in enumerate(ranked.itertuples(), start=1):
        print(
            f"{i}. {row.place} | "
            f"Distance: {row.distance_km} km | "
            f"Rating: {row.rating} | "
            f"Popularity: {row.popularity}"
        )

if __name__ == "__main__":
    city = input("Enter source city: ")
    rank_getaways(city)
