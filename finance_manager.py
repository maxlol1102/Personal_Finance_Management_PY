import csv
from google.cloud import storage

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\ADMIN\\Downloads\\MS\\PFM\\pfmanagement-bfb2ec0f1eab.json"

from google.cloud import storage
client = storage.Client()



# Base class for Transaction
class Transaction:
    def __init__(self, amount, description):
        self.amount = amount
        self.description = description

    def display(self):
        raise NotImplementedError("Subclasses should implement this method")

    def __str__(self):
        return f"Amount: {self.amount}, Description: {self.description}"

class Income(Transaction):
    def display(self):
        print(f"{'Income':<15} {self.amount:<15} {self.description:<20}")

class Expenditure(Transaction):
    def display(self):
        print(f"{'Expenditure':<15} {self.amount:<15} {self.description:<20}")

# Base class for Investment
class Investment:
    def __init__(self, amount, duration):
        self.amount = amount
        self.duration = duration

    def display(self):
        raise NotImplementedError("Subclasses should implement this method")

    def maturity_amount(self):
        raise NotImplementedError("Subclasses should implement this method")

    def __str__(self):
        return f"Amount: {self.amount}, Duration: {self.duration}"

class SIP(Investment):
    def __init__(self, amount, duration, monthly_amount):
        super().__init__(amount, duration)
        self.monthly_amount = monthly_amount

    def display(self):
        print(f"{'SIP':<15} {self.amount:<15} {self.duration:<15} {self.monthly_amount:<30}")

    def maturity_amount(self):
        return self.monthly_amount * self.duration + (self.monthly_amount * self.duration * 0.08)

    def __str__(self):
        return f"Amount: {self.amount}, Duration: {self.duration}, Monthly Amount: {self.monthly_amount}"

class FD(Investment):
    def display(self):
        print(f"{'FD':<15} {self.amount:<15} {self.duration:<15} {'N/A':<30}")

    def maturity_amount(self):
        return self.amount + (self.amount * 0.05 * self.duration)

    def __str__(self):
        return f"Amount: {self.amount}, Duration: {self.duration}"

# Finance Manager class
class FinanceManager:
    def __init__(self):
        self.transactions = []
        self.investments = []

    def add_income(self, amount, description):
        self.transactions.append(Income(amount, description))

    def add_expenditure(self, amount, description):
        self.transactions.append(Expenditure(amount, description))

    def add_sip(self, amount, duration, monthly_amount):
        self.investments.append(SIP(amount, duration, monthly_amount))

    def add_fd(self, amount, duration):
        self.investments.append(FD(amount, duration))

    def display_transactions(self):
        print(f"{'Type':<15} {'Amount':<15} {'Description':<20}")
        print('-' * 50)
        for t in self.transactions:
            t.display()

    def display_investments(self):
        print(f"{'Type':<15} {'Amount':<15} {'Duration':<15} {'Monthly':<30}")
        print('-' * 70)
        for i in self.investments:
            i.display()

    def save_to_csv(self):
        # Save transactions to CSV
        with open('transactions.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Type', 'Amount', 'Description'])
            for t in self.transactions:
                writer.writerow([t.__class__.__name__, t.amount, t.description])

        # Save investments to CSV
        with open('investments.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Type', 'Amount', 'Duration', 'Monthly'])
            for i in self.investments:
                if isinstance(i, SIP):
                    writer.writerow(['SIP', i.amount, i.duration, i.monthly_amount])
                elif isinstance(i, FD):
                    writer.writerow(['FD', i.amount, i.duration, 0])

        print("Data saved to CSV files.")

    def upload_to_gcs(self, bucket_name):
        """Uploads CSV files to Google Cloud Storage."""
        client = storage.Client()
        bucket = client.bucket(bucket_name)

        # Upload transactions CSV
        blob = bucket.blob('transactions.csv')
        blob.upload_from_filename('transactions.csv')
        print("Transactions CSV uploaded to Google Cloud Storage.")

        # Upload investments CSV
        blob = bucket.blob('investments.csv')
        blob.upload_from_filename('investments.csv')
        print("Investments CSV uploaded to Google Cloud Storage.")

# Main program
def main():
    manager = FinanceManager()
    while True:
        print("\n1. Add Income\n2. Add Expenditure\n3. Add SIP\n4. Add FD\n5. Display Transactions\n6. Display Investments\n7. Save to CSV\n8. Upload CSV to GCS\n9. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amt = float(input("Enter income amount: "))
            desc = input("Enter income description: ")
            manager.add_income(amt, desc)
        elif choice == '2':
            amt = float(input("Enter expenditure amount: "))
            desc = input("Enter expenditure description: ")
            manager.add_expenditure(amt, desc)
        elif choice == '3':
            amt = float(input("Enter SIP amount: "))
            dur = int(input("Enter duration (in months): "))
            monthly_amt = float(input("Enter monthly amount: "))
            manager.add_sip(amt, dur, monthly_amt)
        elif choice == '4':
            amt = float(input("Enter FD amount: "))
            dur = int(input("Enter duration (in years): "))
            manager.add_fd(amt, dur)
        elif choice == '5':
            manager.display_transactions()
        elif choice == '6':
            manager.display_investments()
        elif choice == '7':
            manager.save_to_csv()
        elif choice == '8':
            bucket_name = input("Enter your Google Cloud Storage bucket name: ")
            manager.upload_to_gcs(bucket_name)
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# python finance_manager.py
# bucket name: my-finance-bucket-1234