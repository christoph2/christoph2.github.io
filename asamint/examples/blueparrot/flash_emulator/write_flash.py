#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""HEX file downloader.
"""

__copyright__ = """
    pySART - Simplified AUTOSAR-Toolkit for Python.

   (C) 2009-2020 by Christoph Schueler <cpu12.gems@googlemail.com>

   All Rights Reserved

  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License along
  with this program; if not, write to the Free Software Foundation, Inc.,
  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

import time


from objutils import load
from pyxcp.cmdline import ArgumentParser

HEX_FILE_NAME = "paged_flash.s28"

hex_file = load("srec", HEX_FILE_NAME)

def upload_file(xcp_master):
    for sec in hex_file:
        address = 0x8000    # Paging window.
        address_ext = (sec.start_address >> 16) - 0x10    # Calculate page number.
        data = sec.data
        print(hex(address), address_ext, len(sec))
        xcp_master.setMta(address, address_ext)
        xcp_master.push(data)

def callout(master, args):
    if args.sk_dll:
        master.seedNKeyDLL = args.sk_dll

ap = ArgumentParser(callout, description = "HEX file downloader.")
ap.parser.add_argument("-s", "--sk-dll", dest = "sk_dll", help = "Seed-and-Key .DLL name", type = str, default = None)

with ap.run() as x:
    x.connect()
    if x.slaveProperties.optionalCommMode:
        x.getCommModeInfo()
    x.cond_unlock()
    upload_file(x)
    x.disconnect()
