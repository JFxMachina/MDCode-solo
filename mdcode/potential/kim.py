#!/usr/bin/env python3
"""Utility related to openKIM potentials."""
from kim_query import get_available_models

def get_potentials(elements, logic=["exact"]):
    element_list = [element.name for element in elements]
    potentials = get_available_models(
        species=element_list,
        model_interface=["mo"],
        species_logic=logic)
    return potentials
    
