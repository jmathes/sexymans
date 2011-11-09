#!/usr/bin/env python

import os, sys, urllib, random
cmd_folder = os.path.dirname(os.path.abspath(__file__))
cmd_folder = os.path.join(cmd_folder, "jm_names")
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

import names


def name(phenny, input): 
    origterm = input.groups()[1]
#    try:
    if True: 
        if not origterm: 
            return phenny.say('usage: name <gender>')
        term = origterm.encode('utf-8')
        term = term.lower()
        supported_types = names.supported_types()
        if term not in supported_types:
            error = 'gender must be ' + ', '.join(supported_types[:-1]) + ', or ' + supported_types[-1] + '. other genders not supported, pervert'
            if term in error:
                return phenny.say('ten points from gryffindor')
            return phenny.say(error)
        return phenny.say(names.get(term))
#    except:
#        return phenny.say('fifty points from gryffindor')


name.commands = ['name']
name.priority = 'high'

if __name__ == '__main__': 
    print __doc__.strip()
