import os

from dotenv import load_dotenv
from google import genai

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import FuturePrediction


# Load environment variables
load_dotenv()


# Gemini Client
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

        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )

        except Exception:
            response = client.models.generate_content(
                model="gemini-2.0-flash-lite",
                contents=prompt
            )


        prediction_text = response.text


    except Exception:

        # Backup prediction if Gemini fails
        prediction_text = f"""
After 5 Years:
{name} will continue improving skills in {skills} and move closer to the goal of {goal}.

After 10 Years:
{name} will gain professional experience and achieve important milestones.

After 15 Years:
{name} will become successful through dedication, learning, and consistency.
"""


    # Save prediction
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