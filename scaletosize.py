#!/usr/bin/env python

# These two lines are only needed if you don't put the script directly into
# the installation directory
import sys
sys.path.append('/usr/share/inkscape/extensions')

'''
TODO

Copyright (C) 2015 Johan Andruejol, johan.andruejol@gmail.com

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
'''

import inkex
import cubicsuperpath, simplestyle, copy, math, re, bezmisc # TO CHECK
import measure, simpletransform

class ScaleToSize(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option("--measurement_type",
                        action="store", type="string", 
                        dest="measurement_type", default="length",
                        help="Type of measurement")
        self.OptionParser.add_option("-s", "--expected_size",
                        action="store", type="float", 
                        dest="expected_size", default=1,
                        help="The expected size of the path")
        self.OptionParser.add_option("--scale_type",
                        action="store", type="string", 
                        dest="scale_type", default="uniform",
                        help="Scale type (uniform, horizontal, vertical)")
        self.OptionParser.add_option("--help",
                        action="store", type="string", 
                        dest="help", default="",
                        help="dummy")

    def effect(self):
        # Get the selected path size
        for id, node in self.selected.iteritems():
            if node.tag == inkex.addNS('path','svg'):
                self.group = inkex.etree.SubElement(node.getparent(),inkex.addNS('text','svg'))
                
                if self.options.measurement_type == "length":
                    unused, currentsize = measure.csplength(p)
                else:
                    currentsize = measure.csparea(p)
        
                # Create transform
                scalefactor = currentsize / self.options.expected_size()
                transformstring = ""
                if self.options.scale_type() = "horizontal":
                    transformstring = "scale(0," + scalefactor ")"
                else if self.options.scale_type() = "vertical":
                    transformstring = "scale(" + scalefactor ",0)"
                else: #uniform
                    transformstring = "scale(" + scalefactor ")"

                transform = simpletransform.parsetransform(transformstring)
                simpletransform.applyTransformNode(transform, node)              

if __name__ == '__main__':
    e = ScaleToSize()
    e.affect()

