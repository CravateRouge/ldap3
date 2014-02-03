"""
Created on 2014.01.06

@author: Giovanni Cannata

Copyright 2014 Giovanni Cannata

This file is part of python3-ldap.

python3-ldap is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

python3-ldap is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with python3-ldap in the COPYING and COPYING.LESSER files.
If not, see <http://www.gnu.org/licenses/>.
"""
from os import linesep


class Attribute(object):
    """
    Attribute/values object, it includes the search result (after postQuery transformation) of each attribute in an entry
    Attribute object is read only
    'values' contains the processed attribute values
    'rawValues' contains the unprocessed attribute values
    """
    def __init__(self, attrDef, entry):
        self.__dict__['key'] = attrDef.key
        self.__dict__['definition'] = attrDef
        self.__dict__['values'] = []
        self.__dict__['rawValues'] = []
        self.__dict__['entry'] = entry

    def __repr__(self):
        if len(self.values) == 1:
            r = self.key + ': ' + str(self.values[0])
        elif len(self.values) > 1:
            r = self.key + ': ' + str(self.values[0])
            filler = ' ' * (len(self.key) + 6)
            for value in self.values[1:]:
                r += linesep + filler + str(value)
        else:
            r = ''

        return r

    def __str__(self):
        if len(self.values) == 1:
            return self.values[0]
        else:
            return str(self.values)

    def __len__(self):
        return len(self.values)

    def __iter__(self):
        return self.values.__iter__()

    def __getitem__(self, item):
        return self.values[item]

    def __setattr__(self, item, value):
        raise Exception('attribute is read only')
