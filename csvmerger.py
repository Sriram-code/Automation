import os
import pandas as pd

# Path setup
folder_path = r'C:\Users\Sriram\Desktop\csvshortcut'
output_file = 'merged_output.csv'

# Get CSV files
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Empty DataFrame
merged_df = pd.DataFrame()

# Merge all CSVs
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)

    # Drop unwanted columns
    df = df.drop(columns=['Username', 'Prompt', 'Response'], errors='ignore')

    # Clean column names
    df.columns = df.columns.str.strip()

    # Convert "Timestamp (UTC)" if it exists
    if 'Timestamp (UTC)' in df.columns:
        df['Timestamp (UTC)'] = pd.to_datetime(df['Timestamp (UTC)'], unit='s', errors='coerce')

    merged_df = pd.concat([merged_df, df], ignore_index=True)

# Sort by most recent date first
if 'Timestamp (UTC)' in merged_df.columns:
    merged_df = merged_df.sort_values(by='Timestamp (UTC)', ascending=False)
    # Format to MM/DD/YYYY after sorting
    merged_df['Timestamp (UTC)'] = merged_df['Timestamp (UTC)'].dt.strftime('%m/%d/%Y')

# Save final output
merged_df.to_csv(os.path.join(folder_path, output_file), index=False)

print("Merged, sorted, and saved with date format MM/DD/YYYY.")
