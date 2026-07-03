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

def search_karvand_by_id():
    try:
        with open("./data/karvands.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        if not data["karvands"]:
            print("No karvands found.")
            return

        try:
            search_id = int(input("Enter karvand id: "))
        except ValueError:
            print("ID must be a number.")
            return

        for karvand in data["karvands"]:
            if karvand["id"] == search_id:
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
                return

        print("Karvand not found.")

    except (FileNotFoundError, json.JSONDecodeError):
        print("No karvands found.")

def search_karvand_by_skill():
    try:
        with open("./data/karvands.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        if not data["karvands"]:
            print("No karvands found.")
            return

        skill_name = input("Enter skill name: ").strip().lower()

        found = False

        for karvand in data["karvands"]:
            for skill in karvand["skills"]:
                if skill["name"].lower() == skill_name:
                    found = True

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
                    for s in karvand["skills"]:
                        print(
                            f"  - {s['name']} | "
                            f"{s['level']} | "
                            f"{s['score']}"
                        )
                    break

        if not found:
            print("No karvand found with this skill.")

    except (FileNotFoundError, json.JSONDecodeError):
        print("No karvands found.")

def edit_karvand():
    try:
        with open("./data/karvands.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        if not data["karvands"]:
            print("No karvands found.")
            return

        try:
            search_id = int(input("Enter karvand id: "))
        except ValueError:
            print("ID must be a number.")
            return

        for karvand in data["karvands"]:
            if karvand["id"] == search_id:
                print("Leave empty to keep current value.")

                email = input(f"Email ({karvand['email']}): ")
                city = input(f"City ({karvand['city']}): ")
                degree = input(f"Degree ({karvand['education']['degree']}): ")
                field = input(f"Field ({karvand['education']['field']}): ")

                if email:
                    karvand["email"] = email

                if city:
                    karvand["city"] = city

                if degree:
                    karvand["education"]["degree"] = degree

                if field:
                    karvand["education"]["field"] = field

                with open("./data/karvands.json", "w", encoding="utf-8") as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)

                print("Karvand updated successfully.")
                return

        print("Karvand not found.")

    except (FileNotFoundError, json.JSONDecodeError):
        print("No karvands found.")

def delete_karvand():
    try:
        with open("./data/karvands.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        if not data["karvands"]:
            print("No karvands found.")
            return

        try:
            search_id = int(input("Enter karvand id to delete: "))
        except ValueError:
            print("ID must be a number.")
            return

        for i, karvand in enumerate(data["karvands"]):
            if karvand["id"] == search_id:
                data["karvands"].pop(i)

                with open("./data/karvands.json", "w", encoding="utf-8") as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)

                print("Karvand deleted successfully.")
                return

        print("Karvand not found.")

    except (FileNotFoundError, json.JSONDecodeError):
        print("No karvands found.")

def generate_report():
    try:
        with open("./data/karvands.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        karvands = data.get("karvands", [])
        if not karvands:
            print("No karvands found to generate a report.")
            return

        total_karvands = len(karvands)
        total_skills = 0
        total_score = 0
        cities = set()
        unique_skills = set()

        for karvand in karvands:
            cities.add(karvand["city"])
            for skill in karvand["skills"]:
                total_skills += 1
                total_score += skill["score"]
                unique_skills.add(skill["name"])

        average_skill_score = (total_score / total_skills) if total_skills > 0 else 0

        report_data = {
            "total_karvands": total_karvands,
            "total_skills": total_skills,
            "average_skill_score": round(average_skill_score, 2),
            "cities": list(cities),
            "unique_skills": list(unique_skills)
        }

        print("-" * 40)
        print("General Report:")
        print(f"Total Karvands: {report_data['total_karvands']}")
        print(f"Total Skills: {report_data['total_skills']}")
        print(f"Average Skill Score: {report_data['average_skill_score']}")
        print(f"Registered Cities: {', '.join(report_data['cities'])}")
        print(f"Unique Skills: {', '.join(report_data['unique_skills'])}")
        print("-" * 40)

        with open("./data/report.json", "w", encoding="utf-8") as r_file:
            json.dump(report_data, r_file, indent=4, ensure_ascii=False)

        print("Report successfully generated and saved to 'data/report.json'.")

    except (FileNotFoundError, json.JSONDecodeError):
        print("No valid data found to generate a report.")

while True:
    command = input(
        "\nPlease enter your command:\n"
        "1. Add karvand\n"
        "2. Show karvands\n"
        "3. Search by id\n"
        "4. Search by skill\n"
        "5. Edit karvand\n"
        "6. Delete karvand\n"
        "7. General Report\n"
        "8. Exit\n> "
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
            search_karvand_by_id()

        case "4":
            search_karvand_by_skill()

        case "5":
            edit_karvand()

        case "6":
            delete_karvand()

        case "7":
            generate_report()

        case "8":
            break

        case _:
            print("Invalid command.")