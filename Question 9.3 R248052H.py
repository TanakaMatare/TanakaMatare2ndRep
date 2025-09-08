#Question 9 (4 tasks)

import re

# Part I: Extract email addresses
def extract_emails(text):
    """Extract all email addresses from the given text."""
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

# Part II: Validate date in YYYY-MM-DD format
def validate_date(date_str):
    """Validate a date in the format YYYY-MM-DD."""
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    return bool(re.match(pattern, date_str))

# Part III: Replace all occurrences of a word with another word
def replace_word(text, old_word, new_word):
    """Replace all occurrences of old_word with new_word in the text."""
    return re.sub(rf'\b{re.escape(old_word)}\b', new_word, text)

# Part IV: Split a string by all non-alphanumeric characters
def split_non_alphanumeric(text):
    """Split the string by all non-alphanumeric characters."""
    return re.split(r'\W+', text)

def main():
    # Part I
    user_text = input("Enter a text containing email addresses: ")
    emails = extract_emails(user_text)
    print("Extracted emails:", emails)

    # Part II
    date_input = input("\nEnter a date in YYYY-MM-DD format: ")
    if validate_date(date_input):
        print(f"{date_input} is a valid date format.")
    else:
        print(f"{date_input} is NOT a valid date format.")

    # Part III
    text_to_replace = input("\nEnter a text to perform word replacement: ")
    old_word = input("Enter the word to replace: ")
    new_word = input("Enter the new word: ")
    updated_text = replace_word(text_to_replace, old_word, new_word)
    print("Updated text:", updated_text)

    # Part IV
    text_to_split = input("\nEnter a text to split by non-alphanumeric characters: ")
    split_list = split_non_alphanumeric(text_to_split)
    print("Split result:", split_list)

if __name__ == "__main__":
    main()
