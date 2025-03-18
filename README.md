Web Content Q&A Tool
A lightweight, web-based application that ingests content from URLs and answers questions based exclusively on that content. Built as a functional prototype, it prioritizes simplicity and usability.

Features
Ingests web content from provided URLs.
Answers questions using a keyword-matching approach based solely on the ingested content.
Minimal, user-friendly interface with sections for URL input and Q&A.

Setup Instructions
Prerequisites
Python 3.x installed (download here).
Git installed for cloning the repository (download here).
Steps to Run Locally

1. Clone the Repository
Open a terminal and run:
git clone <repository-url>
cd web-qa-tool

2. Install Dependencies
Ensure you're in the project directory, then install the required packages:
pip install -r requirements.txt

3. Launch the Application
Start the Flask server:
python app.py

4. Access the Tool
Open your browser and navigate to:
http://localhost:5000

Deliverables

Live Demo: No hosted version is available due to time constraints, but the local setup is fully operational.

Source Code: Included in this repository; feel free to fork or push to your own GitHub repo.

Instructions: Detailed in this README.md.

Evaluation Notes

Relevance & Accuracy:

The tool uses a simple keyword-matching algorithm to ensure answers are grounded in the scraped content. It performs well for direct questions but may falter with complex or nuanced queries.

UI/UX:

The interface is clean and intuitive, featuring two distinct sections: one for URL ingestion and another for question-answering.

Code Clarity:

The implementation leverages Flask routes, with modular functions for content ingestion and question processing. Inline comments clarify key logic for easy understanding.

Limitations & Future Improvements

Developed within a 24-hour timeframe, this prototype meets core requirements but could be enhanced for production use:

Upgrade NLP capabilities (e.g., integrate transformer-based models).

Add robust error handling for invalid URLs or unexpected inputs.

Deploy to a cloud platform for public access.

Need Help?

If you encounter issues with setup, deployment, or testing, feel free to reach out!
