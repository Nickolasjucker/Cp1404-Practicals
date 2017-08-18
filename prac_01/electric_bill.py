cents_per_kwatt = int(input("Enter cents per kWh: "))
daily_usage_kwatt = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
decimal_cents = cents_per_kwatt / 100
estimated_bill = decimal_cents * daily_usage_kwatt * billing_days
print ("Estimated bill: ${}".format(estimated_bill))