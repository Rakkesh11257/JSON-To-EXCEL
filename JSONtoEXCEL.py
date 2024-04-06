import os
import json
import pandas as pd

def json_to_excel(input_folder, output_file):
    # Initialize an empty list to store all JSON dataframes
    all_data = []

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            # Read JSON data from each file
            with open(os.path.join(input_folder, filename), 'r') as file:
                data = json.load(file)
                # Convert JSON data to DataFrame
                df = pd.json_normalize(data)
                # Append DataFrame to the list
                all_data.append(df)

    # Concatenate all DataFrames in the list
    all_data_concatenated = pd.concat(all_data, ignore_index=True)

    # Write DataFrame to Excel
    all_data_concatenated.to_excel(output_file, index=False)

# Provide the folder path containing JSON files and the output Excel file path
input_folder = r"Input folder"
output_file = r'Output path/filename.xlsx'

# Convert JSON files to Excel
json_to_excel(input_folder, output_file)

print("Conversion completed successfully.")
