import tkinter as tk
# Defining my function to calculate BMI:
def BMI_calc():
    # Convert height to meters
    height_m = float(height_entry.get())/100
    # BMI rule 
    BMI = float(weight_entry.get()) / (height_m ** 2)
    # Update the results label:
    result_label.config(text = "Your BMI is: {:.2f}".format(BMI))
    weight_category_label.config(text="Weight category is: {}".format(weight_category(BMI)))

# Defining the weight category the patient in:
def weight_category(BMI):
    if BMI < 18.5:
        return "Underweight"
    elif 18.5 <= BMI <25:
        return "Normal Weight"
    elif 25 <= BMI < 30:
        return "Overweight"
    else:
        return "Obese"

window = tk.Tk()
window.title = ('BMI Calculator')

# Create and position the labels and entry fields
weight_label = tk.Label(window, text="Weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

height_label = tk.Label(window, text="Height (cm):")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()

result_label = tk.Label(window, text="Your BMI is:")
result_label.pack()

weight_category_label = tk.Label(window, text="Weight category:")
weight_category_label.pack()

calculate_button = tk.Button(window, text="Calculate", command=BMI_calc)
calculate_button.pack()

# Start the main event loop
window.mainloop()
