from flask import Flask,render_template

app = Flask(__name__)

PROJECTS = [
    {
        "title":'Heart Disease Risk Prediction With AI health Advice',
        "About":'In this project, I developed a Heart Disease Risk Prediction system using advanced AI techniques. By analyzing key health indicators such as age, blood pressure, cholesterol, and more, the system predicts the likelihood of a patient developing heart disease. I utilized Regression models with the help of Scikit-learn, Pandas for data preprocessing, and GenAI to provide personalized health advice. The model not only offers a prediction but also provides actionable health recommendations tailored to the individuals risk factors, empowering users to take proactive steps toward improving their heart health.',
        "Link":'link'
    },
    {
        "title":'New Delhi LIVE data House Price prediction with property Recommendation',
        "About":'In this project, I built a House Price Prediction model using LIVE data from popular housing platforms. I used BeautifulSoup to scrape real-time property listings and gather crucial features like location, area, and amenities. The data was processed using Pandas, and an Artificial Neural Network (ANN) was employed to predict house prices based on these features. Additionally, I developed a recommendation system that suggests properties based on user-provided preferences, providing links to the most relevant listings. This project integrates machine learning with real-time data to assist users in finding the best property deals in New Delhi.',
        "Link":'link'
    },
    {
        "title":'AI powered SQL query Chatbot',
        "About":"In this project, I developed an AI-powered SQL Query Chatbot that allows users to interact with their MySQL or SQL Server databases through a conversational interface. By inputting their database credentials, users can simply ask questions about their data in natural language, and the chatbot automatically generates and executes the corresponding SQL queries. This chatbot streamlines the process of querying databases, making it easier for both technical and non-technical users to retrieve insights without needing to write SQL code manually.",
        "Link":'link'
    },
    {
        "title":'Skin Cancer Detection',
        "About":"The skin cancer detection project aims to classify skin lesions as either malignant or benign based on images of the skin. Using deep learning techniques, particularly convolutional neural networks (CNNs), the model is trained on a large dataset of labeled images of skin lesions. The primary goal is to assist healthcare professionals by providing an automated system for detecting cancerous growths early, leading to timely intervention. The project involves preprocessing the images, applying data augmentation to increase model robustness, and using classification algorithms to distinguish between malignant (cancerous) and benign (non-cancerous) lesions. Accuracy, sensitivity, and specificity are key metrics used to evaluate the model’s performance in real-world settings.",
        "Link":'link'
    }

]
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/projects")
def projects():
    return render_template('projects.html',jobs=PROJECTS)

if __name__ == '__main__':
    app.run(debug=True)