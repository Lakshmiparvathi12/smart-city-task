# Smart City Citizen Issue Reporting System

## GitHub Repository
## GitHub Repository
https://github.com/Lakshmiparvathi12/smart-city


## Problem Statement
Citizens in a smart city face infrastructure issues such as broken streetlights, potholes,
garbage overflow, and water leakage. A digital portal is required where citizens can easily
report issues and receive confirmation. To improve reliability, sensor-based validation is
used to support reported issues.

---

## Part A: Citizen Issue Reporting (MVP)

### Features
- Select City, Area, and Street
- Report an infrastructure-related issue
- Submit issue successfully
- Generate a unique Reference ID
- Send confirmation email to the citizen
- Store issue details in a database

### Technologies Used
- Python
- Flask
- SQLite
- HTML, CSS
- SMTP (Gmail)

### Email Trigger Explanation
When a citizen submits the issue form, the system generates a unique reference ID and
stores the issue details in a SQLite database. An email is automatically sent to the
citizen using SMTP with the reference ID confirming successful submission.

### Screenshots
- ### Screenshots
### Form Submission
![Form Submission](screenshots/form_submission.png)

### Confirmation Email
![Confirmation Email](screenshots/confirmation_email.png)



---

## Part B: Sensor-Based Support for Reported Issue

### Selected Issue
Broken Streetlight

### Sensor Used
Light Sensor

### Sensor-Based Approach
A light sensor is used to detect whether the streetlight is functioning at night. If the
sensor detects no light output, the issue is confirmed as valid. If light is detected,
the issue is marked as pending for further verification.

### Sensor Validation Logic (Pseudo Code)
```python
import random

def check_light_sensor():
    return random.choice([0, 1])  # 0 = Broken, 1 = Working

if check_light_sensor() == 0:
    print("Issue confirmed. Maintenance team notified.")
else:
    print("Streetlight working. Issue pending.")
