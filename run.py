from app import app
from db import db
db.init_app(app)
if __name__ == "__main__":
	app.run(port=5002, debug=True)

@app.before_first_request
def create_tables():
	db.create_all()
