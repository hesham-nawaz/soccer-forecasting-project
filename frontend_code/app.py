from flask import Flask, render_template, request, jsonify
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

# Load predictions data
def load_predictions():
    predictions_path = '../backend_code/output_data/predictions.csv'
    if os.path.exists(predictions_path):
        df = pd.read_csv(predictions_path)
        # Convert date column to datetime
        df['date'] = pd.to_datetime(df['date'])
        return df
    return pd.DataFrame()

@app.route('/')
def index():
    predictions_df = load_predictions()
    
    if predictions_df.empty:
        return render_template('index.html', matches=[], total_matches=0)
    
    # Sort by date
    predictions_df = predictions_df.sort_values('date')
    
    # Convert to list of dictionaries for template
    matches = []
    for _, row in predictions_df.iterrows():
        match = {
            'home_team': row['home_team'],
            'away_team': row['away_team'],
            'date': row['date'].strftime('%Y-%m-%d'),
            'time': row['time'] if pd.notna(row['time']) else 'TBD',
            'home_win_prob': round(row['home_win_prob'] * 100, 1),
            'draw_prob': round(row['draw_prob'] * 100, 1),
            'away_win_prob': round(row['away_win_prob'] * 100, 1),
            'predicted_outcome': row['predicted_outcome'],
            'home_elo': round(row['HomeElo'], 1),
            'away_elo': round(row['AwayElo'], 1),
            'elo_diff': round(row['EloDiff'], 1)
        }
        matches.append(match)
    
    return render_template('index.html', matches=matches, total_matches=len(matches))

@app.route('/api/matches')
def api_matches():
    predictions_df = load_predictions()
    
    if predictions_df.empty:
        return jsonify({'matches': []})
    
    # Get query parameters
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 15, type=int)
    team_filter = request.args.get('team', '').strip()
    
    # Apply team filter if provided
    if team_filter:
        mask = (predictions_df['home_team'].str.contains(team_filter, case=False) | 
                predictions_df['away_team'].str.contains(team_filter, case=False))
        predictions_df = predictions_df[mask]
    
    # Sort by date
    predictions_df = predictions_df.sort_values('date')
    
    # Pagination
    total_matches = len(predictions_df)
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    page_matches = predictions_df.iloc[start_idx:end_idx]
    
    matches = []
    for _, row in page_matches.iterrows():
        match = {
            'home_team': row['home_team'],
            'away_team': row['away_team'],
            'date': row['date'].strftime('%Y-%m-%d'),
            'time': row['time'] if pd.notna(row['time']) else 'TBD',
            'home_win_prob': round(row['home_win_prob'] * 100, 1),
            'draw_prob': round(row['draw_prob'] * 100, 1),
            'away_win_prob': round(row['away_win_prob'] * 100, 1),
            'predicted_outcome': row['predicted_outcome'],
            'home_elo': round(row['HomeElo'], 1),
            'away_elo': round(row['AwayElo'], 1),
            'elo_diff': round(row['EloDiff'], 1)
        }
        matches.append(match)
    
    return jsonify({
        'matches': matches,
        'total_matches': total_matches,
        'current_page': page,
        'total_pages': (total_matches + per_page - 1) // per_page
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) 