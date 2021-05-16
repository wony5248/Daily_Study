import sys

FF, FS, SF, SS = map(int, input().split())
song = []
stack = []
for i in range(FF):
    song.append("FF")
for i in range(FS):
    song.append("FS")
for i in range(SF):
    song.append("SF")
for i in range(SS):
    song.append("SS")
print(song)

for so in song:
    