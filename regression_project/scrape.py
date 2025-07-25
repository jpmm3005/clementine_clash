import os
import subprocess
import key

os.environ['KAGGLE_USERNAME'] = key.username
os.environ['KAGGLE_KEY'] = key.key

path = "/Users/jpxmaestas/clementine_clash/clementine_clash/clementine_clash-1/regression_project"
os.makedirs('./data', exist_ok=True)
download_dir = "./data"
zip_path = os.path.join(download_dir, "smokers-health-data.zip")


subprocess.run([
    "kaggle", "datasets", "download", "-d", "jaceprater/smokers-health-data", "--force"
], check= True)

# Unzip
subprocess.run([
    "unzip", "-o", "smokers-health-data.zip", "-d", path
])

os.remove("smokers-health-data.zip")


if os.path.exists(path):
    print(f"CSV found at: {path}")
else:
    print("CSV not found. Check extraction path or ZIP contents.")

