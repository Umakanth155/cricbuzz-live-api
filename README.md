# 1. Unzip the folder
cd cricbuzz_live_api

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the API server
uvicorn main:app --reload

# 4. Open in browser
http://127.0.0.1:8000/live-scores
