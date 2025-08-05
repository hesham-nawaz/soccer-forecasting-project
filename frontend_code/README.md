# EPL 2025/26 Season Predictions Web App

A modern, responsive web application for displaying soccer match predictions for the English Premier League 2025/26 season. The app shows predicted outcomes, win probabilities, and Elo ratings for all 380 matches.

## Features

- **Modern UI**: Clean, responsive design similar to professional sports apps
- **Match Cards**: Individual cards for each match showing:
  - Home and away teams with Elo ratings
  - Win probabilities for home, draw, and away outcomes
  - Predicted match outcome
  - Elo difference between teams
- **Search & Filter**: Search by team name and filter matches
- **Pagination**: Navigate through all 380 matches with customizable page sizes
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Real-time Updates**: Dynamic loading with loading indicators

## Screenshots

The app displays predictions in a format similar to the screenshot you provided, with:
- Team names and Elo ratings
- Win probabilities as percentages
- Color-coded prediction boxes (green for home win, yellow for draw, red for away win)
- Predicted outcome badges
- Elo difference indicators

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd /path/to/soccer-forecasting-project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the web app**
   Open your browser and go to: `http://localhost:5000`

## Project Structure

```
soccer-forecasting-project/
├── app.py                          # Flask application
├── requirements.txt                # Python dependencies
├── README.md                      # This file
├── templates/
│   └── index.html                 # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css             # Custom CSS styles
│   └── js/
│       └── app.js                # JavaScript functionality
└── backend_code/
    └── output_data/
        └── predictions.csv        # Prediction data
```

## Data Format

The app expects a CSV file with the following columns:
- `home_team`: Home team name
- `away_team`: Away team name
- `date`: Match date (YYYY-MM-DD)
- `time`: Match time (HH:MM or TBD)
- `HomeElo`: Home team Elo rating
- `AwayElo`: Away team Elo rating
- `EloDiff`: Difference in Elo ratings
- `home_win_prob`: Probability of home win (0-1)
- `draw_prob`: Probability of draw (0-1)
- `away_win_prob`: Probability of away win (0-1)
- `predicted_outcome`: Predicted outcome (H/D/A)

## Usage

### Basic Navigation
- **Browse Matches**: Scroll through all matches or use pagination
- **Search Teams**: Use the search box to find specific teams
- **Filter Matches**: Use the filter buttons (All/Upcoming/Completed)
- **Adjust Display**: Change matches per page (15/30/50)

### Features
- **Responsive Cards**: Each match is displayed in a card format
- **Probability Display**: Win probabilities shown as percentages with color coding
- **Elo Information**: Team Elo ratings and differences displayed
- **Predicted Outcomes**: Clear badges showing predicted match results

## Technical Details

### Backend (Flask)
- **Framework**: Flask web framework
- **Data Processing**: Pandas for CSV handling
- **API Endpoints**: RESTful API for match data
- **Pagination**: Server-side pagination support

### Frontend
- **Framework**: Bootstrap 5 for responsive design
- **Icons**: Font Awesome for UI icons
- **JavaScript**: Vanilla JS for interactivity
- **Styling**: Custom CSS with modern design patterns

### Key Features
- **Async Loading**: Dynamic content loading with loading indicators
- **Search Functionality**: Real-time team search
- **Pagination**: Smooth page navigation
- **Mobile Responsive**: Optimized for all screen sizes
- **Accessibility**: Proper ARIA labels and keyboard navigation

## Customization

### Styling
- Modify `static/css/style.css` to change colors, fonts, and layout
- Update CSS variables in `:root` for theme colors
- Adjust card layouts and animations

### Functionality
- Edit `static/js/app.js` for JavaScript behavior changes
- Modify `app.py` for backend logic and API endpoints
- Update `templates/index.html` for HTML structure changes

### Data
- Replace `backend_code/output_data/predictions.csv` with your own prediction data
- Ensure the CSV follows the expected column format
- Update the data loading logic in `app.py` if needed

## Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Change port in app.py
   app.run(debug=True, host='0.0.0.0', port=5001)
   ```

2. **Missing dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Data not loading**
   - Check that `backend_code/output_data/predictions.csv` exists
   - Verify CSV format matches expected columns
   - Check file permissions

4. **Styling issues**
   - Clear browser cache
   - Check browser console for CSS errors
   - Verify static files are being served correctly

## Development

### Adding New Features
1. **Backend**: Add new routes in `app.py`
2. **Frontend**: Update HTML template and JavaScript
3. **Styling**: Add CSS rules to `style.css`
4. **Testing**: Test on different devices and browsers

### Performance Optimization
- The app uses server-side pagination for large datasets
- Static assets are served efficiently
- JavaScript is optimized for smooth interactions
- CSS uses modern techniques for fast rendering

## License

This project is for educational and personal use. Feel free to modify and extend as needed.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify all dependencies are installed
3. Ensure the data file exists and is properly formatted
4. Check browser console for JavaScript errors









