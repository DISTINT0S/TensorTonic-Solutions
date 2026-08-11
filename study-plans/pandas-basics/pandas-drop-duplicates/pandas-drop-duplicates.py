import pandas as pd
data = {"name": ["A", "B", "A", "C"], "val": [1, 2, 1, 3]}
def drop_duplicates(data):
    """
    Returns: list [rows_before, rows_after, cleaned_data]
    """

    df = pd.DataFrame(data)

    rows_before = df.shape[0]
    cleaned_data = df.drop_duplicates()
    rows_after = cleaned_data.shape[0]

    res = {
        "rows_before": rows_before,
        "rows_after": rows_after,
        "cleaned_data": cleaned_data.to_dict("list")
    }


    return [rows_before, rows_after, cleaned_data.to_dict("list")]