import pandas as pd

# versión pandas
print(pd.__version__)


dicx = {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth"
            , "Gonzalo"
        ],
        "Age": [22, 35, 58, None],
        "Sex": ["male", "male", "female", None],
    }

# df -> es una variable de tipo Dataframe
df = pd.DataFrame(dicx)
print(df)