import os
import pytest
import requests
from sqlitedict import SqliteDict
import pandas as pd

from mdcode.db.mp import load_materials

test_cache = "tests/db/test_cache.sqlite3"

def remove_test_cache():
    if os.path.exists(test_cache):
        os.remove(test_cache)
        print("Test cache removed successfully.")
    else:
        print("Test cache does not exist.")
    

def test_connectivity():
        response = requests.get("https://materialsproject.org/materials")
        response.raise_for_status()

def test_load_from_API():
    remove_test_cache()
    smry, mts = load_materials(["Ti"], (1,1),
        cache_key="Ti",
        cache_file=test_cache,
        override=True)
    assert len(smry) > 0 and len(mts) > 0

def test_cache_created():
    assert os.path.exists(test_cache)

def test_cache_written():
    with SqliteDict(test_cache) as cache:
        assert "Ti/materials" in cache and "Ti/summary" in cache

def test_load_from_cache():
    smry, mts = load_materials(None, None,
        cache_key="Ti",
        cache_file=test_cache)

def test_dataframes_are_sorted():
    smry, mts = load_materials("Ti", (1,1),
        cache_key="Ti",
        cache_file=test_cache)
    assert smry["material_id"].is_monotonic_increasing
    assert mts["material_id"].is_monotonic_increasing

def test_dataframes_contain_same_materials():
    smry, mts = load_materials("Ti", (1,1),
        cache_key="Ti",
        cache_file=test_cache)
    for m_id in mts.material_id:
        assert m_id in smry.material_id.values