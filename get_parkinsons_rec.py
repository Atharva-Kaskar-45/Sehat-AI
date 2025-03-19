from groq import Groq
import re  
import json
import os
from dotenv import load_dotenv
load_dotenv()

class SehatAIParkinsonsReport:
    def __init__(self, language="English", patient_name="", **kwargs):
        self.language = language
        self.patient_name = patient_name
        self.parameters = kwargs
        self.api_key =  os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=self.api_key)
    
    def get_parkinsons_risk_level(self):
        """Determine Parkinson's risk level based on provided parameters."""
        if self.parameters.get("spread1", 0) > -4 or self.parameters.get("DFA", 0) > 0.7:
            return "High"
        elif self.parameters.get("spread1", 0) > -6 or self.parameters.get("DFA", 0) > 0.6:
            return "Moderate"
        else:
            return "Low"
    
    def get_groq_recommendations(self):
        """Fetch AI-generated health recommendations based on the patient's data."""
        try:
            prompt = f"""
            As a medical AI, provide Parkinson's disease management advice in {self.language} for:
            
            - Name: {self.patient_name}
            - Parkinson's Risk Level: {self.get_parkinsons_risk_level()}
            
            Provided metrics:
            {json.dumps(self.parameters, indent=2)}
            
            Include:
            1. Early warning signs and symptoms of Parkinson's disease
            2. Lifestyle modifications to slow progression
            3. Dietary recommendations to support neurological health
            4. Recommended physical activities for maintaining motor functions
            5. Medication and treatment options based on risk level
            6. When to seek medical attention
            """

            response = self.client.chat.completions.create(
                model="qwen-qwq-32b",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.6,
                max_completion_tokens=2048,
                top_p=0.95,
            )
            recommendations = response.choices[0].message.content
            return re.sub(r"\bThink\b.*", "", recommendations, flags=re.DOTALL).strip()
        except Exception as e:
            return f"Error fetching recommendations: {str(e)}"
    
    def generate_report(self):
        """Generate a structured Parkinson's disease report with AI recommendations."""
        risk_level = self.get_parkinsons_risk_level()
        recommendations = self.get_groq_recommendations()
        
        report = f"""
        # Sehat AI Parkinson's Disease Report
        
        ## Patient Information
        **Name:** {self.patient_name}  
        **Language:** {self.language}  
        
        ## Health Metrics
        {json.dumps(self.parameters, indent=2)}
        
        ## Parkinson's Risk Level
        **{risk_level}**
        
        ## AI Recommendations
        {recommendations}
        """
        return report