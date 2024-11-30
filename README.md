# Personal Finance Management

This project is a **Personal Finance Management** tool designed to help users track their financial activities. It supports adding income, expenditures, and investments, saving data to CSV files, and integrating with **Google Cloud Storage** for secure data storage.

---

## Features

- **Data Entry:**
  - Add Income
  - Add Expenditures
  - Add Systematic Investment Plans (SIPs)
  - Add Fixed Deposits (FDs)

- **Data Management:**
  - Save transactions and investment details to a CSV file.
  - View all stored financial data.

- **Cloud Integration:**
  - Upload CSV files to Google Cloud Storage using a service account for secure backup.

- **Error Handling:**
  - Handles invalid user inputs and exceptions (e.g., missing permissions, invalid bucket names).

---

## Prerequisites

1. **Python Installation:**
   - Python 3.7 or higher.

2. **Required Libraries:**
   - Install the dependencies using pip:
     ```bash
     pip install pandas google-cloud-storage
     ```

3. **Google Cloud Setup:**
   - **Enable Google Cloud Storage API** in your Google Cloud project.
   - **Download Service Account Credentials:**
     1. Go to `IAM & Admin > Service Accounts` in the Google Cloud Console.
     2. Create a service account with the `Storage Admin` role.
     3. Download the JSON key file and save it as `credentials.json` in the project directory.
   - Set the environment variable:
     ```bash
     export GOOGLE_APPLICATION_CREDENTIALS="credentials.json"
     ```

---

## Usage

1. **Run the Program:**
   ```bash
   python finance_manager.py
   ```

2. **Options:**
   - Add financial data (income, expenditures, investments).
   - View or save data.
   - Upload CSV files to Google Cloud Storage.

---

## Code Structure

### Key Functions

- `add_income()`: Prompts the user to add income details.
- `add_expenditure()`: Records expenditure details.
- `save_to_csv()`: Saves all financial records into a CSV file.
- `upload_to_gcs(bucket_name)`: Uploads the CSV file to a specified Google Cloud Storage bucket.

### Highlights

- **Data Processing:**
  - Transactions are handled using the `pandas` library for easy manipulation and export to CSV.

- **Cloud Integration:**
  - Uses `google-cloud-storage` for seamless interaction with Google Cloud Storage buckets.

- **Error Handling:**
  - Checks for valid inputs and gracefully handles exceptions, such as missing credentials or invalid bucket names.

---

## Example Workflow

1. **Adding Data:**
   ```text
   Enter your choice: 1
   Enter income source: Salary
   Enter amount: 5000
   ```

2. **Saving Data:**
   ```text
   Enter your choice: 7
   Data saved to finance_records.csv
   ```

3. **Uploading to Google Cloud:**
   ```text
   Enter your choice: 8
   Enter your Google Cloud Storage bucket name: my-finance-bucket
   File uploaded successfully!
   ```

---

## Future Enhancements

- Add a graphical interface for easier interaction.
- Include data visualization tools to analyze spending patterns.
- Support for additional cloud storage providers.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributions

Contributions are welcome! Feel free to fork the repository and submit a pull request with your improvements or ideas.

---

## Contact

For any questions or feedback, please contact "caonguyenvu2016@gmail.com"
