import pytest
from main import extract_data  # or the appropriate import statement based on your project structure

# Test for Email Extraction
@pytest.mark.parametrize("text, expected", [
    ("user@example.com", ["user@example.com"]),
    ("firstname.lastname@company.co.uk", ["firstname.lastname@company.co.uk"]),
])
def test_email_extraction(text, expected):
    emails, _, _, _, _, _, _, _ = extract_data(text)
    assert emails == expected

# Test for URL Extraction
@pytest.mark.parametrize("text, expected", [
    ("https://www.example.com", ["https://www.example.com"]),
    ("https://subdomain.example.org/page", ["https://subdomain.example.org/page"]),
])
def test_url_extraction(text, expected):
    _, urls, _, _, _, _, _, _ = extract_data(text)
    assert urls == expected

# Test for Phone Extraction
@pytest.mark.parametrize("text, expected", [
    ("(123) 456-7890", ["(123) 456-7890"]),
    ("123-456-7890", ["123-456-7890"]),
])
def test_phone_extraction(text, expected):
    _, _, phones, _, _, _, _, _ = extract_data(text)
    assert phones == expected

# Test for Currency Extraction
@pytest.mark.parametrize("text, expected", [
    ("$1,234.56", ["$1,234.56"]),
    ("$19.99", ["$19.99"]),
])
def test_currency_extraction(text, expected):
    _, _, _, _, _, _, _, currencies = extract_data(text)
    assert currencies == expected

# Test for Credit Card Extraction
@pytest.mark.parametrize("text, expected", [
    ("4111-1111-1111-1111", ["4111-1111-1111-1111"]),
    ("1234 5678 9876 5432", ["1234 5678 9876 5432"]),
])
def test_credit_card_extraction(text, expected):
    _, _, _, credit_cards, _, _, _, _ = extract_data(text)
    assert credit_cards == expected

# Test for Time Extraction
@pytest.mark.parametrize("text, expected", [
    ("02:30 PM", [("02", "30", "PM")]),
    ("14:30", [("14", "30", "")]),
])
def test_time_extraction(text, expected):
    _, _, _, _, times, _, _, _ = extract_data(text)
    assert times == expected

# Test for HTML Tag Extraction
@pytest.mark.parametrize("text, expected", [
    ("<div>HTML</div>", ["<div>HTML</div>"]),
    ("<a href='#'>Link</a>", ["<a href='#'>Link</a>"]),
])
def test_html_tag_extraction(text, expected):
    _, _, _, _, _, html_tags, _, _ = extract_data(text)
    assert html_tags == expected

# Test for Hashtag Extraction
@pytest.mark.parametrize("text, expected", [
    ("#hashtag", ["#hashtag"]),
    ("Check out #Python and #AI.", ["#Python", "#AI"]),
])
def test_hashtag_extraction(text, expected):
    _, _, _, _, _, _, hashtags, _ = extract_data(text)
    assert hashtags == expected
