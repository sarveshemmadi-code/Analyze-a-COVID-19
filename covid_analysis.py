# =====================================================
# COVID-19 Data Analysis using Pandas and Matplotlib
# =====================================================

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set graph style
sns.set_style("whitegrid")

# -----------------------------------------------------
# Load Dataset
# -----------------------------------------------------
df = pd.read_csv("covid_19_data.csv")

# -----------------------------------------------------
# Display Dataset
# -----------------------------------------------------
print("\n========== FIRST 5 ROWS ==========\n")
print(df.head())

print("\n========== DATASET INFORMATION ==========\n")
print(df.info())

print("\n========== MISSING VALUES ==========\n")
print(df.isnull().sum())

# -----------------------------------------------------
# Data Cleaning
# -----------------------------------------------------
df.fillna(0, inplace=True)

# Convert ObservationDate into Date format
df["ObservationDate"] = pd.to_datetime(df["ObservationDate"])

# -----------------------------------------------------
# Group Data by Date
# -----------------------------------------------------
daily_data = df.groupby("ObservationDate")[["Confirmed", "Deaths", "Recovered"]].sum()

print("\n========== DAILY SUMMARY ==========\n")
print(daily_data.head())

# -----------------------------------------------------
# Basic Statistics
# -----------------------------------------------------
print("\n========== STATISTICS ==========\n")
print(daily_data.describe())

# -----------------------------------------------------
# Chart 1 - Daily Confirmed Cases
# -----------------------------------------------------
plt.figure(figsize=(12,6))

plt.plot(
    daily_data.index,
    daily_data["Confirmed"],
    color="blue",
    linewidth=2,
    label="Confirmed Cases"
)

plt.title("Daily Confirmed COVID-19 Cases", fontsize=16)
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.show()

# -----------------------------------------------------
# Chart 2 - Daily Deaths
# -----------------------------------------------------
plt.figure(figsize=(12,6))

plt.plot(
    daily_data.index,
    daily_data["Deaths"],
    color="red",
    linewidth=2,
    label="Deaths"
)

plt.title("Daily COVID-19 Deaths", fontsize=16)
plt.xlabel("Date")
plt.ylabel("Deaths")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.show()

# -----------------------------------------------------
# Chart 3 - Recovery Trend
# -----------------------------------------------------
plt.figure(figsize=(12,6))

plt.plot(
    daily_data.index,
    daily_data["Recovered"],
    color="green",
    linewidth=2,
    label="Recovered"
)

plt.title("COVID-19 Recovery Trend", fontsize=16)
plt.xlabel("Date")
plt.ylabel("Recovered")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.show()

# -----------------------------------------------------
# Save Charts
# -----------------------------------------------------
plt.figure(figsize=(12,6))
plt.plot(daily_data.index, daily_data["Confirmed"])
plt.title("Daily Confirmed COVID-19 Cases")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("confirmed_cases.png")
plt.close()

plt.figure(figsize=(12,6))
plt.plot(daily_data.index, daily_data["Deaths"])
plt.title("Daily COVID-19 Deaths")
plt.xlabel("Date")
plt.ylabel("Deaths")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("deaths.png")
plt.close()

plt.figure(figsize=(12,6))
plt.plot(daily_data.index, daily_data["Recovered"])
plt.title("COVID-19 Recovery Trend")
plt.xlabel("Date")
plt.ylabel("Recovered")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("recovered.png")
plt.close()

print("\n========================================")
print("COVID-19 Data Analysis Completed")
print("Charts have been saved successfully.")
print("========================================")
