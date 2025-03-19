from groq import Groq
import json
from dotenv import load_dotenv
import os
import re  
load_dotenv()
class SehatAIDiabetesReport:
    def __init__(self, language="English", patient_name="", age=0, gender="", glucose=0, blood_pressure=0, bmi=0, insulin=0):
        self.language = language
        self.patient_name = patient_name
        self.age = age
        self.gender = gender
        self.glucose = glucose
        self.blood_pressure = blood_pressure
        self.bmi = bmi
        self.insulin = insulin
        self.api_key = os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=self.api_key)
    
    def get_diabetes_risk_level(self):
        """Determine risk level based on glucose, BMI, and insulin levels."""
        if self.glucose > 140 or self.bmi > 30 or self.insulin > 200:
            return "High"
        elif self.glucose > 100 or self.bmi > 25 or self.insulin > 150:
            return "Moderate"
        else:
            return "Low"
    
    def get_groq_recommendations(self):
        """Fetch AI-generated health recommendations based on the patient's data."""
        try:
            prompt = f"""
            As a medical AI, provide diabetes management advice in {self.language} for:
            
            - Name: {self.patient_name}
            - Age: {self.age}
            - Gender: {self.gender}
            - Glucose Level: {self.glucose} mg/dL
            - Blood Pressure: {self.blood_pressure} mmHg
            - BMI: {self.bmi}
            - Insulin Level: {self.insulin} pmol/L
            - Diabetes Risk Level: {self.get_diabetes_risk_level()}
            
            Include:
            1. Lifestyle changes for diabetes prevention and control
            2. Dietary recommendations based on glucose levels
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
        """Generate a structured diabetes report with AI recommendations."""
        risk_level = self.get_diabetes_risk_level()
        recommendations = self.get_groq_recommendations()
        
        # Remove "Think" section from recommendations
        recommendations = re.sub(r"\bThink\b.*", "", recommendations, flags=re.DOTALL).strip()

        report = f"""
        # Sehat AI Diabetes Report
        
        ## Patient Information
        **Name:** {self.patient_name}  
        **Age:** {self.age}  
        **Gender:** {self.gender}  
        
        ## Health Metrics
        - **Glucose Level:** {self.glucose} mg/dL
        - **Blood Pressure:** {self.blood_pressure} mmHg
        - **BMI:** {self.bmi}
        - **Insulin Level:** {self.insulin} pmol/L
        
        ## Diabetes Risk Level
        **{risk_level}**
        
        ## AI Recommendations
        {recommendations}
        """

        return report

        

