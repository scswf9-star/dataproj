from piboufilings import get_filings

# Remember to replace with your actual email for the User-Agent
USER_AGENT_EMAIL = "yourname@example.com"
USER_NAME = "Your Name or Company" # Add your name or company

get_filings(
    user_name=USER_NAME,
    user_agent_email=USER_AGENT_EMAIL,
    cik="0001067983",              # Example: Berkshire Hathaway CIK
    form_type=["13F-HR", "NPORT-P"], # Can be a string or list of strings
    start_year=2023,
    end_year=2023,
    base_dir="./my_sec_data_testing",       # Optional: Custom directory for parsed CSVs
    log_dir="./my_sec_logs_testing",        # Optional: Custom directory for logs
    keep_raw_files=True            # Optional: Set to False to delete raw .txt files after parsing
)