import requests
import pandas as pd
from datetime import date
from io import StringIO
from urllib.parse import quote_plus

BASE_URL = "http://api.clubelo.com"

def get_daily_ranking(target_date: date):
    """
    Fetch the full Elo ranking for a single day.
    
    Parameters:
    -----------
    target_date : date
        A datetime.date object (e.g. date(2024, 8, 15))
        
    Returns:
    --------
    pandas.DataFrame
        DataFrame with columns: 'Rank', 'Club', 'Country', 'Level', 'Elo', 'From', 'To'
    """
    url = f"{BASE_URL}/{target_date.isoformat()}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/csv, application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
    }
    
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        
        # Parse CSV response
        df = pd.read_csv(StringIO(resp.text))
        return df
        
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None
    except Exception as e:
        print(f"Error parsing CSV: {e}")
        return None

def get_club_history(club_name: str):
    """
    Fetch the Elo history for one club.
    
    Parameters:
    -----------
    club_name : str
        Exact club name as in the ranking (e.g. "Liverpool")
        
    Returns:
    --------
    pandas.DataFrame
        DataFrame with columns: 'Rank', 'Club', 'Country', 'Level', 'Elo', 'From', 'To'
    """
    # URL‐encode club name (handles spaces, punctuation, etc.)
    safe_name = quote_plus(club_name)
    url = f"{BASE_URL}/{safe_name}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/csv, application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
    }
    
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        
        # Parse CSV response
        df = pd.read_csv(StringIO(resp.text))
        return df
        
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None
    except Exception as e:
        print(f"Error parsing CSV: {e}")
        return None

if __name__ == "__main__":
    # Example: get the ranking for August 15, 2024
    print("=== Club Elo API Test ===")
    
    # Test daily ranking
    print("\n1. Testing daily ranking...")
    ranking_df = get_daily_ranking(date(2024, 8, 15))
    
    if ranking_df is not None:
        print(f"Top 5 clubs on 2024-08-15:")
        print(ranking_df.head().to_string(index=False))
        print(f"\nTotal clubs in ranking: {len(ranking_df)}")
    else:
        print("Failed to get daily ranking")

    # Test club history
    print("\n2. Testing club history...")
    history_df = get_club_history("Liverpool")
    
    if history_df is not None:
        print("Liverpool Elo history (first 5 entries):")
        print(history_df.head().to_string(index=False))
        print(f"\nTotal history entries: {len(history_df)}")
        
        # Show recent history
        print("\nLiverpool recent Elo (last 5 entries):")
        print(history_df.tail().to_string(index=False))
    else:
        print("Failed to get club history")
    
    # Test with a different club
    print("\n3. Testing with Arsenal...")
    arsenal_df = get_club_history("Arsenal")
    
    if arsenal_df is not None:
        print("Arsenal recent Elo (last 5 entries):")
        print(arsenal_df.tail().to_string(index=False))
    else:
        print("Failed to get Arsenal history") 