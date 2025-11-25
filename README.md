# ELECTRICITY-BILL-CALCULATOR
Electricity Bill Unit Calculator
This Python script provides an interactive command-line interface (CLI) tool to estimate the daily and monthly electricity consumption (in kWh) and associated costs for multiple household appliances.
Features
	Interactive Input: Easily add multiple appliances by name, power consumption (in Watts), and daily usage (in hours).
	Cost Estimation: Calculates daily and monthly electricity costs based on a specified rate per kilowatt-hour (kWh).
	Error Handling: Basic validation ensures that only numerical values are accepted for power and usage inputs.
How It Works
The script uses the following formula to calculate energy consumption:
 
"Energy (kWh)"=("Power (Watts)" ×"Time (Hours)" )/1000
Energy (kWh)=Power (Watts)×Time (Hours)1000
It then multiplies the total kWh used by a predefined cost per kWh to estimate expenses.
Getting Started
Prerequisites
You only need Python installed on your system to run this script. The code is written in standard Python and requires no external libraries.
Usage
	Save the Code: Save the provided Python code into a file named electricity_calculator.py.
	Run from Terminal: Open your terminal or command prompt, navigate to the directory where you saved the file, and run the following command:
bash
python electricity_calculator.py
Use code with caution.
	Follow the Prompts:
	Enter the name of an appliance (e.g., "Refrigerator").
	Enter its power consumption in Watts (check the appliance label or manufacturer specifications).
	Enter the daily usage in hours.
	Type done when finished adding all appliances.
Example Session
--- Electric Appliance Unit Calculator ---
Using a default rate of $6.50 per kWh.

Enter appliance name (or 'done' to finish): TV
Enter power consumption of TV (in Watts): 100
Enter hours used per day for TV (in hours): 5

Enter appliance name (or 'done' to finish): Lamp
Enter power consumption of Lamp (in Watts): 60
Enter hours used per day for Lamp (in hours): 4

Enter appliance name (or 'done' to finish): done

TV daily usage: 0.50 kWh

Lamp daily usage: 0.24 kWh

--- Summary ---
Total daily consumption: 0.74 kWh
Estimated daily cost: $4.81
Estimated monthly cost: $146.30
Configuration
Adjusting the Electricity Rate
By default, the script uses a hardcoded rate of 6.5 per kWh. You can easily modify this variable within the calculate_electricity_cost function to match your local utility rate (e.g., rupees, dollars, etc.):
python
# Define a default cost per kWh (modify this for your local rate)
cost_per_kwh = 6.5  # Example: 8.5 rupees or dollars per kWh
Use code with caution.
To find your current electricity rate, check your physical bill statement or visit your utility provider's website. You can often find this information via a utility provider's official online portal or by using an online tool to find your local electricity rates.
Monthly Calculation
The monthly cost is estimated by multiplying the daily cost by an average of 30.4 days per month
