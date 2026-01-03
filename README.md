# Weekend Getaway Ranker

Weekend Getaway Ranker is a Python-based data engineering project that ranks nearby travel destinations for weekend trips based on distance, user ratings, and popularity. The project demonstrates data filtering, scoring logic, and ranking using Pandas.

---

## Tech Stack

- Python
- Pandas

---

## Features

- City-based destination filtering
- Ranking using weighted scoring logic
- Clean and readable console output
- Lightweight and fast execution
- Easy to extend with more cities or parameters

---

## Project Structure

<pre>
  weekend-getaway-ranker/
├── data/
│ └── travel_places.csv
├── ranker.py
├── requirements.txt
├── sample_outputs/
│ ├── kolkata.txt
│ ├── delhi.txt
│ └── bangalore.txt
└── README.md
</pre>


---

## Dataset Description

The dataset contains the following fields:
- `place` – Name of the destination
- `source_city` – Starting city
- `distance_km` – Distance from source city
- `rating` – User rating (out of 5)
- `popularity` – Popularity score (out of 100)

---

## Ranking Logic

Each destination is assigned a score based on:
- Shorter distance (preferred)
- Higher user rating
- Higher popularity

A weighted formula combines these factors to generate the final ranking.

---

## How to Run

1. Install dependencies
```bash
pip install -r requirements.txt
```

2. Run the script
```bash
python ranker.py
```

3. Enter a source city when prompted
Example:
- Kolkata
- Delhi
- Bangalore

## Sample Outputs
Sample ranked outputs for the following cities are included:
- Kolkata
- Delhi
- Bangalore
These can be found in the sample_outputs/ folder.
