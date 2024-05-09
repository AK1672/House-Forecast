import tkinter as tk
from tkinter import *
import joblib

model=joblib.load("House.joblib")

def predict_price():
    try:
        bedrooms = int(bedrooms_entry.get())
        bathrooms = int(bathrooms_entry.get())
        living_area = int(living_area_entry.get())
        lot_area = int(lot_area_entry.get())
        num_floors = int(floors_entry.get())
        num_views = int(views_entry.get())
        grade = int(grade_entry.get())
        house_area = int(house_area_entry.get())
        basement_area = int(basement_area_entry.get())
        built_year = int(built_year_entry.get())
        renovation_year = int(renovation_year_entry.get())
        postal_code = int(postal_code_entry.get())
        latitude = float(latitude_entry.get())
        longitude = float(longitude_entry.get())
        living_area_renov = int(living_area_renov_entry.get())
        lot_area_renov = int(lot_area_renov_entry.get())

        features = [[bedrooms, bathrooms, living_area, lot_area, num_floors, num_views, grade,
                     house_area, basement_area, built_year, renovation_year, postal_code, latitude, longitude,
                     living_area_renov, lot_area_renov]]
        predicted_price = model.predict(features)
        result_label.config(text="Predicted Price: " + str(round(predicted_price[0],3))+" Lakhs.\nEstimated Range : "+str(round(predicted_price[0]-0.7,3))+"-"+str(round(predicted_price[0]+0.7,3))+" Lakhs")
    except ValueError:
        result_label.config(text="Error, Please enter valid values.")

def toggle_features():
    if toggle_button.cget("text") == "Show Additional Features":
        toggle_button.config(text="Hide Additional Features")
        additional_features_frame.pack()
    else:
        toggle_button.config(text="Show Additional Features")
        additional_features_frame.pack_forget()

root = tk.Tk()
root.title("House Price Prediction")
root.geometry("800x600")
bg = PhotoImage(file = "bg.png")
label1 = Label( root, image = bg)
label1.place(relheight=1, relwidth= 1)


header = tk.Frame(root)
header.pack(pady=10)
tk.Label(header,text="Real Estate Price Prediction",fg="blue",bg="Yellow",relief="solid",font=("arial",25,"bold")).grid(row=0, column=0)

main_features_frame = tk.Frame(root)
main_features_frame.pack(pady=10)


tk.Label(main_features_frame, text="Number of Bedrooms:").grid(row=0, column=0)
bedrooms_entry = tk.Entry(main_features_frame)
bedrooms_entry.grid(row=0, column=1)

tk.Label(main_features_frame, text="Number of Bathrooms:").grid(row=1, column=0)
bathrooms_entry = tk.Entry(main_features_frame)
bathrooms_entry.grid(row=1, column=1)

tk.Label(main_features_frame, text="Living Area:").grid(row=2, column=0)
living_area_entry = tk.Entry(main_features_frame)
living_area_entry.grid(row=2, column=1)

tk.Label(main_features_frame, text="Latitude:").grid(row=3, column=0)
latitude_entry = tk.Entry(main_features_frame)
latitude_entry.grid(row=3, column=1)

tk.Label(main_features_frame, text="Longitude:").grid(row=4, column=0)
longitude_entry = tk.Entry(main_features_frame)
longitude_entry.grid(row=4, column=1)

tk.Label(main_features_frame, text="Postal Code:").grid(row=5, column=0)
postal_code_entry = tk.Entry(main_features_frame)
postal_code_entry.grid(row=5, column=1)

tk.Label(main_features_frame, text="Built Year:").grid(row=6, column=0)
built_year_entry = tk.Entry(main_features_frame)
built_year_entry.grid(row=6, column=1)


additional_features_frame = tk.Frame(root)

tk.Label(additional_features_frame, text="Lot Area:").grid(row=0, column=0)
lot_area_entry = tk.Entry(additional_features_frame)
lot_area_entry.insert(0, "15093")
lot_area_entry.grid(row=0, column=1)

tk.Label(additional_features_frame, text="Number of Floors:").grid(row=1, column=0)
floors_entry = tk.Entry(additional_features_frame)
floors_entry.insert(0, "2")
floors_entry.grid(row=1, column=1)


tk.Label(additional_features_frame, text="Number of Views:").grid(row=2, column=0)
views_entry = tk.Entry(additional_features_frame)
views_entry.insert(0, "0")
views_entry.grid(row=2, column=1)

tk.Label(additional_features_frame, text="Grade of the House:").grid(row=3, column=0)
grade_entry = tk.Entry(additional_features_frame)
grade_entry.insert(0, "8")
grade_entry.grid(row=3, column=1)

tk.Label(additional_features_frame, text="Area of the House (excluding basement):").grid(row=4, column=0)
house_area_entry = tk.Entry(additional_features_frame)
house_area_entry.insert(0, "1802")
house_area_entry.grid(row=4, column=1)

tk.Label(additional_features_frame, text="Area of the Basement:").grid(row=5, column=0)
basement_area_entry = tk.Entry(additional_features_frame)
basement_area_entry.insert(0, "296")
basement_area_entry.grid(row=5, column=1)

tk.Label(additional_features_frame, text="Renovation Year:").grid(row=6, column=0)
renovation_year_entry = tk.Entry(additional_features_frame)
renovation_year_entry.insert(0, "91")
renovation_year_entry.grid(row=6, column=1)

tk.Label(additional_features_frame, text="Living Area (Renovated):").grid(row=7, column=0)
living_area_renov_entry = tk.Entry(additional_features_frame)
living_area_renov_entry.insert(0, "1997")
living_area_renov_entry.grid(row=7, column=1)

tk.Label(additional_features_frame, text="Lot Area (Renovated):").grid(row=8, column=0)
lot_area_renov_entry = tk.Entry(additional_features_frame)
lot_area_renov_entry.insert(0, "12754")
lot_area_renov_entry.grid(row=8, column=1)


toggle_button = tk.Button(root, text="Show Additional Features", command=toggle_features)
toggle_button.pack(pady=10)

predict_button = tk.Button(root, text="Predict Price", command=predict_price)
predict_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
