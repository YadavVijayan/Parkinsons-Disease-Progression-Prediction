import customtkinter as ctk
import joblib
import numpy as np
import pandas as pd

motor_model=joblib.load("motor_UPDRS_model.pkl")
scaler_x_motor=joblib.load("scalar_x_for_motor_UPDRS")
scaler_y_motor=joblib.load("scalar_y_for_motor_UPDRS")

total_model=joblib.load("total_UPDRS_model.pkl")
scaler_x_total=joblib.load("scalar_x_for_total_UPDRS")
scaler_y_total=joblib.load("scalar_y_for_total_UPDRS")

root = ctk.CTk()
root.geometry("900x700")
root.resizable(False, False)
root.title("UPDRS Predictor")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

heading_label = ctk.CTkLabel(
    root,
    text="Parkinsons UPDRS Predictor",
    font=ctk.CTkFont(size=26, weight="bold")
)
heading_label.pack(pady=20)

input_frame = ctk.CTkFrame(root)
input_frame.pack(pady=10, padx=20, fill="both", expand=True)

all_columns = [
    "age", "test_time", "Jitter(%)", "Jitter(Abs)", "Jitter:RAP", "Jitter:PPQ5",
    "Jitter:DDP", "Shimmer", "Shimmer(dB)", "Shimmer:APQ3", "Shimmer:APQ5",
    "Shimmer:APQ11", "Shimmer:DDA", "NHR", "HNR", "RPDE", "DFA", "PPE", "sex"
]

selected_columns = [
    "age", "Jitter(%)", "Shimmer:APQ11", "NHR", "HNR", "RPDE", "DFA", "PPE"
]

entry_boxes = {}

for i, col in enumerate(all_columns):
    row = i // 2
    col_pos = i % 2

    label = ctk.CTkLabel(input_frame, text=col, font=ctk.CTkFont(size=14))
    label.grid(row=row, column=col_pos * 2, padx=10, pady=8, sticky="e")

    entry = ctk.CTkEntry(input_frame, width=200, placeholder_text=f"Enter {col}")
    entry.grid(row=row, column=col_pos * 2 + 1, padx=10, pady=8, sticky="w")

    entry_boxes[col] = entry

def textbox_entry():
    textbox_entry=entry_box.get("0.0", "end").strip() 
    textbox_values=[val.strip() for val in textbox_entry.split(",")]
    for col, val in zip(all_columns, textbox_values):
        entry_boxes[col].delete(0, ctk.END) 
        entry_boxes[col].insert(0, str(val))


entry_label=ctk.CTkLabel(root,text="Enter values seperated by commas: ")
entry_label.pack()
entry_box=ctk.CTkTextbox(root,width=800,height=10,fg_color="white",text_color="black")
entry_box.pack()

textbox_entry_btn=ctk.CTkButton(root,text="insert values to fields",fg_color="red",text_color="white",command=textbox_entry)
textbox_entry_btn.pack(padx=100,pady=3,side='left')

result=ctk.CTkLabel(input_frame,text_color="white",font=("Arial", 16, "bold"),text="")
result.grid()

def predict():
    data = {}
    for col in selected_columns:
        value = entry_boxes[col].get()
        if value.strip() == "":
            data[col] = None
        else:
            try:
                data[col] = float(value)
            except ValueError:
                data[col] = value 

    motor_inputs=[i for i in data.values()]
    motor_inputs=pd.DataFrame([motor_inputs],columns=selected_columns)
    motor_inputs_x=scaler_x_motor.transform(motor_inputs)
    y_pred_motor_scaled=motor_model.predict(motor_inputs_x)
    y_pred_motor_scaled=y_pred_motor_scaled.reshape(-1,1)
    y_pred_motor=scaler_y_motor.inverse_transform(y_pred_motor_scaled)[0][0]
    motor_UPDRS=y_pred_motor

    
    total_input=list(data.values())
    total_input=np.array([total_input]).reshape(1,-1)
    total_input_x=scaler_x_total.transform(total_input)
    y_pred_total_scaled=total_model.predict(total_input_x)
    y_pred_total_scaled=y_pred_total_scaled.reshape(-1,1)
    y_pred_total=scaler_y_total.inverse_transform(y_pred_total_scaled)[0][0]
    total_UPDRS=y_pred_total

    result.configure(text=f"motor_UPDRS :{motor_UPDRS} \ntotal_UPDRS : {total_UPDRS}")

def clear():
    result.configure(text="")
    for col in all_columns:
        entry_boxes[col].delete(0, ctk.END) 

    entry_box.delete("0.0","end")



clear_buttton=ctk.CTkButton(root,text="clear",fg_color="blue",text_color="white",command=clear)

clear_buttton.pack(side='left',pady=3,padx=80)

predict_buttton=ctk.CTkButton(root,text="Predict",fg_color="green",text_color="white",command=predict)

predict_buttton.pack(side='left',pady=3) 


root.mainloop()
