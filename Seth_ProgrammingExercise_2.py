def get_spam_keywords():
# List the 30 common spam words
    return [
        "free", "winner", "cash", "buy now", "limited time", "guarantee",
        "offer", "click here", "act now", "credit", "urgent", "money back",
        "congratulations", "risk-free", "easy money", "weight loss",
        "miracle", "apply now", "100% free", "trial", "instant", "deal",
        "amazing", "exclusive", "no cost", "winner guaranteed",
        "extra income", "earn money", "lowest price", "get paid"
    ]


def analyze_message(message, spam_keywords):
    score = 0
    found_words = []
    message_lower = message.lower()

    for word in spam_keywords:
        if word in message_lower:
            score += 1
            found_words.append(word)

    return score, found_words


def rate_spam(score):
    if score == 0:
        return "Not Spam"
    elif score <= 3:
        return "Slight chance of Spam"
    elif score <= 7:
        return "Likely Spam"
    else:
        return "Definitely Spam"


def main():
    print("=== Spam Detector ===")
    email_message = input("Enter your email message:\n")

    spam_keywords = get_spam_keywords()
    score, found_words = analyze_message(email_message, spam_keywords)
    rating = rate_spam(score)

    print("\n--- Analysis Result ---")
    print(f"Spam Score: {score}")
    print(f"Rating: {rating}")
    if found_words:
        print("Triggered words/phrases:")
        for word in found_words:
            print(f"- {word}")
    else:
        print("No spam keywords found.")


if __name__ == "__main__":
    main()
