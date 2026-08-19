import pandas as pd

def groupby_basics(data, group_col, value_col):
    """
    Returns: dict with 'sum', 'mean', 'count' (each a dict)
    """

    df = pd.DataFrame(data)

    grouped_df = df.groupby([group_col]).agg(
        sum=(value_col, "sum"),
        mean=(value_col, "mean"),
        count=(value_col, "count")
    )

    return grouped_df.to_dict()