#Helper function to translate playerIDs to actually names.
def name_lookup(playerID, df_bio):
    player_row = df_bio[df_bio['playerID'] == playerID]
    real_name = player_row.iloc[0]['nameGiven'] + " " + player_row.iloc[0]['nameLast']
    return real_name

#Sums up yearly fielding stats to give careers stats for players
def find_career_fielding_stats(df_fieldingstats):
    df_careerfielding  = df_fieldingstats.groupby(['playerID', 'POS'], as_index=False).sum()
    return df_careerfielding 

#Given a player and career fielding stats, return that player's primary postion.
def find_primary_postion(player, df_fieldingstats):
    # Filter the dataframe for the given playerID
    df_playerspostion = df_fieldingstats[df_fieldingstats['playerID'] == player]
    
    # Check if the filtered dataframe is empty
    if df_playerspostion.empty:
        return None  # or you can return a message like "Player not found"
    
    # Find the row with the maximum value in the 'Games' column
    max_games_row = df_playerspostion.loc[df_playerspostion['G'].idxmax()]
    
    # Return the 'Position' value of that row
    return max_games_row['POS']