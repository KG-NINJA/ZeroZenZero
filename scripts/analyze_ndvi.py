import os
import numpy as np
import rasterio
import matplotlib.pyplot as plt

# パス設定
DATA_FOLDER = os.getenv("DATA_FOLDER", "./data/")
RESULTS_FOLDER = os.getenv("RESULTS_FOLDER", "./results/")
INPUT_PATH = os.path.join(DATA_FOLDER, "raw", "input_ndvi.tif")
NDVI_PNG_PATH = os.path.join(RESULTS_FOLDER, "ndvi_map.png")
STATS_PATH = os.path.join(RESULTS_FOLDER, "ndvi_stats.txt")

def load_ndvi(input_path):
    with rasterio.open(input_path) as src:
        ndvi = src.read(1)
    return ndvi

def calc_stats(ndvi):
    mean = np.nanmean(ndvi)
    std = np.nanstd(ndvi)
    return mean, std

def save_ndvi_png(ndvi, out_path):
    plt.imshow(ndvi, cmap="RdYlGn", vmin=-1, vmax=1)
    plt.colorbar(label="NDVI")
    plt.title("NDVI Map")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

def save_stats(mean, std, out_path):
    with open(out_path, "w") as f:
        f.write(f"NDVI mean: {mean:.4f}\n")
        f.write(f"NDVI std: {std:.4f}\n")

if __name__ == "__main__":
    # 入力データ存在チェック
    if not os.path.exists(INPUT_PATH):
        print(f"ERROR: NDVI input file not found at {INPUT_PATH}")
        exit(1)
    ndvi = load_ndvi(INPUT_PATH)
    mean, std = calc_stats(ndvi)
    print(f"NDVI mean: {mean:.4f}")
    print(f"NDVI std: {std:.4f}")
    # 結果保存
    os.makedirs(RESULTS_FOLDER, exist_ok=True)
    save_ndvi_png(ndvi, NDVI_PNG_PATH)
    save_stats(mean, std, STATS_PATH)
    print(f"Saved NDVI map to {NDVI_PNG_PATH}")
    print(f"Saved NDVI stats to {STATS_PATH}")
