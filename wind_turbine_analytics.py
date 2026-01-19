# importing the numpy,pandas and pyplot module from matplotlib library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# reading the dataset and creating dataframe 
data = pd.read_csv("C:/Users/DINAKAR/Downloads/Vayumithra_Assessment/Datasheet.csv" )

# preview the top 5 entities from the dataframe to understand the data
data.head()

# conversion of timestamp from raw string to appropriate format and sorting for future calculation and plotting,
data["Timestamp"] = pd.to_datetime(data["Timestamp"])
data = data.sort_values("Timestamp")

# understanding the information about each columns like dtype and non-null count
data.info(verbose=True)

# 1) Early Failure Indicator Analysis 

# to extract the turbine id T01 for analysis
turbine_id = "T01"
turbine_data = data[data["Turbine_ID"] == turbine_id]

# plotting of Gear Oil Temperature vs Time for turbine id T01
plt.figure(figsize=(14,7))
plt.plot(turbine_data["Timestamp"], turbine_data["Gear_Oil_Temp_Avg"])
plt.xlabel("Time")
plt.ylabel("Gear Oil Temperature (°C)")
plt.title("Gear Oil Temperature vs Time (T01)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# plotting of Generator Bearing Temperature vs Time for turbine id T01

plt.figure(figsize=(14, 7))
plt.plot(turbine_data["Timestamp"], turbine_data["Gen_Bear_Temp_Avg"])
plt.xlabel("Time")
plt.ylabel("Generator Bearing Temperature (°C)")
plt.title(f"Generator Bearing Temperature vs Time ({turbine_id})")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2) Anomaly Detection Using Scatter Plots 

# plotting of wind speed vs power output to find deviations 
plt.figure(figsize=(10, 6))
plt.scatter(data["Amb_WindSpeed_Avg"], data["Grd_Prod_Pwr_Avg"])
plt.xlabel("Ambient Wind Speed (m/s)")
plt.ylabel("Generated Power (kW)")
plt.title("Wind Speed vs Power Output")
plt.tight_layout()
plt.show()

# 3) Operational Consistency Check 

# to verify the linear relationship between rotor and generator (RPM)
plt.figure(figsize=(10, 6))
plt.scatter(data["Rtr_RPM_Avg"], data["Gen_RPM_Avg"])
plt.xlabel("Rotor RPM")
plt.ylabel("Generator RPM")
plt.title("Rotor RPM vs Generator RPM")
plt.tight_layout()
plt.show()

# 4) Predictive Trend Analysis

# Extract generated power values (independent variable)
x = data['Grd_Prod_Pwr_Avg']

# Extract gear oil temperature values (dependent variable)
y = data['Gear_Oil_Temp_Avg']

# Fit a first-order (linear) polynomial to the data
# This finds the best-fit straight line relating power and temperature
coeff = np.polyfit(x, y, 1)

# Create a polynomial function using the obtained coefficients
trend = np.poly1d(coeff)
plt.figure(figsize=(12, 8))
plt.scatter(x, y)
plt.plot(x, trend(x))
plt.xlabel("Generated Power (kW)")
plt.ylabel("Gear Oil Temperature (°C)")
plt.title("Gear Oil Temperature vs Power with Trend Line")
plt.show()

# 5) Blade Pitch Health Check

plt.figure(figsize=(8,4))
plt.scatter(data['Amb_WindSpeed_Avg'], data['Blds_PitchAngle_Avg'])
plt.xlabel("Ambient Wind Speed (m/s)")
plt.ylabel("Blade Pitch Angle (deg)")
plt.title("Blade Pitch Angle vs Wind Speed")
plt.show()




