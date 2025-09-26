# main.py
# may require "pip install numpy"

from neural_net_model import score
import tkinter as tk
from tkinter import messagebox

def predict_value():
    try:
        alpha = float(alpha_entry.get())
        coefficient_drag = float(coeff_drag_entry.get())
        coefficient_lift = float(coeff_lift_entry.get())
        coefficient_moment = float(coeff_moment_entry.get())
        coefficient_parasite_drag = float(coeff_parasite_drag_entry.get())
        reynolds_number = float(reynolds_entry.get())

        input_data = {
            "alpha": alpha,
            "coefficientDrag": coefficient_drag,
            "coefficientLift": coefficient_lift,
            "coefficientMoment": coefficient_moment,
            "coefficientParasiteDrag": coefficient_parasite_drag,
            "reynoldsNumber": reynolds_number
        }

        prediction = score(input_data, {})
        result_label.config(text=f"Predicted topXTR: {prediction:.4f}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numerical values for all fields.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

root = tk.Tk()
root.title("Neural Network Predictor")
root.geometry("400x350")
root.resizable(False, False)

input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack(pady=10)

inputs = {
    "alpha": None,
    "coefficientDrag": None,
    "coefficientLift": None,
    "coefficientMoment": None,
    "coefficientParasiteDrag": None,
    "reynoldsNumber": None
}

row = 0
for text in inputs:
    label = tk.Label(input_frame, text=f"Enter {text}:")
    label.grid(row=row, column=0, sticky="w", pady=5)
    entry = tk.Entry(input_frame)
    entry.grid(row=row, column=1, pady=5)
    inputs[text] = entry
    row += 1

alpha_entry = inputs["alpha"]
coeff_drag_entry = inputs["coefficientDrag"]
coeff_lift_entry = inputs["coefficientLift"]
coeff_moment_entry = inputs["coefficientMoment"]
coeff_parasite_drag_entry = inputs["coefficientParasiteDrag"]
reynolds_entry = inputs["reynoldsNumber"]

predict_button = tk.Button(root, text="Predict", command=predict_value)
predict_button.pack(pady=10)

result_label = tk.Label(root, text="Predicted topXTR: ", font=("Helvetica", 12))
result_label.pack(pady=10)

root.mainloop()
