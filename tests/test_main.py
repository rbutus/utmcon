import pytest
import utmcon
import pandas as pd
import os


def test_to_ll(tmpdir):
    d = tmpdir.join("data.csv")
    d.write("""latitude,longitude,id
555555,5555555,MW18-100""")

    filename = os.path.join(d.dirname, d.basename)
    print(d.dirname)
    print(d.basename)

    df = pd.read_csv(filename)
    print(df)

    column_names = list(df.columns.values)

    assert "latitude" in column_names
    assert "longitude" in column_names
    assert df.loc[0, "latitude"] == 555555

