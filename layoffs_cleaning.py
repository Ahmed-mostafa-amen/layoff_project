# %%
import pandas as pd
import numpy as np



df = pd.read_csv(r"G:\New folder\layoffs.csv")
df

# %%
#pd.set_option('display.max_rows', None)      # show all rows
#pd.set_option('display.max_columns', None)   # show all columns
#pd.set_option('display.width', None)         # don't wrap based on terminal width
#pd.set_option('display.max_colwidth', None)  # don't truncate long text in cells
pd.reset_option('all')
df

# %%
df.isnull()

# %%
df.drop_duplicates(inplace=True)
df

# %%
df[df[
        "total_laid_off"
    ].isnull()
]

# %%
df.sort_values(by="total_laid_off",ascending=False)

# %%
df.select_dtypes(include="number").corr()

# %%
df =df.dropna(subset=[
    "total_laid_off",
    "percentage_laid_off"
],how="all")
df

# %%

pd.set_option("display.max.rows",None)
df.groupby(by=[
    "country"
])[
    "total_laid_off"
].sum()

# %%

df.isnull().any(axis=1).sum()


# %%


# %%
df[df.eq("").any(axis=1)
]          # rows with any empty string
(df == "").sum()     

# %%
pd.reset_option("all")
df

# %%
df[
    "country"
] = df[
    "country"
].str.replace('United States.', 'United States', regex=False)

# %%
df[
    "country"
].unique
# %%

# %%
pd.reset_option("all")

# %%

df[
    "industry"
] = df[
    "industry"
].replace({
    "Crypto Currency": "Crypto",
    "CryptoCurrency": "Crypto"
})

# %%
df.groupby("industry").sum()

# %%
sorted(df['industry'
].dropna().unique())

# %%
df[
    "country"
] = df[
    "country"
].str.strip(
)

# %%
df[
    "company"
] = df[
    "company"
].str.strip()
# %%
df.to_csv(r"g:\layoffproject.csv",index=False)
# %%
# %%



