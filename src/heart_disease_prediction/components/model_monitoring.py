import pandas as pd
import numpy as np
import os

class ModelMonitoring:
    def __init__(self):
        self.log_file = "data_file/monitoring_log.csv"

    
    def log_predictions(self, input_data, predictions):
        df = pd.DataFrame(input_data)
        df["prediction"] = predictions

        os.makedirs("data_file", exist_ok=True)

        if not os.path.exists(self.log_file):
            df.to_csv(self.log_file, index=False)
        else:
            df.to_csv(self.log_file, mode='a', header=False, index=False)

    
    def check_data_drift(self, new_data, reference_data):
        drift_report = {}

        for col in new_data.columns:
            if new_data[col].dtype != "object":
                new_mean = np.mean(new_data[col])
                ref_mean = np.mean(reference_data[col])

                drift = abs(new_mean - ref_mean)
                drift_report[col] = drift

        return drift_report