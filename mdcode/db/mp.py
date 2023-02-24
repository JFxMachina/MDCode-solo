#!/usr/bin/env python3
"""Fetch and cache materials from the Materials Project database."""

import sys
from os import environ
from mp_api.client import MPRester
import pandas as pd

def load_materials(
        elements,
        nelements,
        cache_key="NA",
        override=False,
        cache_file="data/MP/materials.sqlite3",
        verbose=True) \
        -> (pd.DataFrame, pd.DataFrame):
    """Load materials from the Materials Project database.

    Loads data from the summary and materials endpoints of the Materials
    Project API and tries to cache them in a local sqlite database.
    If the database exists already, the data is loaded from the database
    instead (In this case <elements> and <nelements> is ignored,
    except if override is also set to true).

    Caching requires the sqlitedict python package.

    Args:
        elements (List(str)): List of elements.

        nelements (Touple(int, int)): Range of number of elements.

        cache_key (str): The key under which the material is stored in
            the local cache. The summary and materials will be stored at
            '<cache_key>/summary' and '<cache_key>/materials',
            respectively.
            Defaults to "NA" but gives a warning when
            writing to the cache using the default key.

        override (bool, optional): Whether to override the cached data
            (force reloading from Materials Project database).
            Defaults to False.

        cache_file (str, optional): Path to cache file.
            If an empty string is passed, no attempts to read or write a
            cache file are made.
            Defaults to "data/MP/materials.sqlite3".

        verbose (bool, optional): Whether to print output regarding
            caching. Defaults to True.

    Raises:
        Exception: Fails if materials aren't cached and 'MP_API_KEY'
            isn't present in the environment variables.

    Returns:
        tuple(DataFrame, DataFrame): (summary, materials)
    """

    df_summary = None
    df_materials = None

    try:
        from sqlitedict import SqliteDict
    except Exception as ex:
        pass

    if "sqlitedict" in sys.modules and len(cache_file) > 0:
        try:
            with SqliteDict(cache_file) as c_dict:
                if cache_key + "/materials" in c_dict \
                and cache_key + "/summary" in c_dict \
                and not override:
                    df_summary = c_dict[cache_key + "/summary"]
                    df_materials = c_dict[cache_key + "/materials"]
                    if verbose:
                        print("Materials loaded from cache.")

        except Exception as ex:
            print("Failed to load cached materials.")
            print(ex)

    if df_summary is None or df_materials is None or override:
        # MPRester uses the MP_API_KEY environment variable as default
        # if no key is passed
        if not "MP_API_KEY" in environ:
            raise Exception(
                "'MP_API_KEY' not found in environment variables."
                "Please make sure the API key is exported to the parent"
                "environment and try again.")

        with MPRester() as mpr:
            summary = mpr.summary.search(
                elements=elements,
                num_elements=nelements)
            materials = mpr.materials.search(
                material_ids=[s.material_id for s in summary])
                # fields=[
                #         'nsites', 'elements', 'nelements',
                #         'composition', 'composition_reduced',
                #         'formula_pretty', 'formula_anonymous',
                #         'chemsys', 'volume', 'density', 'material_id'
                #         'density_atomic', 'symmetry', 'structure'
                #         ]
            df_summary = pd.DataFrame([mat.__dict__ for mat in summary])
            df_materials = pd.DataFrame([mat.__dict__ for mat in materials])
        
        if "sqlitedict" in sys.modules and len(cache_file) > 0:
            try:
                with SqliteDict(cache_file) as c_dict:
                    c_dict[cache_key + "/summary"] = df_summary
                    c_dict[cache_key + "/materials"] = df_materials
                    c_dict.commit()
                    if verbose:
                        print("Saved materials to cache.")
            except Exception as ex:
                print("Failed to save materials to sqlite cache.")
                print(ex)
    
    return df_summary, df_materials
        