import struct
import random
import zlib


from enum import Enum

class Color(Enum):
    
    RED = (255, 0, 0, 255)  # Define RGBA For Red Color
    GREEN = (0, 255, 0, 255) # Define RGBA For Green Color
    BLUE = (0, 0, 255, 255) # Define RGBA For Blue Color
    BLACK = (0, 0, 0, 255) # Define RGBA For Black Color
    WHITE = (255, 255, 255, 255) # Define RGBA For White Color



class Cube():

    PNG_SIGNATURE = b'\x89PNG\r\n\x1a\n'

    def __init__(self, width:int = 8, color:Color = Color.RED) -> None:

        self.width = width;  
        self.size = width * width;   
        self.image_bytes = None
        self.raw_data = None
        self.png_data = None

        if color == None:
            rendImg = random.choice(list(Color)).value
            for a in range(0, self.size-1):
                rendImg += random.choice(list(Color)).value
            self.image_bytes = struct.pack(">%uB" % len(rendImg), * rendImg)
            self.raw_data = b''.join([b'\x00' + self.image_bytes[i:i + width * 4] for i in range(0, len(self.image_bytes), width*4)])
        else:
            self.image_bytes = struct.pack(">%uB" % len(color.value), * color.value) * self.size
            self.raw_data = b''.join([b'\x00' + self.image_bytes[i:i + width * 4] for i in range(0, len(self.image_bytes), width*4)])
        
    
    @staticmethod
    def create_chunk(chunk_type, data):
        length = struct.pack(">I", len(data))
        chunk_type = chunk_type.encode('ascii')
        crc = struct.pack(">I", zlib.crc32(chunk_type+data) & 0xFFFFFFFF)
        return length + chunk_type + data + crc


    def generate_png(self):
        compressed_data = zlib.compress(self.raw_data)
        ihdr_data = struct.pack(">IIBBBBB", self.width, self.width, 8, 6, 0, 0, 0)
        ihdr_chunk = Cube.create_chunk("IHDR", ihdr_data)
        idat_chunk = Cube.create_chunk("IDAT", compressed_data)
        iend_chunk = Cube.create_chunk("IEND", b'')
        self.png_data = Cube.PNG_SIGNATURE  + ihdr_chunk + idat_chunk +iend_chunk

    def save_png(self, output:str = './output'):
        output += ".png"
        with open(output, 'wb') as f:
            f.write(self.png_data)
    

if __name__ == "__main__":    
    cube = Cube(color=None)
    cube.generate_png()
    cube.save_png()

