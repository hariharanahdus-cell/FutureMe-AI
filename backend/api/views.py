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
You are FutureMe AI, an expert career and life prediction assistant.

Create an inspiring but realistic future journey for this person.

Personal Details:

Name: {name}
Current Age: {age}
Career Goal: {goal}
Current Skills: {skills}


Generate a detailed future roadmap:

## After 5 Years:
- Career position
- Skills developed
- Professional achievements
- Personal growth


## After 10 Years:
- Major career milestones
- Leadership opportunities
- Financial and professional growth
- Contributions to society
- Advanced skills and expertise


## After 15 Years:
- Peak career achievements
- Recognition and impact
- Expertise level
- Life achievements
- How this person inspires others


Make it personalized, motivational, realistic, and emotional.
Avoid generic statements.
Write around 400-500 words.
"""


    try:

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        prediction_text = response.text


    except Exception as e:

        print("Gemini Error:", e)

        prediction_text = f"""
🌟 After 5 Years:

{name} will be progressing strongly toward the goal of {goal}.
With skills in {skills}, continuous learning will help build a successful career.


🚀 After 10 Years:

{name} will become an experienced professional with strong expertise.
Years of dedication will create opportunities for leadership, innovation,
and meaningful achievements.


🏆 After 15 Years:

{name} will reach an advanced stage of career growth.
With experience and knowledge, {name} will become a respected person who
creates impact and guides future generations.
"""


    try:

        FuturePrediction.objects.create(
            name=name,
            age=age,
            goal=goal,
            skills=skills,
            prediction=prediction_text
        )

    except Exception as e:
        print("Database Error:", e)


    return Response({
        "message": f"Hello {name} 👋",
        "future": prediction_text
    })