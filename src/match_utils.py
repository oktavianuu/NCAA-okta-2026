# matchup_utils.py
import pandas as pd

def match(team1, team2, df=None):
    """
    Find the matchup row between two teams in the global DataFrame 'readable_submission'.
    
    Parameters
    ----------
    team1, team2 : str
        Names of the two teams (order doesn't matter).
    df : pd.DataFrame, optional
        DataFrame with columns 'Team_A', 'Team_B', 'Win_Prob_A', etc.
        If not provided, the function looks for a global variable named 'readable_submission'
        in the caller's scope (e.g., your notebook).

    Returns
    -------
    pd.DataFrame
        Rows matching the matchup (should be exactly one row if the pair exists).
        Returns an empty DataFrame if no match is found.
    """
    # If no DataFrame is passed, try to get it from the global scope of the caller
    if df is None:
        import inspect
        caller_globals = inspect.currentframe().f_back.f_globals
        df = caller_globals.get('readable_submission')
        if df is None:
            raise ValueError(
                "No DataFrame provided and no global variable 'readable_submission' found. "
                "Please pass your DataFrame explicitly using df=your_df."
            )

    # Create a boolean mask for both possible orders
    mask = (
        ((df['Team_A'] == team1) & (df['Team_B'] == team2)) |
        ((df['Team_A'] == team2) & (df['Team_B'] == team1))
    )

    result = df[mask]
    if result.empty:
        print(f"⚠️ No matchup found between '{team1}' and '{team2}'")
    return result