# Authentify

Authentify is an AI-powered text humanizer that rewrites text to make it sound more natural while attempting to preserve its original meaning. It combines transformer-based paraphrasing, AI-text detection, semantic similarity checking, and rule-based text transformations.

## Tech Stack

- **Frontend:** React
- **Backend:** FastAPI
- **ML/NLP:** PyTorch, Hugging Face Transformers, spaCy, Sentence Transformers

## How It Works

1. **AI Detection:** A RoBERTa-based sequence classification model estimates the AI-generated probability of the input text.
2. **Text Chunking:** spaCy splits long text into manageable chunks at sentence boundaries.
3. **Neural Paraphrasing:** A pretrained T5 model (`humarin/chatgpt_paraphraser_on_T5_base`) generates rewritten text.
4. **Rule-Based Rewriting:** Python functions replace selected phrases, attempt passive-voice variations, and apply contractions.
5. **Semantic Check:** `all-MiniLM-L6-v2` generates embeddings for the original and rewritten text. Cosine similarity determines whether to accept the rewrite or fall back to the original.
6. **Final Evaluation:** The RoBERTa detector evaluates the resulting text again.

## Key Models

| Model | Purpose |
|---|---|
| `humarin/chatgpt_paraphraser_on_T5_base` | Text paraphrasing |
| `Hello-SimpleAI/chatgpt-detector-roberta` | AI-text classification |
| `all-MiniLM-L6-v2` | Semantic similarity checking |

The separate `ai_detector.py` file uses `roberta-base-openai-detector`, which is different from the detector used in the main humanization pipeline.

## Output

The backend's `humanize_text()` function returns:

- `original_text`: Original input
- `humanized_text`: Final rewritten text
- `initial_ai_score`: Initial detector score
- `local_ai_score`: Final detector score
- `chunks_processed`: Number of chunks processed

**Note:** Detector scores are estimates, not proof of authorship. Semantic similarity helps reduce meaning changes but cannot guarantee that the original meaning is preserved.

## Project Structure

```text
Authentify/
├── Backend/
│   └── app/
│       └── services/
│           ├── ai_detector.py
│           ├── humanizer.py
│           └── style_rules.py
└── Frontend/
    └── React application
```

*The structure above is a simplified overview.*
