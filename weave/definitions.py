from dagster import Definitions, load_assets_from_modules

from weave import assets  # type: ignore

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
)
