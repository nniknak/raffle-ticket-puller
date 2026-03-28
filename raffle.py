import csv
import re
import random
import sys

## TO-DO: add error handling for file not found, invalid input, etc.
# some row skipping will happen if people put extra lines in venmo note

print("Welcome to the Raffle Winner Picker!")
print("This program will read a CSV file, extract contacts and names from the venmo statements, and randomly pick winners.")
print("Best practice is to delete any non-raffle entries from the CSV file before running this program.")
print("However, the program will attempt to handle some common issues, such negative amounts and invalid data.")
input_file = input("Enter the name of the input CSV file (with .csv extension): ")
output_file = "raffletickets.csv"
winner_count = int(input("Enter the number of winners to pick: "))
ticket_price = int(input("Enter the ticket price (in dollars): "))

print("\n----------- Processing -------------\n")
with open(input_file, newline="", encoding="utf-8") as infile:
    # Skip the first two lines
    next(infile)
    next(infile)
    
    reader = csv.DictReader(infile)
    with open(output_file, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)

        # list to track added lines
        added_lines = []

        row_count = 0
        for row in reader:
            row_count += 1
            contact = row.get("Note", "").strip()
            contact = re.sub(r"\s+", " ", contact)
            name = row.get("From", "").strip()

            amount_raw = row.get("Amount (total)", "").strip()
            if not amount_raw:
                print("Skipping row with missing Amount (total) from ", name, "on row #:", row_count)
                continue

            # Remove currency symbols and thousands separators
            amount_clean = re.sub(r"[^0-9.\-]", "", amount_raw)
            try:
                amount = float(amount_clean)
            except ValueError:
                print("Skipping this row with invalid Amount (total) from ", name, "on row # ", row_count)
                continue

            if ticket_price <= 0:
                print("Invalid ticket price:", ticket_price)
                sys.exit(1)

            count = int(amount // ticket_price)
            if count <= 0:
                print("Skipping this row with negative tickets from this person:", name, "on row #:", row_count)
                continue

            for _ in range(count):
                writer.writerow([contact, name])
                added_lines.append(contact + " | " + name)

    # After writing all rows, you can inspect the list
    print("\n----------- Winner Calculation -------------\n")
    print(f"Added {len(added_lines)} entries:")
    # print(added_lines)

    print("Winners:")

    # pick winners randomly and remove all matches each time
    for i in range(winner_count):
        if not added_lines:
            print("No more entries to choose from.")
            break
        pick = random.choice(added_lines)
        print(f"{i+1}: {pick}")
        # remove all occurrences of the picked contact
        added_lines = [n for n in added_lines if n != pick]

print("Output CSV created successfully.")
