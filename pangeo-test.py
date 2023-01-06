
# #### Testing
from dask.diagnostics import ProgressBar
import intake

recipe_pruned = recipe.copy_pruned()
delayed = recipe_pruned.to_dask()
with ProgressBar():
    delayed.compute()
cat_url = f"{recipe_pruned.target}/reference.yaml"
cat = intake.open_catalog(cat_url)
ds = cat.data.to_dask()
print(ds)

df = ds.to_dask_dataframe()
df.to_csv('out.csv')
