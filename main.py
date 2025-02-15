import re

# Sample text containing different data types
text = """
Contact us at user@example.com or firstname.lastname@company.co.uk.
Visit https://www.example.com and https://subdomain.example.org/page for more info.
Call (123) 456-7890, 123-456-7890, or 123.456.7890 for support.
The total cost is $1,234.56, but it can also be $19.99.
My credit card number is 4111-1111-1111-1111 and my other card is 1234 5678 9876 5432.
Meeting time is 02:30 PM or 14:30.
Here is a <div>HTML</div> tag.
Here is a <a href='#'>Link</a> tag.
Don't forget to check #hashtag.
"""

# Regex patterns
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
url_pattern = r"https?://[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})+(?:/[^\s]*)?"
phone_pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
credit_card_pattern = r"\b(?:\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}|\d{4} \d{4} \d{4} \d{4})\b"
time_pattern = r"(\d{1,2}):([0-5][0-9])\s?(AM|PM)?|(\d{2}):([0-5][0-9])"
html_tag_pattern = r"<([a-zA-Z0-9]+)([^<>]*)>(.*?)</\1>|<([a-zA-Z0-9]+)([^<>]*)/?>"
hashtag_pattern = r"#\w+"
currency_pattern = r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"

# Function to extract data using regex
def extract_data(text):
    # Extract emails
    emails = re.findall(email_pattern, text)
    
    # Extract URLs
    urls = re.findall(url_pattern, text)
    
    # Extract phone numbers
    phones = re.findall(phone_pattern, text)
    
    # Extract credit card numbers
    credit_cards = re.findall(credit_card_pattern, text)
    
    # Extract times
    times = re.findall(time_pattern, text)
    # Filter out extra empty groups
    times = [(h, m, ampm) for h, m, ampm, _, _ in times if h]  # Keep only valid groups
    
    # Extract HTML tags (corrected regex to capture full tag with attributes)
    html_tags = re.findall(html_tag_pattern, text)
    # Format to match the expected output (full HTML tag with attributes)
    html_tags = [
        f"<{tag[0]}{tag[1]}>{tag[2]}</{tag[0]}>" if tag[0] else f"<{tag[3]}{tag[4]}/>"
        for tag in html_tags
    ]
    
    # Extract hashtags
    hashtags = re.findall(hashtag_pattern, text)
    
    # Extract currency amounts
    currencies = re.findall(currency_pattern, text)
    
    return emails, urls, phones, credit_cards, times, html_tags, hashtags, currencies

# Example usage (you can call this function in another script or test file)
if __name__ == "__main__":
    emails, urls, phones, credit_cards, times, html_tags, hashtags, currencies = extract_data(text)
    print("Emails:", emails)
    print("URLs:", urls)
    print("Phone Numbers:", phones)
    print("Credit Cards:", credit_cards)
    print("Times:", times)
    print("HTML Tags:", html_tags)
    print("Hashtags:", hashtags)
    print("Currency Amounts:", currencies)
