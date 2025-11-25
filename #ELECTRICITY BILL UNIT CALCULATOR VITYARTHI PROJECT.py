                                                  #ELECTRICITY BILL UNIT CALCULATOR


#AT THE END TYPE DONE TO FINISH
def calculate_electricity_cost():
    """
    Calculates the total electricity consumption (kWh) and cost for multiple appliances.
    """
    appliances = {}
    
    print("--- Electric Appliance Unit Calculator ---")
    
    # Define a default cost per kWh (modify this for your local rate)
    cost_per_kwh = 6.5  # Example: 8.5 rupees or dollars per kWh

    print(f"Using a default rate of ${cost_per_kwh:.2f} per kWh.")
    
    while True:
        appliance_name = input("\nEnter appliance name (or 'done' to finish): ")
        if appliance_name.lower() == 'done':
            break
        try:
            power_watts = float(input(f"Enter power consumption of {appliance_name} (in Watts): "))
            hours_used = float(input(f"Enter hours used per day for {appliance_name} (in hours): "))
            
            # Store the data
            appliances[appliance_name] = {
                'power': power_watts,
                'hours': hours_used
            }
        except ValueError:
            print("Invalid input. Please enter numerical values for power and hours.")
    
    # Calculate totals
    total_daily_kwh = 0
    for name, data in appliances.items():
        # Energy (Watt-hours) = Power (Watts) * Time (Hours)
        watt_hours = data['power'] * data['hours']
        # Convert Wh to kWh (Kilowatt-hours)
        kwh = watt_hours / 1000
        total_daily_kwh += kwh
        print(f"\n{name} daily usage: {kwh:.2f} kWh")
    # Calculate costs
    daily_cost = total_daily_kwh * cost_per_kwh
    monthly_cost = daily_cost * 30.4 # Average days in a month

    print("\n--- Summary ---")
    print(f"Total daily consumption: {total_daily_kwh:.2f} kWh")
    print(f"Estimated daily cost: ${daily_cost:.2f}")
    print(f"Estimated monthly cost: ${monthly_cost:.2f}")

# Run the calculator
if __name__ == "__main__":
    calculate_electricity_cost()



