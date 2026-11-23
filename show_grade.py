"""Display your Homework 2 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "ec0bbfd8b2909baa7eec13ee385450b1"
GRADE_HASH = "594963831936e739c84c59ff304a32584dbf8c27e4196db7df70e716b0706976"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 2: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
