# Email Word Spam Probability using Bayes’ Theorem

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def get_inputs():
    total_emails = get_positive_int("Enter total number of emails: ")
    emails_with_free = get_positive_int("Enter number of emails containing 'free': ")
    spam_emails = get_positive_int("Enter number of spam emails: ")
    spam_and_free = get_positive_int("Enter number of emails that are both spam and contain 'free': ")

    # Validation
    if (emails_with_free > total_emails or
        spam_emails > total_emails or
        spam_and_free > emails_with_free or
        spam_and_free > spam_emails):
        print("Input values are inconsistent. Please try again.")
        return get_inputs()
    return total_emails, emails_with_free, spam_emails, spam_and_free

def main():
    print("Calculate P(Spam | Email contains 'free') using Bayes' Theorem\n")
    total_emails, emails_with_free, spam_emails, spam_and_free = get_inputs()

    # Probabilities
    P_spam = spam_emails / total_emails
    P_free = emails_with_free / total_emails
    P_free_given_spam = spam_and_free / spam_emails

    # Bayes' Theorem
    if P_free == 0:
        print("Cannot compute probability: No emails contain 'free'.")
        return

    P_spam_given_free = (P_free_given_spam * P_spam) / P_free

    print(f"\nP(Spam | Email contains 'free') = {P_spam_given_free:.4f}")

if __name__ == "__main__":
    main()
