from flask import Flask, request, render_template
import joblib

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    model=joblib.load("./static/House.joblib")
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    living_area = int(request.form['livingArea'])
    lot_area = int(request.form['lotArea'])
    num_floors = int(request.form['floors'])
    num_views = int(request.form['views'])
    grade = int(request.form['grade'])
    house_area = int(request.form['area_w/o_base'])
    basement_area = int(request.form['area_base'])
    built_year = int(request.form['builtYear'])
    renovation_year = int(request.form['ren_year'])
    postal_code = int(request.form['postalCode'])
    latitude = float(request.form['latitude'])
    longitude = float(request.form['longitude'])
    living_area_renov = int(request.form['liv_area_ren'])
    lot_area_renov = int(request.form['lot_area_ren'])

    features = [[bedrooms, bathrooms, living_area, lot_area, num_floors, num_views, grade,
                    house_area, basement_area, built_year, renovation_year, postal_code, latitude, longitude,
                    living_area_renov, lot_area_renov]]
    predicted_price = model.predict(features)

    return render_template('index.html', prediction_text=f'The predicted price is Rs. {round(predicted_price[0],3)} Lakhs',bedrooms=bedrooms,bathrooms=bathrooms,living_area=living_area,latitude=latitude,longitude=longitude,postal_code=postal_code,built_year=built_year)

if __name__ == "__main__":
    app.run(debug=True)
