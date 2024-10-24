def check_alerts(current_temp, threshold=35):
    if current_temp > threshold:
        print("Alert! Current temperature exceeds threshold:", current_temp)
