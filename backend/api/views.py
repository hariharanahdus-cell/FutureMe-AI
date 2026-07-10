import os

from dotenv import load_dotenv
from google import genai

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import FuturePrediction


# Load .env file
load_dotenv()


# Create Gemini Client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


@api_view(["POST"])
def future_prediction(request):

    name = request.data.get("name")
    age = request.data.get("age")
    goal = request.data.get("goal")
    skills = request.data.get("skills")

    prompt = f"""
You are FutureMe AI.

Create a realistic and motivating future prediction.

Name: {name}
Age: {age}
Goal: {goal}
Skills: {skills}

Generate:

1. After 5 Years
2. After 10 Years
3. After 15 Years

Keep the prediction realistic, inspiring, and around 200 words.
"""

    try:

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        prediction_text = response.text

        # Save into MySQL
        FuturePrediction.objects.create(
            name=name,
            age=age,
            goal=goal,
            skills=skills,
            prediction=prediction_text
        )

        return Response({
            "message": f"Hello {name} 👋",
            "future": prediction_text
        })

    except Exception as e:

        import traceback
        traceback.print_exc()

        error_message = str(e)

        # Handle Gemini quota errors
        if "RESOURCE_EXHAUSTED" in error_message or "429" in error_message:
            return Response({
                "message": "Gemini quota exceeded",
                "future": "The Gemini free API quota has been reached. Please wait until the quota resets or use another API key."
            }, status=429)

        return Response({
            "message": "Error",
            "future": error_message
        }, status=500)