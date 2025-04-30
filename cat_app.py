from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__, template_folder='cat_templates')

# Temporary in-memory store for user messages
god_messages = []

# Route for homepage
@app.route("/")
def cat_index():
    return render_template("cat_index.html")

# Route for "Talk to God" form submission
@app.route("/talk_to_god", methods=["POST"])
def talk_to_god():
    user_message = request.form.get("message", "")
    
    if user_message:
        # Store the message temporarily in memory
        god_messages.append(f"Message from user: {user_message}")
    
    return redirect("/")  # Redirect back to the homepage

# Route for the "Talk to God" page (optional)
@app.route("/talk_to_god_page")
def talk_to_god_page():
    return render_template("talk_to_god.html")

# Route to view all messages (optional)
@app.route("/view_messages")
def view_messages():
    return "<br>".join(god_messages) or "No messages yet."

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

        return redirect("/")

    return render_template("cat_add.html")

# Route for searching counseling forms
@app.route("/cat_search")
def cat_search():
    return render_template("cat_search.html")

if __name__ == "__main__":
    app.run(debug=True)
