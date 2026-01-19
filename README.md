Wind Turbine SCADA Data Analysis - Early Fault Detection & Operational Anomaly Identification

Project Description : 
This project analyzes Wind Turbine SCADA data to understand turbine operational behavior, detect anomalies, and identify early signs of component degradation. The analysis is based on time-series and scatter-based visual techniques, commonly used in wind turbine condition monitoring.
The focus is on interpreting relationships between wind speed, power output, temperatures, rotational speeds, and blade pitch angle without using complex machine learning models.

Objectives

1) Analyze turbine operational trends using SCADA data
2) Detect abnormal operating points using power curve analysis
3) Identify early failure indicators through temperature trends
4) Verify drivetrain consistency using RPM relationships
5) Assess blade pitch system health
6) Dataset Description

Source Data file : Datasheet.csv
The dataset contains the following SCADA parameters:

- Timestamp
- Turbine ID
- Amb_WindSpeed_Avg (m/s)
- Grd_Prod_Pwr_Avg (kW)
- Rtr_RPM_Avg (rpm)
- Gen_RPM_Avg (rpm)
- Gear_Oil_Temp_Avg (°C)
- Gen_Bear_Temp_Avg (°C)
- Blds_PitchAngle_Avg (deg)
- Amb_Temp_Avg (°C)

Tools & Technologies Used

Python
Pandas – data handling
Matplotlib – visualization
NumPy – trend fitting

📊 Tasks Performed

Task 1: Early Failure Indicator Analysis
Plotted Gear Oil Temperature vs Time
Plotted Generator Bearing Temperature vs Time
Observed gradual temperature rise patterns indicating potential degradation

Task 2: Anomaly Detection Using Power Curve
Plotted Ambient Wind Speed vs Generated Power
Identified operational anomalies deviating from the normal power curve

Task 3: Operational Consistency Check
Plotted Rotor RPM vs Generator RPM
Verified linear relationship and healthy gearbox behavior

Task 4: Simple Predictive Trend Analysis
Plotted Gear Oil Temperature vs Power Output
Fitted a linear trend line to assess thermal behavior at higher loads

Task 5: Blade Pitch Health Check
Plotted Blade Pitch Angle vs Wind Speed
Verified smooth pitch response and control stability

📌 Key Observations

- Most data points follow the expected turbine power curve
- Deviations indicate curtailment, shutdowns, or sensor errors
- Temperature trends help identify early degradation
- RPM linearity confirms drivetrain health
- Smooth pitch variation indicates a healthy pitch control system

📌 Conclusion

This project demonstrates how simple visualization-based analysis of SCADA data can effectively identify operational anomalies and early failure indicators in wind turbines. 
Such methods are widely used in industry for condition monitoring and preventive maintenance.

🚀 How to Run the Project

Clone the repository:
git clone https://github.com/dinakar186/wind_turbine_analytics.git

Install required libraries:
pip install pandas matplotlib numpy

Run the analysis script:
python analysis.py
