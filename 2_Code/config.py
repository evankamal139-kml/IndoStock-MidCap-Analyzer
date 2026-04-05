import os

# Get the directory where config.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Use 'r' for Raw Strings and separate components for safety
RAW_DATA_PATH = os.path.normpath(os.path.join(BASE_DIR, r'..\1_Data\0_Raw_Data\Ringkasan_Perdagangan_Saham'))
DAFTAR_SAHAM = os.path.normpath(os.path.join(BASE_DIR, r'..\1_Data\0_Raw_Data\Daftar_Saham'))
INGESTED_DATA_PATH = os.path.normpath(os.path.join(BASE_DIR, r'..\1_Data\1_Ingestion_Ringkasan_Perdagangan_Saham'))
MASKED_DATA_DAFTAR_SAHAM_PATH = os.path.normpath(os.path.join(BASE_DIR, r'..\1_Data\2_Masked_Data\Masked_Daftar_Saham'))
MASKED_DATA_RINGKASAN_PERDAGANGAN_SAHAM_PATH = os.path.normpath(os.path.join(BASE_DIR, r'..\1_Data\2_Masked_Data\Masked_Ringkasan_Perdagangan_Saham'))
CLEAN_MASTER_DATA_PATH = os.path.normpath(os.path.join(BASE_DIR, r'..\1_Data\3_Cleaning_Data'))