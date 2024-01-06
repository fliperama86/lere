import os
import struct

PROM_MAX_SIZE = 0x800000 # 8MB in HEX

class NeoSDRom:
  def __init__(self, file_path):
    self.file_path = file_path
    self.file_content = open(file_path, "rb").read()
    self.header_size = 4096
    self.sizes = struct.unpack("<IIIIII", self.file_content[4:28])
    self.eproms = self.get_eproms()

  def get_eproms(self):
    eproms = {}
    offset = self.header_size
    for index, name in enumerate(['prom', 'srom', 'm1rom', 'vroma0', 'vroma2', 'crom0']):
      size = self.sizes[index]
      eproms[name] = self.file_content[offset:offset+size]

      if name == 'crom0':
        crom0 = bytearray(eproms[name])
        crom0[1::4], crom0[2::4] = crom0[2::4], crom0[1::4]
        eproms[name] = crom0
      
      if name == 'prom' and size > PROM_MAX_SIZE:
        eproms[name] = self.file_content[offset:offset+PROM_MAX_SIZE]
        eproms[name+'1'] = self.file_content[offset+PROM_MAX_SIZE:offset+size]
      
      offset += size
    return eproms

  def get_prom(self):
    return self.eproms['prom']

  def get_srom(self):
    return self.eproms['srom']

  def get_m1rom(self):
    return self.eproms['m1rom']

  def get_vroma0(self):
    return self.eproms['vroma0']

  def get_crom0(self):
    return self.eproms['crom0']

  def get_file_path(self):
    return self.file_path

  def get_file_name(self):
    return os.path.basename(self.file_path)

  def get_file_name_without_extension(self):
    return os.path.splitext(self.get_file_name())[0]