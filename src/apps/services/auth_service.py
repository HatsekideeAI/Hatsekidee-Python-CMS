# ./src/python/apps/services/auth_service.py

import os
from datetime import datetime, timedelta
import bcrypt
import jwt

from .database import get_user_by_email, save_user

# Secret key for JWT (load from environment in production)
SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key")
if SECRET_KEY == "fallback-secret-key":
  raise ValueError("SECRET_KEY is niet ingesteld! Controleer je .env bestand.")


class AuthService:
  """Service voor authenticatie en gebruikersbeheer."""

  @staticmethod
  def hash_password(password: str) -> str:
    """Hashes a password using bcrypt."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

  @staticmethod
  def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a password using bcrypt."""
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())

  @staticmethod
  def generate_token(email: str, expiration_hours: int = 1) -> str:
    """Generates a JWT token with a default expiration of 1 hour."""
    expiration = datetime.utcnow() + timedelta(hours=expiration_hours)
    payload = {"email": email, "exp": expiration}
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

  @staticmethod
  def verify_token(token: str) -> dict:
    """Verifies and decodes a JWT token."""
    try:
      return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
      return {"error": "Token has expired"}
    except jwt.InvalidTokenError:
      return {"error": "Invalid token"}

  @staticmethod
  def user_exists(email: str) -> bool:
    """Checks if a user with the given email already exists."""
    return bool(get_user_by_email(email))

  def login(self, email: str, password: str) -> dict:
    """Authenticates a user and returns a token."""
    user = get_user_by_email(email)
    if not user or not self.verify_password(password, user["password"]):
      return {"error": "Invalid email or password"}
    return {"token": self.generate_token(email)}

  def register(self, email: str, password: str) -> dict:
    """Registers a new user."""
    if self.user_exists(email):
      return {"error": "Email already registered"}
    hashed_password = self.hash_password(password)
    save_user({"email": email, "password": hashed_password})
    return {"success": "User registered successfully"}

  def reset_password(self, email: str, new_password: str) -> dict:
    """Resets the user's password."""
    user = get_user_by_email(email)
    if not user:
      return {"error": "User not found"}
    user["password"] = self.hash_password(new_password)
    save_user(user)
    return {"success": "Password reset successfully"}
