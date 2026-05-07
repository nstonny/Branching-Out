"""Utilities to filter and print users loaded from `users.json`."""

import json

def filter_users_by_name(name):
    """Print users whose `name` matches the given value (case-insensitive)."""
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)

def filter_users_by_age(age):
    """Print users whose `age` exactly matches the given integer value."""
    with open("users.json", "r") as file:
        users = json.load(file)
    filtered_users = [user for user in users if user["age"] == age]
    for user in filtered_users:
        print(user)

def filter_users_by_email(email):
    """Print users whose `email` exactly matches the given value."""
    with open("users.json", "r") as file:
        users = json.load(file)
    filtered_users = [user for user in users if user["email"] == email]
    for user in filtered_users:
        print(user)


def main():
    """Run the interactive prompt for selecting and applying user filters."""
    filter_option = input("What would you like to filter by? (Currently, only 'name' is supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = int(input("Enter an age to filter users: "))
        filter_users_by_age(age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()

