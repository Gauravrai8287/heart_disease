from flask import Flask, request, render_template
import pandas as pd
from src.heart_disease_prediction.pipelines.prediction_pipeline import PredictPipeline

app = Flask(__name__)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    try:
        if request.method == "GET":
            return render_template('index.html')

        else:
            data = {
                "age": request.form.get("age"),
                "sex": request.form.get("sex"),
                "cp": request.form.get("cp"),
                "trestbps": request.form.get("trestbps"),
                "chol": request.form.get("chol"),
                "fbs": request.form.get("fbs"),
                "restecg": request.form.get("restecg"),
                "thalachh": request.form.get("thalachh"),
                "exang": request.form.get("exang"),
                "oldpeak": request.form.get("oldpeak"),
                "slope": request.form.get("slope"),
                "ca": request.form.get("ca"),
                "thal": request.form.get("thal")
            }


            df = pd.DataFrame([data])
            print("DF:\n", df)
            print("COLUMNS:", df.columns)
            pipeline = PredictPipeline()
            prediction = pipeline.predict(df)
            
            if prediction == 1:
              result = "Heart Disease Detected ❌"
            else:
             result = "No Heart Disease ✅"
            return render_template("result.html", Result=result)

    except Exception as e:
        import traceback
        traceback.print_exc()   
        return str(e)  
    
    
if __name__ == "__main__":
    app.run(debug=True,port=5000)