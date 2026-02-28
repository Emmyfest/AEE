from app import app, create_tables, seed_database
    create_tables()
    seed_database()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

