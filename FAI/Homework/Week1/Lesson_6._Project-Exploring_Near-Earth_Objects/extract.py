"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.
    f = open(neo_csv_path, 'r')
    f.readline()
    rdr = csv.reader(f)

    neos = []
    for line in rdr:
        neo = NearEarthObject(designation=line[3], name=line[4], diameter=line[15], hazardous=line[7])
        neos.append(neo)
    
    f.close()
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    f = open(cad_json_path, 'r')
    ld = json.load(f)

    approaches = []
    for des,orbit_id,jd,cd,dist,dist_min,dist_max,v_rel,v_inf,t_sigma_f,h in ld['data']:
        approach = CloseApproach(_designation=des, time=cd, distance=float(dist), velocity=float(v_rel))
        approaches.append(approach)
    f.close()
    return approaches
