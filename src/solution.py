import argparse
import os

def extract_logs(log_file_path, target_date):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = os.path.join(output_dir, f"output_{target_date}.txt")

    with open(log_file_path, 'r') as log_file, open(output_file_path, 'w') as output_file:
        for line in log_file:
            if line.startswith(target_date):
                output_file.write(line)

    print(f"Logs for {target_date} have been extracted to {output_file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract logs for a specific date.")
    parser.add_argument("date", type=str, help="Date in YYYY-MM-DD format")
    args = parser.parse_args()

    # Validate date format 
    if len(args.date) != 10 or args.date[4] != '-' or args.date[7] != '-':
        print("Error: Date must be in YYYY-MM-DD format.")
    else:
        log_file_path = "/logs_2024.log" 
        extract_logs(log_file_path, args.date)
