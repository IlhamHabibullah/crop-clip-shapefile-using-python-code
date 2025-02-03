import geopandas as gpd

# Path ke file shapefile
zonasi_path = "/home/gps06/Downloads/Zonasi_Kawasan_Konservasi_2024_B8/Zonasi_Kawasan_Konservasi_2024_B8.shp"
wpp_path = "/home/gps06/Documents/1_tes/wpp_714/poly_wpp_714.shp"
output_path = "/home/gps06/Documents/1_tes/wpp_714/clipped_zonasi.shp"

# Membaca shapefile
zonasi_gdf = gpd.read_file(zonasi_path)
wpp_gdf = gpd.read_file(wpp_path)

# Periksa dan tetapkan CRS jika tidak ada
if zonasi_gdf.crs is None:
    zonasi_gdf.set_crs(epsg=4326, inplace=True)  # Ganti dengan CRS yang sesuai
if wpp_gdf.crs is None:
    wpp_gdf.set_crs(epsg=4326, inplace=True)  # Ganti dengan CRS yang sesuai

# Memastikan kedua shapefile memiliki CRS yang sama
if zonasi_gdf.crs != wpp_gdf.crs:
    wpp_gdf = wpp_gdf.to_crs(zonasi_gdf.crs)

# Melakukan clip (crop) shapefile
clipped_gdf = gpd.clip(zonasi_gdf, wpp_gdf)

# Menyimpan hasil clip ke file shapefile baru
clipped_gdf.to_file(output_path)

print(f"Shapefile berhasil dipotong dan disimpan di {output_path}")
