def get_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"
    
def get_advice(category):
    if category == "Underweight":
        return "Try to eat more nutritious food."
    elif category == "Normal weight":
        return "Great! Keep maintaining your lifestyle."
    elif category == "Overweight":
        return "Consider adding exercise to your routine."
    else:
        return "Consult a doctor for a health plan."

def show_result(name, bmi, category, advice):
    print("---------------------------")
    print("Name    :", name)
    print("BMI     :", bmi)
    print("Status  :", category)
    print("Advice  :", advice)
    print("---------------------------")

# Main program
name = input("Enter your name: ")
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = get_bmi(weight, height)
category = get_category(bmi)
advice = get_advice(category)
show_result(name, bmi, category, advice)
