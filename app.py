import json
import os

os.makedirs("data", exist_ok=True)


def create_karvand(pk, full_name, email, city, education_degree, education_field, skills):
    return {
        "id": pk,
        "full_name": full_name,
        "email": email,
        "city": city,
        "education": {
            "degree": education_degree,
            "field": education_field
        },
        "skills": skills
    }


while True:
    command = input(
        "\nPlease enter your command:\n"
        "1. Add karvand\n"
        "2. Show karvands\n"
        "3. Exit\n> "
    )

    match command:
        case "1":
            full_name = input("Please enter your full name: ")
            email = input("Please enter your email: ")
            city = input("Please enter your city: ")
            education_degree = input("Please enter your education degree: ")
            education_field = input("Please enter your education field: ")

            skills = []

            while True:
                print("\nAdd Skill")

                skill_name = input("Skill name: ")
                skill_level = input("Skill level: ")

                while True:
                    try:
                        skill_score = int(input("Skill score (0-100): "))
                        if 0 <= skill_score <= 100:
                            break
                        print("Score must be between 0 and 100.")
                    except ValueError:
                        print("Please enter a valid number.")

                skills.append({
                    "name": skill_name,
                    "level": skill_level,
                    "score": skill_score
                })

                another = input("Add another skill? (y/n): ").lower()
                if another != "y":
                    break

            try:
                with open("./data/karvands.json", "r", encoding="utf-8") as file:
                    data = json.load(file)

            except (FileNotFoundError, json.JSONDecodeError):
                data = {
                    "bootcamp": {
                        "title": "Karvand Python",
                        "year": 2026
                    },
                    "karvands": []
                }

            pk = max((k["id"] for k in data["karvands"]), default=0) + 1

            data["karvands"].append(
                create_karvand(
                    pk,
                    full_name,
                    email,
                    city,
                    education_degree,
                    education_field,
                    skills
                )
            )

            with open("./data/karvands.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)

            print("Karvand added successfully.")

        case "2":
            try:
                with open("./data/karvands.json", "r", encoding="utf-8") as file:
                    data = json.load(file)

                if not data["karvands"]:
                    print("No karvands found.")
                    continue

                for karvand in data["karvands"]:
                    print("-" * 40)
                    print(f"ID: {karvand['id']}")
                    print(f"Name: {karvand['full_name']}")
                    print(f"Email: {karvand['email']}")
                    print(f"City: {karvand['city']}")
                    print(
                        f"Education: {karvand['education']['degree']} - "
                        f"{karvand['education']['field']}"
                    )

                    print("Skills:")
                    for skill in karvand["skills"]:
                        print(
                            f"  - {skill['name']} | "
                            f"{skill['level']} | "
                            f"{skill['score']}"
                        )

            except (FileNotFoundError, json.JSONDecodeError):
                print("No karvands found.")

        case "3":
            break

        case _:
            print("Invalid command.")