"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')
    # TODO: Write the results to a CSV file, following the specification in the instructions.

   
    f = open(filename, 'w', newline='')
    wr = csv.writer(f)
    wr.writerow(['datetime_utc', 'distance_au', 'velocity_km_s', 
                    'designation', 'name', 'diameter_km', 'potentially_hazardous'])
    
    for approach in results:
        approach_serial = approach.serialize()
        neo_serial = approach.neo.serialize()
        wr.writerow([approach_serial.get('datetime_utc'), approach_serial.get('distance_au'), approach_serial.get('velocity_km_s'),
                     neo_serial.get('designation'), neo_serial.get('name'), neo_serial.get('diameter_km'), neo_serial.get('potentially_hazardous')])

    f.close()


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # TODO: Write the results to a JSON file, following the specification in the instructions.
    
    f = open(filename, 'w')
    res = []
    for appoach in results:
        res.append(appoach.serialize())
    json.dump(res, f, indent='\t')