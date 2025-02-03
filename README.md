# crop-clip-shapefile-using-python-code
cara memotong data shapefile menggunakan code python perhatikan CRS nyaa


import geopandas as gpd


zonasi_path = ""
wpp_path = ""
output_path = ""


zonasi_gdf = gpd.read_file(zonasi_path)
wpp_gdf = gpd.read_file(wpp_path)


if zonasi_gdf.crs is None:
    zonasi_gdf.set_crs(epsg=4326, inplace=True)  # Ganti dengan CRS yang sesuai
if wpp_gdf.crs is None:
    wpp_gdf.set_crs(epsg=4326, inplace=True)  # Ganti dengan CRS yang sesuai


if zonasi_gdf.crs != wpp_gdf.crs:
    wpp_gdf = wpp_gdf.to_crs(zonasi_gdf.crs)

clipped_gdf = gpd.clip(zonasi_gdf, wpp_gdf)


clipped_gdf.to_file(output_path)

print(f"Shapefile berhasil dipotong dan disimpan di {output_path}")
