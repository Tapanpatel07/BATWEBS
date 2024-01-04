from django.shortcuts import render

# Create your views here.
import os
from django.shortcuts import render
from google.generativeai import GenerativeModel
from dotenv import load_dotenv


load_dotenv()

model =os.getenv("GEMINI_API_KEY")

def chat_view(request):
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        response = model.generate_text(
            prompt=user_input,
            max_tokens=150,
            temperature=0.7  
        )
        context = {"user_input": user_input, "response": response.text}
        return render(request, "chatbot/chat.html", context)
    else:
        return render(request, "chatbot/chat.html")