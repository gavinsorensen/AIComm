# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load GoHighLevel and Hubspot CRM data
gohighlevel_data = pd.read_csv("gohighlevel_data.csv")
hubspot_data = pd.read_csv("hubspot_data.csv")

# Concatenate dataframes and remove duplicates
crm_data = pd.concat([gohighlevel_data, hubspot_data])
crm_data = crm_data.drop_duplicates()

# Clean and preprocess data
crm_data["date"] = pd.to_datetime(crm_data["date"])
crm_data["day_of_week"] = crm_data["date"].dt.day_name()

# Visualize data using bar chart
sns.countplot(x="day_of_week", data=crm_data)
plt.title("Number of Communications by Day of Week")
plt.xlabel("Day of Week")
plt.ylabel("Count")
plt.show()

# Identify patterns and trends in data
max_communications_day = crm_data["day_of_week"].value_counts().idxmax()
print("The day with the most communications is:", max_communications_day)

mean_communications_month = crm_data.groupby(pd.Grouper(key="date", freq="M")).size().mean()
print("The average number of communications per month is:", mean_communications_month)
