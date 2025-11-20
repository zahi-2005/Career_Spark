import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "AIzaSyBbmJ9-n5LH1Iq4AgNxWN_PXrmjpVvqVL4")
GOOGLE_SEARCH_API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY", "AIzaSyBbmJ9-n5LH1Iq4AgNxWN_PXrmjpVvqVL4")
GOOGLE_SEARCH_CX_ID = os.getenv("GOOGLE_SEARCH_CX_ID", "AIzaSyBbmJ9-n5LH1Iq4AgNxWN_PXrmjpVvqVL4")

print("Google GenAI API Key from config:", GOOGLE_API_KEY)
print("Google Search API Key from config:", GOOGLE_SEARCH_API_KEY)
print("Google Search CX ID from config:", GOOGLE_SEARCH_CX_ID)
