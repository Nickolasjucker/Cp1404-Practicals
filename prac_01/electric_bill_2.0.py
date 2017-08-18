TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff_per_kwatt = int(input("Which tariff? 11 or 31: "))
daily_usage_kwatt = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
if tariff_per_kwatt == 11:
    estimated_bill = TARIFF_11 * daily_usage_kwatt * billing_days
    print ("Estimated bill: ${:.2f}".format(estimated_bill))
elif tariff_per_kwatt == 31:
    estimated_bill = TARIFF_31 * daily_usage_kwatt * billing_days
    print ("Estimated bill: ${:.2f}".format(estimated_bill))
else:
    print("Not valid")