# Split NeoSD roms (.neo) into Darksoft rom format (eprom, srom, m1rom, vroma0, vroma2, crom0)
import sys
import os
from os import path
from binascii import crc32
from neosd_rom import NeoSDRom

if len(sys.argv) < 2:
  print("No input given")
  exit()

if len(sys.argv) < 3:
  print("No output given")
  exit()

neo_file_path = sys.argv[1]

print(f"Reading {neo_file_path}")

neofile = NeoSDRom(neo_file_path)
output_dir = path.join(sys.argv[2], neofile.get_file_name_without_extension())

if not path.exists(output_dir):
  os.mkdir(output_dir)

print(f"Writing to {output_dir}")

for key in neofile.eproms:
  eprom_path = path.join(output_dir, key)
  if len(neofile.eproms[key]) == 0:
    continue
  print(f"{key}\tsize: {len(neofile.eproms[key])} \tcrc: {hex(crc32(neofile.eproms[key]))}")
  with open(eprom_path, "wb") as f:
    f.write(neofile.eproms[key])
  
print("Done")