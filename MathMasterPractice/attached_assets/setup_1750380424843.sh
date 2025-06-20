#!/bin/bash

# Setup script for EQAO Math Practice Test deployment

echo "Setting up EQAO Grade 9 Math Practice Test..."

# Install streamlit if not present
pip install streamlit

# Create streamlit config directory if it doesn't exist
mkdir -p .streamlit

# Ensure proper streamlit configuration
cat > .streamlit/config.toml << EOF
[server]
headless = true
address = "0.0.0.0"
port = 5000

[browser]
gatherUsageStats = false
EOF

echo "Setup complete! Run 'streamlit run app.py --server.port 5000' to start the application."