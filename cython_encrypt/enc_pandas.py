import pandas as pd


def test():
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    pd.testing.assert_series_equal(
        df.x * df.y, pd.Series([4, 10, 18])
    )
    return 'OK'
