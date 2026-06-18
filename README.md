# D2C Customer Churn Intelligence - Part 4
## Objective
Deploy the churn prediction model as a FastAPI service for internal CRM usage.

## API Endpoints
### Health Check
GET /health

### Single Prediction
POST /predict
Returns:
* churn_probability
* prediction
* risk_reason

### Batch Prediction
POST /batch_predict
Returns predictions for multiple customers.

## Run
Install dependencies:
pip install -r requirements.txt
Start server:
uvicorn app.main:app --reload
Open:
http://127.0.0.1:8000/docs

## Testing
Run:
pytest

## Responsible Use
Predictions should assist retention teams and not be used as the sole basis for customer decisions.
