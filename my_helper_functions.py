import os
import requests
import urllib.parse
import random

from flask import redirect, render_template, request, session
from functools import wraps

def test():
    return 1

def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"

def lpm_random():
    list = ['cat', 'dog', 'rat','bat','octopus']
    return list[random.randrange(0,5)]

print(lpm_random())