# EQAO Grade 9 Math Practice Test

An interactive web application that generates practice tests for the EQAO (Education Quality and Accountability Office) Grade 9 Mathematics Assessment.

## Features

- 54 unique multiple choice questions per test
- Interactive one-question-at-a-time format
- Immediate feedback and explanations
- Progress tracking and scoring
- Covers all Ontario Grade 9 curriculum strands
- Fresh questions generated on every restart

## Deployment Instructions

### Option 1: Direct Streamlit Deployment

1. Upload all files to your hosting platform
2. Install dependencies: `pip install streamlit`
3. Run the application: `streamlit run app.py --server.port 5000`

### Option 2: Using Setup Script

1. Upload all files to your hosting platform
2. Run the setup script: `bash setup.sh`
3. Start the application: `streamlit run app.py --server.port 5000`

### Option 3: Platform-Specific Deployment

For platforms like Heroku, Railway, or Render:

1. Upload all project files
2. Set the start command to: `streamlit run app.py --server.port $PORT`
3. Ensure the platform can access port 5000 or use the platform's assigned port

## File Structure

```
├── app.py                    # Main Streamlit application
├── question_generator.py     # Question generation logic
├── curriculum_strands.py     # Ontario curriculum mappings
├── index.html               # Optional landing page
├── setup.sh                 # Deployment setup script
├── .streamlit/
│   └── config.toml          # Streamlit configuration
└── README.md                # This file
```

## Local Development

1. Install Streamlit: `pip install streamlit`
2. Run locally: `streamlit run app.py`
3. Open browser to `http://localhost:8501`

## Curriculum Coverage

The test covers all five strands of the Ontario Grade 9 Mathematics curriculum:

- **Number Sense (B):** Powers, rational numbers, scientific notation, fractions, percentages
- **Algebra (C):** Expressions, equations, linear relations, graphing, slope
- **Data (D):** Statistics, correlation, data analysis, probability
- **Geometry & Measurement (E):** Geometric properties, area/perimeter, Pythagorean theorem
- **Financial Literacy (F):** Interest, budgeting, consumer math, taxation

Each test maintains proper strand distribution as per EQAO requirements.