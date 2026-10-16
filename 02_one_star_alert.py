"""Alert on new 1-2 star reviews since the last run (onlyNewReviews remembers state). Env: APIFY_TOKEN, APPS, optional SLACK_WEBHOOK_URL"""
import os
import requests
from common import run_actor

apps = os.environ.get("APPS", "com.duolingo").split(",")
bad = [r for r in run_actor({"apps": apps, "maxReviewsPerApp": 200, "onlyNewReviews": True}) if r.get("type") == "review" and (r.get("rating") or 5) <= 2]
text = f"{len(bad)} new low-rated reviews\n" + "\n".join(f"{r['rating']}★ {r.get('title') or ''} {(r.get('text') or '')[:140]}" for r in bad[:15])
print(text)
if os.environ.get("SLACK_WEBHOOK_URL") and bad:
    requests.post(os.environ["SLACK_WEBHOOK_URL"], json={"text": text}, timeout=20).raise_for_status()
