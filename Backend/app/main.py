import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# ✅ Keep your existing internal import
from app.services.humanizer import humanize_text

app = FastAPI(
    title="Authentify API",
    description="Human-Centric AI Text Refinement System",
    version="2.0"
)

# --- CORS Setup (Updated for Deployment) ---
# We include localhost for testing and "*" to ensure Vercel can connect 
# You can replace "*" with your specific Vercel URL later for tighter security
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "*", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Request Model ---
class TextRequest(BaseModel):
    text: str
    tone: str = "human"


# --- Routes ---
@app.get("/")
def root():
    # Helpful for debugging on Hugging Face to see if the API is actually up
    return {
        "message": "Authentify API is running on Hugging Face",
        "status": "online",
        "mode": "production"
    }


@app.post("/refine")
def refine(request: TextRequest):
    """
    Refines text using fully local humanization pipeline on Hugging Face hardware.
    """
    # Trigger your humanizer logic
    results = humanize_text(request.text, request.tone)

    # Return the fields exactly as your Frontend expects them
    return {
        "original_text": results.get("original_text"),
        "refined_text": results.get("humanized_text"),
        "local_ai_score": results.get("local_ai_score"),
        "initial_ai_score": results.get("initial_ai_score")  
    }

# --- Hugging Face Startup ---
# Note: Hugging Face automatically handles the port 7860 mapping, 
# but having this block ensures it runs correctly if executed as a script.
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 7860))
    uvicorn.run(app, host="0.0.0.0", port=port)