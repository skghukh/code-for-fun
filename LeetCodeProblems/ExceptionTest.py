provided_password = "hunter3"
correct_password = "hunter2"

if provided_password != correct_password:
  raise ValueError("Incorrect password")
"Access granted"