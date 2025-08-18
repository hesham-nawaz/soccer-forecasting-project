from sklearn.model_selection import train_test_split

def filter_matches(matches, matches_rel_cols, filter_start_date, filter_end_date, divisions_list):
    matches_col_filtered = matches[matches_rel_cols]
    # Apply both filters using logical AND (&)
    filtered_matches = matches_col_filtered[
        (matches_col_filtered.date >= filter_start_date) & (matches_col_filtered.date <= filter_end_date) & 
        (matches_col_filtered.Division.isin(divisions_list))
    ]

    return filtered_matches

def train_test_split_pipeline(filtered_matches, target, random_state=42, val_size=0.15, test_size=0.15):

    X = filtered_matches.drop(columns=[target])
    y = filtered_matches[target]

    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=(val_size + test_size), random_state=random_state, stratify=y)

    val_test_ratio = val_size / (val_size + test_size)

    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=(1 - val_test_ratio), random_state=random_state, stratify=y_temp)

    return X_train, X_val, X_test, y_train, y_val, y_test