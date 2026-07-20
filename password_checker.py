def check_password_strength(password):
    length_ok = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    score = sum([length_ok, has_upper, has_digit, has_symbol])

    if not length_ok:
        return "Weak (Password must be at least 8 characters)"
    elif score == 4:
        return "Strong"
    elif score >= 2:
        return "Medium"
    else:
        return "Weak"


def main():
    print("=== Password Strength Checker ===")
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print(f"\nPassword Strength: {result}")


if __name__ == "__main__":
    main()