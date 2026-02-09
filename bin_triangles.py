import struct
import sys

def convert_obj_to_custom_bin(obj_file, output_file):
    vertices = []
    triangles = []
    
    with open(obj_file, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.split()
            if not parts: continue
            if parts[0] == 'v':
                vertices.append([float(parts[1]), float(parts[2]), float(parts[3])])
            elif parts[0] == 'f':
                indices = [int(p.split('/')[0]) - 1 for p in parts[1:4]]
                t = []
                for i in indices: t.extend(vertices[i])
                triangles.append(t)

    with open(output_file, 'wb') as f:
        
        f.write(struct.pack('<I', 0xA1030))
        for v in vertices:
            f.write(struct.pack('<I', 0))
            f.write(struct.pack('<3f', *v))

        f.write(struct.pack('<I', 0xA3050))
        for t in triangles:
            f.write(struct.pack('<I', 0)) 
            f.write(struct.pack('<9f', *t))

        f.write(struct.pack('<I', 0xA4060)) 

if __name__=="__main__":
	convert_obj_to_custom_bin(sys.argv[1],sys.argv[2])





