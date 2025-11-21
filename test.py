
import sys
import pandas as pd

try:
    # Import the library
    from piboufilings import FilingsDownloader, FilingsParser
except ImportError:
    print("PibouFilings is not installed. Install it with: pip install piboufilings")
    sys.exit(1)

# Example CIK for Berkshire Hathaway (0001067983)
CIK = "0001067983"

# Initialize downloader
downloader = FilingsDownloader()

try:
    # Download the last 5 13F filings for the given CIK
    filings_paths = downloader.download_filings(
        cik=CIK,
        form_type="13F-HR",
        count=5,  # number of filings to fetch
        download_dir="sec_filings"  # local folder to store files
    )
    print(f"Downloaded {len(filings_paths)} filings.")
except Exception as e:
    print(f"Error downloading filings: {e}")
    sys.exit(1)

# Initialize parser
parser = FilingsParser()

all_holdings = []

# Parse each downloaded filing
for filing_path in filings_paths:
    try:
        parsed_data = parser.parse_filing(filing_path)
        # Convert parsed data to DataFrame
        df = pd.DataFrame(parsed_data["holdings"])
        df["filing_date"] = parsed_data.get("filing_date")
        all_holdings.append(df)
    except Exception as e:
        print(f"Error parsing {filing_path}: {e}")

# Combine all filings into one DataFrame
if all_holdings:
    combined_df = pd.concat(all_holdings, ignore_index=True)
    print("\nSample parsed holdings data:")
    print(combined_df.head())
else:
    print("No holdings data parsed.")

