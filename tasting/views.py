from django.shortcuts import render
from django.http import JsonResponse
from decouple import config
import openai

# Load OpenAI API key
openai.api_key = config("OPENAI_API_KEY")

def generate_tasting_note(request):
    if request.method == "POST":
        wine_input = request.POST.get("wine_characteristics", "")

        if wine_input.strip():  # Ensure input is not empty
            try:
                # Correct method for OpenAI >=1.0.0
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",  # Use the correct model
                    messages=[
                        {"role": "system", "content": "You are a professional wine-tasting note generator."},
                        {"role": "user", "content": f"Write a professional wine-tasting note based on these characteristics: {wine_input}"}
                    ],
                    max_tokens=150
                )

                # Extract the AI-generated content
                tasting_note = response.choices[0].message.content.strip()
                return JsonResponse({"tasting_note": tasting_note})
            except Exception as e:
                print(f"Error: {e}")
                return JsonResponse({"error": "Failed to generate tasting note. Please try again later."}, status=500)
        else:
            return JsonResponse({"error": "Input cannot be empty."}, status=400)

    return render(request, "tasting/form.html")
