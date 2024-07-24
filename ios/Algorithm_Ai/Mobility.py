def classify_age(age):
    if age < 18:
        return "Child"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"

def mobility_recommendation(age_group):
    if age_group == "Child":
        return "Encourage physical activities and outdoor play."
    elif age_group == "Adult":
        return "Engage in regular exercise and maintain an active lifestyle."
    else:
        return "Stay physically active with gentle exercises like walking or yoga."

def assistance_needed(age_group, mobility_level, with_nurse=False):
    if mobility_level == "Limited":
        if with_nurse:
            return "May require assistance from the nurse for mobility and daily tasks."
        else:
            return "Assistance from caregivers or family members may be needed for mobility and daily tasks."
    else:
        return "Independent mobility. Assistance may be required for specific tasks or activities."

# Example usage:
ages = [5, 30, 70]  # Ages of individuals
mobility_levels = ["Limited", "Independent", "Independent"]  # Mobility levels of individuals
for age, mobility_level in zip(ages, mobility_levels):
    age_group = classify_age(age)
    print(f"Age: {age}, Age Group: {age_group}")
    print("Mobility Recommendation:", mobility_recommendation(age_group))
    print("Assistance Needed:", assistance_needed(age_group, mobility_level, with_nurse=True))  # Include nurse assistance
    print()

