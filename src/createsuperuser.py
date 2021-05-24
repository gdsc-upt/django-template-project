from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

USERNAME = "admin"
EMAIL = "admin@example.com"
PASSWORD = "admin"

try:
    get_user_model().objects.create_superuser(USERNAME, EMAIL, PASSWORD)
except IntegrityError:
    print(f"User '{USERNAME} <{EMAIL}>' already exists")
else:
    print(f"Created superuser '{USERNAME} <{EMAIL}>' with password '{PASSWORD}'")
