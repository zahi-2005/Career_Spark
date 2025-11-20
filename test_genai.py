from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="What skills are needed for a data analyst?",
    config=genai.types.GenerateContentConfig(
        temperature=0.5,
        candidate_count=1,
        max_output_tokens=500,
    ),
)

print(response.text)

