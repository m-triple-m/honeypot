from db import count_attempts
from config import SUSPICIOUS_THRESHOLD

def is_suspicious(ip):
    attempts = count_attempts(ip)
    return attempts >= SUSPICIOUS_THRESHOLD
