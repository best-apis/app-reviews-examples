"""Export App Store and Google Play reviews to one CSV. Usage: python 01_reviews_to_csv.py 570060128 com.duolingo"""
import sys
import pandas as pd
from common import run_actor

apps = sys.argv[1:] or ["570060128", "com.duolingo"]
rows = [r for r in run_actor({"apps": apps, "maxReviewsPerApp": 500, "country": "us", "language": "en"}) if r.get("type") == "review"]
df = pd.DataFrame(rows)
df.to_csv("reviews.csv", index=False)
print(df.groupby(["store", "appId"]).rating.agg(["count", "mean"]).round(2))
