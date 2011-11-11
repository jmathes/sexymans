#!/usr/bin/env python

import os, sys, urllib, random
from pprint import pformat
cmd_folder = os.path.dirname(os.path.abspath(__file__))
cmd_folder = os.path.join(cmd_folder, "jm_names")
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

import names


def name(phenny, input): 
    origterm = input.groups()[1]
    try:
        if not origterm: 
            return phenny.say('usage: name <gender> (<gender2> <gender3> ...)')
        raw_terms = origterm.encode('utf-8')
        raw_terms = raw_terms.lower()
        supported_types = names.supported_types()
        terms = raw_terms.split(" ")
        namelist = []
        for term in terms:
            if term not in supported_types:
                error = 'gender must be ' + ', '.join(supported_types[:-1]) + ', or ' + supported_types[-1] + '. other genders not supported, pervert'
                if raw_terms in error:
                    return phenny.say('ten points from gryffindor')
                if term in error:
                    return phenny.say('ten points from gryffindor')
                return phenny.say(error)
            namelist.append(names.get(term))
        return phenny.say(" ".join(namelist))
    except:
        return phenny.say('fifty points from gryffindor')


name.commands = ['name']
name.priority = 'high'

if __name__ == '__main__': 
    print __doc__.strip()
