# Monitoring Plan
## Objective
Monitor model performance and business outcomes after deployment.

## Metrics to Track
### Data Drift
Monitor changes in:
* recency_days
* frequency_180d
* monetary_180d
* sessions_30d

### Prediction Distribution
Track:
* percentage predicted as churn
* average churn probability

### API Monitoring
Track:
* response time
* failed requests
* server errors

### Business Metrics
Track:
* retention campaign success rate
* customer retention rate
* churn reduction percentage

### Retraining Triggers
Retraining should be considered when:
* Prediction distributions change significantly.
* Data drift exceeds acceptable thresholds.
* Business KPIs decline.
* Model performance deteriorates.
