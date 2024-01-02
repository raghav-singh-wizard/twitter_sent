from fastapi import FastAPI, HTTPException, Query
from transformers import BertForSequenceClassification, BertTokenizer
from pydantic import BaseModel
import torch

app = FastAPI()

# Load the pre-trained model and tokenizer
model_path = "twitterSentiment"  
tokenizer_path = "twitterSentiment"  
model = BertForSequenceClassification.from_pretrained(model_path)
tokenizer = BertTokenizer.from_pretrained(tokenizer_path)

emotion_dict = { 0: "I can't tell",
                1: "Negative emotion",
                2 : 'No emotion toward brand or product',
                3: "Positive emotion",
               }

# Create a Pydantic model for the input
class SentimentRequest(BaseModel):
    text: str = Query(..., description="Text for sentiment analysis")

# Create a route to handle sentiment analysis
@app.post("/predict_sentiment")
async def predict_sentiment(request: SentimentRequest):
    try:
        # Tokenize the input text
        tokens = tokenizer.encode_plus(
            request.text,
            add_special_tokens=True,
            max_length=128,
            padding='max_length',
            return_attention_mask=True,
            return_tensors='pt',
        )

        # Perform inference
        with torch.no_grad():
            outputs = model(**tokens)

        # Get the predicted sentiment
        logits = outputs.logits
        predicted_class = torch.argmax(logits).item()

        return {"sentiment": emotion_dict[predicted_class], "confidence": torch.softmax(logits, dim=1).tolist()[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
