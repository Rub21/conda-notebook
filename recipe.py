import pandas as pd

from pangeo_forge_recipes.patterns import ConcatDim, FilePattern
from pangeo_forge_recipes.recipes import XarrayZarrRecipe
from pangeo_forge_recipes.recipes import setup_logging
import xarray as xr

dates = pd.date_range('1981-09-01', '2022-02-01', freq='D')

URL_FORMAT = (
    "https://www.ncei.noaa.gov/data/sea-surface-temperature-optimum-interpolation/"
    "v2.1/access/avhrr/{time:%Y%m}/oisst-avhrr-v02r01.{time:%Y%m%d}.nc"
)

def make_url(time):
    return URL_FORMAT.format(time=time)

time_concat_dim = ConcatDim("time", dates, nitems_per_file=1)
pattern = FilePattern(make_url, time_concat_dim)



# Create recipe object
recipe = XarrayZarrRecipe(pattern, inputs_per_chunk=2)

# Set up logging
setup_logging()

# Prune the recipe
recipe_pruned = recipe.copy_pruned()

# Run the recipe
run_function = recipe_pruned.to_function()
run_function()

# Check the output
oisst_zarr = xr.open_zarr(recipe.target_mapper, consolidated=True)
print(oisst_zarr)
