from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import joblib
import pandas as pd
app = FastAPI(
    title="Customer Churn API"
)
model = joblib.load("model.pkl")
class CustomerFeatures(BaseModel):
    recency_days:int
    frequency_180d:int
    monetary_180d:float
    return_rate_180d:float
    avg_discount_pct_180d:float
    avg_rating_180d:float
    category_diversity_180d:int
    ticket_count_90d:int
    negative_ticket_rate_90d:float
    avg_resolution_hours_90d:float
    days_since_signup:int
    sessions_30d:int
    product_views_30d:int
    cart_adds_30d:int
    wishlist_adds_30d:int
    abandoned_carts_30d:int
    email_opens_30d:int
    campaign_clicks_30d:int
    last_visit_days_ago:int
@app.get("/health")
def health():
    return {
        "status":"healthy"
    }

@app.post("/predict")
def predict(customer:CustomerFeatures):
    df = pd.DataFrame([customer.dict()])
    probability = float(
        model.predict_proba(df)[0][1]
    )
    prediction = int(
        probability > 0.5
    )
    if probability > 0.7:
        reason = "High churn risk"

    elif probability > 0.4:
        reason = "Moderate churn risk"
    else:
        reason = "Low churn risk"
    return {
        "churn_probability":probability,
        "prediction":prediction,
        "risk_reason":reason
    }
@app.post("/batch_predict")
def batch_predict(
    customers:List[CustomerFeatures]
):
    df = pd.DataFrame(
        [c.dict() for c in customers]
    )
    probabilities = model.predict_proba(df)[:,1]

    results = []

    for prob in probabilities:
        results.append({
            "churn_probability":float(prob),
            "prediction":int(prob > 0.5)
        })
    return results
