from flask import Flask, render_template, request, redirect
import gspread
import os
import json
from google.oauth2.service_account import Credentials

app = Flask(__name__, template_folder='cat_templates')

# Google Sheets setup
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive.readonly"
]

# Authentication using service account credentials from environment variable
if "GOOGLE_CREDENTIALS" in os.environ:
    creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])
    creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
else:
    # fallback for local development
    creds = Credentials.from_service_account_file("cat_credentials.json", scopes=scope)

# Authorize gspread with the credentials
client = gspread.authorize(creds)

# Spreadsheet setup
SPREADSHEET_ID = "1vb_dh0SrwmKU8ZmXs0xNod1GJlvcMu-XqbyymeAkdyg"
try:
    sheet = client.open_by_key(SPREADSHEET_ID).worksheet("Sheet1")
    print("\u2705 Successfully connected to Google Sheet.")
except Exception as e:
    print(f"❌ ERROR connecting to Google Sheet: {e}")
    sheet = None  # Prevent crashing if connection fails

# Route for homepage
@app.route("/")
def cat_index():
    return render_template("cat_index.html")

# Route for "Talk to God" form submission
@app.route("/talk_to_god", methods=["POST"])
def talk_to_god():
    user_message = request.form.get("message", "")
    
    if user_message:
        # Define the path where you want to store the messages.txt
        message_file_path = os.path.join(os.path.dirname(__file__), 'static', 'messages', 'messages.txt')
        
        # Ensure the directory exists
        os.makedirs(os.path.dirname(message_file_path), exist_ok=True)
        
        # Save the message to the messages.txt file
        try:
            with open(message_file_path, "a") as file:
                file.write(f"Message from user: {user_message}\n")
                file.write("-" * 40 + "\n")
            print("✅ Message saved.")
        except Exception as e:
            print(f"❌ Error saving message: {e}")
    
    return redirect("/")  # Redirect back to the homepage

# Route for the "Talk to God" page (optional)
@app.route("/talk_to_god_page")
def talk_to_god_page():
    return render_template("talk_to_god.html")

# Route for adding counseling form
@app.route("/cat_add", methods=["GET", "POST"])
def cat_add_form():
    if request.method == "POST":
        data = [
            request.form.get("session", ""),
            request.form.get("form_number", ""),
            request.form.get("date", ""),
            request.form.get("name", ""),
            request.form.get("admission_class", ""),
            request.form.get("father_name", ""),
            request.form.get("father_occupation", ""),
            request.form.get("address", ""),
            request.form.get("referred_by", ""),
            request.form.get("last_school", ""),
            request.form.get("phone", ""),
            request.form.get("school_visited", ""),
            request.form.get("proposed_fees", ""),
            request.form.get("discount_given", ""),
            request.form.get("fee_agreement", ""),
            request.form.get("comments", ""),
            request.form.get("counseled_by", ""),
            request.form.get("principals_comments", "")
        ]

        if sheet:
            try:
                sheet.append_row(data)
                print("\u2705 Data successfully saved to Google Sheet.")
            except Exception as e:
                print(f"❌ ERROR saving data to Google Sheet: {e}")
        else:
            print("\u274c No sheet connection available.")
        return redirect("/")

    return render_template("cat_add.html")

# Route for searching counseling forms
@app.route("/cat_search")
def cat_search():
    return render_template("cat_search.html")

if __name__ == "__main__":
    app.run(debug=True)
