import os
import traceback

from dotenv import load_dotenv
from google import genai

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import FuturePrediction


load_dotenv()


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

Create a personalized and motivational future prediction.

User Details:

Name: {name}
Age: {age}
Goal: {goal}
Skills: {skills}


Give the prediction in exactly this format:


After 5 Years:

Write a meaningful paragraph of 3 to 4 lines.
Explain career growth, skills improvement, achievements,
and progress towards the goal.


After 10 Years:

Write a meaningful paragraph of 3 to 4 lines.
Explain professional success, experience,
leadership, financial stability and achievements.


After 15 Years:

Write a meaningful paragraph of 3 to 4 lines.
Explain becoming an expert, recognition,
impact and dream accomplishments.


Important:
- Do not write short sentences.
- Each section must be a paragraph.
- Make it realistic and inspiring.
- Personalize using the user's details.

"""


    try:

        response = client.models.generate_content(

            model="gemini-2.0-flash",

            contents=prompt

        )


        prediction_text = response.text



    except Exception as e:

        traceback.print_exc()


        prediction_text = f"""

After 5 Years:

{name} will improve skills in {skills} and move closer to becoming a successful {goal}. 
Through continuous learning and dedication, new opportunities will open and career growth will begin.


After 10 Years:

{name} will gain valuable experience and become a skilled professional in the field of {goal}. 
With strong knowledge and confidence, bigger responsibilities and achievements will come.


After 15 Years:

{name} will become an expert with years of experience and strong professional recognition. 
The journey will inspire others and create a meaningful impact through dedication and hard work.

"""



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