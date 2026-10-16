# App Store & Google Play reviews: Python examples

Examples for the [**App Store & Google Play Reviews Scraper**](https://apify.com/best_apis/app-store-play-reviews) Apify Actor.

[![App reviews on Apify](https://apify.com/actor-badge?actor=best_apis/app-store-play-reviews)](https://apify.com/best_apis/app-store-play-reviews)

| Script | What it does |
|---|---|
| `01_reviews_to_csv.py` | Reviews from both stores to one CSV |
| `02_one_star_alert.py` | Alert on new low-rated reviews (state is kept by the Actor between runs) |

```bash
pip install -r requirements.txt
export APIFY_TOKEN=...
python 01_reviews_to_csv.py 570060128 com.duolingo
```
MIT licensed examples.
