def calculate_spam_score(message, trigger_list):
    """
    Scans the message and calculates the total spam score.
    :param message: str (The email content)
    :param trigger_list: list (A list of triggers)
    :return: tuple (int score, list found_words)
    """

    score = 0
    found_words = []

    # Convert message to lowercase for case-insensitive matching
    lowered_message = message.lower()

    for trigger in trigger_list:
        if trigger in lowered_message:
            # Count how many times the phrase appears
            occurrences = lowered_message.count(trigger)
            score += occurrences
            found_words.append(trigger)

    return score, found_words

def rate_spam_likelihood(score):
    """
    Determines the likelihood of spam given the total spam score.
    :param score: int
    :return: str (The spam likelihood)
    """

    if score == 0:
        return "Not Spam"
    elif 1 <= score <= 2:
        return "Low Likelihood"
    elif 3 <= score <= 5:
        return "Moderate Likelihood"
    else:
        return "High Likelihood"

def main():
    # 30 triggers
    spam_triggers = [
        "Claim your prize", "Free money", "Fast cash", "Please read", "Urgent",
        "Act now", "Limited time", "Exclusive deal", "Click here", "Hidden charges",
        "No fees", "Great offer", "Newsletter", "Get paid", "Best rates", "Save",
        "Be your own boss", "Cashback", "Today only", "Time-sensitive", "Trial",
        "Mega sale", "Supplements", "Pre-approved", "Life-changing", "Ultimate",
        "Important notice", "Attention", "Click here", "Dear beneficiary"
    ]

    print("---Email Spam Scanner ---")
    user_email = input("Enter the email message body to scan:\n ")

    # Step 1: Calculate Score
    final_score, detected_words = calculate_spam_score(user_email, spam_triggers)

    # Step 2: Get Likelihood
    likelihood = rate_spam_likelihood(final_score)

    # Step 3: Display Results
    print("\n--- Scan Results ---")
    print(f"Spam Score: {final_score}")
    print(f"Likelihood: {likelihood}")

    if detected_words:
        print("\n--- Detected words ---")
    else:
        print("No common spam triggers detected")

if __name__ == "__main__":
    main()
