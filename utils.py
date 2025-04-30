from datetime import datetime, date
import pandas as pd
from google_auth import get_gsheet

SHEET_NAME = "mood_log"

def append_mood(mood, note):
    """
    Helper function that appends input mood to linked Google Sheet

    Args:
        mood: user selected mood from drop-down
        note [optional]: optional text note input from user 
    """
    sheet = get_gsheet(SHEET_NAME)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([now, mood, note or ""])

def get_today_moods():
    """
    Helper function to grab today's mood entries from linked Google Sheet
    """
    sheet = get_gsheet(SHEET_NAME)
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    if not df.empty:
        df["Timestamp"] = pd.to_datetime(df["Timestamp"])
        df = df[df["Timestamp"].dt.date == date.today()]
    return df