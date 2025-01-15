# ./src/python/apps/services/database.py

# This is a placeholder for database integration. Replace with real database logic.
_mock_db = {}

def get_user_by_email(email: str) -> dict:
  """Fetches a user by email."""
  return _mock_db.get(email)

def save_user(user: dict) -> None:
  """Saves a user to the database."""
  _mock_db[user["email"]] = user
