import requests
import json
import matplotlib.pyplot as plt

GITHUB_USERNAME = "RamishFatimaa"  # Replace with your username
TOKEN = "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"

headers = {"Authorization": f"token {TOKEN}"}
repos_url = f"https://api.github.com/users/{RamishFatimaa}/repos"

# Fetch repositories
response = requests.get(repos_url, headers=headers)
repos = response.json()

topic_counts = {}

for repo in repos:
    if "topics" in repo and repo["topics"]:
        for topic in repo["topics"]:
            topic_counts[topic] = topic_counts.get(topic, 0) + 1

# Save stats as JSON
with open("topic_stats.json", "w") as f:
    json.dump(topic_counts, f, indent=4)

# Generate a bar chart
plt.figure(figsize=(10, 5))
plt.bar(topic_counts.keys(), topic_counts.values(), color="blue")
plt.xlabel("Topics")
plt.ylabel("Number of Repositories")
plt.title("GitHub Repository Topics Stats")
plt.xticks(rotation=45)
plt.savefig("topic_stats.png")
