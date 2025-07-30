def filter_matches(matches, matches_rel_cols, filter_start_date, filter_end_date, divisions_list):
    matches_col_filtered = matches[matches_rel_cols]
    # Apply both filters using logical AND (&)
    filtered_matches = matches_col_filtered[
        (matches_col_filtered.date >= filter_start_date) & (matches_col_filtered.date <= filter_end_date) & 
        (matches_col_filtered.Division.isin(divisions_list))
    ]

    return filtered_matches

def train_test_split(filtered_matches):
    # Shuffle the data
    filtered_matches = filtered_matches.sample(frac=1).reset_index(drop=True)
    # Split the data into train and test sets
    train_size = int(len(filtered_matches) * 0.8)
    train_set = filtered_matches.iloc[:train_size]
    test_set = filtered_matches.iloc[train_size:]
    return train_set, test_set