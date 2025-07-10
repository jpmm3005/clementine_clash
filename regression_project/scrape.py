import pandas as pd
import kaggle
import os
import subprocess

path = "/workspaces/cosmos_2025_personal/lecture_three"

os.makedirs('./data', exist_ok=True)

subprocess.run([
    "kaggle", "datasets", "download", "-d", "jaceprater/smokers-health-data", "--force"
])

# Unzip
subprocess.run([
    "unzip", "-o", "smokers-health-data.zip", "-d", path
])

os.remove("smokers-health-data.zip")


if os.path.exists(path):
    print(f"CSV found at: {path}")
else:
    print("CSV not found. Check extraction path or ZIP contents.")

