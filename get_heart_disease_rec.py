from groq import Groq
import json
import os
from dotenv import load_dotenv
import re  
load_dotenv()
class SehatAIHeartDiseaseReport:
    def __init__(self, language="English", patient_name="", age=0, sex="", chest_pain_type=0, 
                 resting_bp=0, fasting_blood_sugar=0, rest_ecg=0, max_heart_rate=0, 
                 exercise_angina=0, cholesterol=0, st_depression=0, st_slope=0, 
                 major_vessels=0, thal=0):
        self.language = language
        self.patient_name = patient_name
        self.age = age
        self.sex = sex
        self.chest_pain_type = chest_pain_type
        self.resting_bp = resting_bp
        self.fasting_blood_sugar = fasting_blood_sugar
        self.rest_ecg = rest_ecg
        self.max_heart_rate = max_heart_rate
        self.exercise_angina = exercise_angina
        self.cholesterol = cholesterol
        self.st_depression = st_depression
        self.st_slope = st_slope
        self.major_vessels = major_vessels
        self.thal = thal
        self.api_key = os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=self.api_key)
    
    def get_heart_disease_risk_level(self):
        """Determine risk level based on key heart health indicators."""
        if self.cholesterol > 240 or self.resting_bp > 140 or self.max_heart_rate < 100:
            return "High"
        elif self.cholesterol > 200 or self.resting_bp > 120:
            return "Moderate"
        else:
            return "Low"
    
    def get_groq_recommendations(self):
        """Fetch AI-generated heart health recommendations based on the patient's data."""
        try:
            prompt = f"""
            As a medical AI, provide heart disease management advice in {self.language} for:
            
            - Name: {self.patient_name}
            - Age: {self.age}
            - Sex: {self.sex}
            - Chest Pain Type: {self.chest_pain_type}
            - Resting Blood Pressure: {self.resting_bp} mmHg
            - Fasting Blood Sugar > 120 mg/dL: {self.fasting_blood_sugar}
            - Resting ECG Results: {self.rest_ecg}
            - Maximum Heart Rate Achieved: {self.max_heart_rate}
            - Exercise Induced Angina: {self.exercise_angina}
            - Serum Cholesterol: {self.cholesterol} mg/dL
            - ST Depression (Exercise-Induced): {self.st_depression}
            - Slope of Peak Exercise ST Segment: {self.st_slope}
            - Major Vessels Colored by Fluoroscopy: {self.major_vessels}
            - Thalassemia Type: {self.thal}
            - Heart Disease Risk Level: {self.get_heart_disease_risk_level()}
            
            Include:
            1. Lifestyle changes for heart disease prevention and control
            2. Dietary recommendations for heart health
            3. Exercise plans suitable for age and risk level
            4. Medication guidance if necessary
            5. Any warning signs requiring medical attention
            """

            response = self.client.chat.completions.create(
                model="qwen-qwq-32b",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.6,
                max_completion_tokens=2048,
                top_p=0.95,
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error fetching recommendations: {str(e)}"
    
    def generate_report(self):
        """Generate a structured heart disease report with AI recommendations."""
        risk_level = self.get_heart_disease_risk_level()
        recommendations = self.get_groq_recommendations()
        
        # Remove "Think" section from recommendations
        recommendations = re.sub(r"\bThink\b.*", "", recommendations, flags=re.DOTALL).strip()

        report = f"""
        # Sehat AI Heart Disease Report
        
        ## Patient Information
        **Name:** {self.patient_name}  
        **Age:** {self.age}  
        **Sex:** {self.sex}  
        
        ## Health Metrics
        - **Chest Pain Type:** {self.chest_pain_type}
        - **Resting Blood Pressure:** {self.resting_bp} mmHg
        - **Fasting Blood Sugar > 120 mg/dL:** {self.fasting_blood_sugar}
        - **Resting ECG Results:** {self.rest_ecg}
        - **Maximum Heart Rate Achieved:** {self.max_heart_rate}
        - **Exercise Induced Angina:** {self.exercise_angina}
        - **Serum Cholesterol:** {self.cholesterol} mg/dL
        - **ST Depression (Exercise-Induced):** {self.st_depression}
        - **Slope of Peak Exercise ST Segment:** {self.st_slope}
        - **Major Vessels Colored by Fluoroscopy:** {self.major_vessels}
        - **Thalassemia Type:** {self.thal}
        
        ## Heart Disease Risk Level
        **{risk_level}**
        
        ## AI Recommendations
        {recommendations}
        """

        return report
