def input_gender():
    while True:
        gender = str(input("\nAre you MALE or FEMALE? ")).lower()

        if gender == "male":
            return gender

        elif gender == "female":
            return gender

        else:
            print(f"Invalid input {gender}. ")
            continue


def input_stats():
    weight = float(input("\nEnter your BODY WEIGHT in lbs: "))
    height = float(input("Enter your HEIGHT in inches: "))
    age = float(input("Enter your age in years: "))

    stats = [weight, height, age]
    return stats


def input_activity():
    print("\n1. Sedentary (little or no exercise)")
    print("2. Lightly active (light exercise/sports 1-3 days/week)")
    print("3. Moderately active (moderate exercise/sports 3-5 days/week)")
    print("4. Very active (hard exercise/sports 6-7 days a week)")
    print("5. Extra active (very hard exercise/sports & physical job or 2x training)")

    while True:
        activity = input("\nHow active are you? ")

        if activity.isdigit():
            activity = int(activity)

        else:
            print(
                f"Invalid input {activity}. Activity level must be a number.")
            continue

        if 1 <= activity <= 5:
            return int(activity)

        else:
            print(
                f"Invalid input {activity}. Must be an activity level from 1 to 5.")
            continue


def calculate_bmr(gender, stats):
    if gender == "male":
        bmr = 66 + (6.3 * stats[0]) + (12.9 * stats[1]) - (6.8 * stats[2])
        return bmr

    else:
        bmr = 655 + (4.3 * stats[0]) + (4.7 * stats[1]) - (4.7 * stats[2])
        return bmr


def calculate_caloric_needs(bmr, activity):
    if activity == 1:
        caloric_needs = round(bmr * 1.2)
        print(
            f"\nYour daily caloric maintenance is approximately {caloric_needs} calories.")

    elif activity == 2:
        caloric_needs = round(bmr * 1.375)
        print(
            f"\nYour daily caloric maintenance is approximately {caloric_needs} calories.")

    elif activity == 3:
        caloric_needs = round(bmr * 1.55)
        print(
            f"\nYour daily caloric maintenance is approximately {caloric_needs} calories.")

    elif activity == 4:
        caloric_needs = round(bmr * 1.725)
        print(
            f"\nYour daily caloric maintenance is approximately {caloric_needs} calories.")

    else:
        caloric_needs = round(bmr * 1.9)
        print(
            f"\nYour daily caloric maintenance is approximately {caloric_needs} calories.")


def run_calculator():
    print("\nNOTE: This calculator utilizes the BASAL METABOLIC RATE method.\nSource: http://www.checkyourhealth.org/eat-healthy/cal_calculator.php")

    gender = input_gender()
    stats = input_stats()
    activity = input_activity()
    bmr = calculate_bmr(gender, stats)

    calculate_caloric_needs(bmr, activity)


run_calculator()
