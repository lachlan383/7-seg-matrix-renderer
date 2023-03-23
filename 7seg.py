import pygame, math
from PIL import Image

segs = (32, 12)
seg_size = 24
spacing = 1.1

# .56" 7 seg digit display w/ 8 degree skew
#
#         ___A__
#        /     /
#       F     B
#      /__G__/
#     /     /
#    E     C
#   /__D__/   (DP)
#
# vertices:
# (-2.5, -6.4) FA
# (4.3, -6.4) AB
# (3.4, 0) BC
# (2.5, 6.4) CD
# (-4.3, 6.4) DE
# (-3.4, 0) EF
# Segment G connects EF to BC
# Segment DP (4.3, 6.4), dia 1.4
# lines 1.4 thick

img = Image.open("sample.png")

verts = {   "FA": (-.25, -.64),
            "AB": (.43, -.64),
            "BC": (.34, 0),
            "CD": (.25, .64),
            "DE": (-.43, .64),
            "EF": (-.34, 0),
             "P":  (.43, .64)   }

lines = {   "A": (verts['FA'], verts['AB']),
            "B": (verts['AB'], verts['BC']),
            "C": (verts['BC'], verts['CD']),
            "D": (verts['CD'], verts['DE']),
            "E": (verts['DE'], verts['EF']),
            "F": (verts['EF'], verts['FA']),
            "G": (verts['EF'], verts['BC']),
            "P": (verts['P'], verts['P'])   }

seg_aspect = (1, 1.42)

def line_centre(line):
    return ( line[0][0]/2 + line[1][0]/2, line[0][1]/2 + line[1][1]/2 )

def surf_at_pt(point):
    # point must be in ([0,1], [0,1])

    
    # zoom = 1.5 + 0.5*math.sin(time*0.00007)
    # disable image zoom:
    zoom = 1
    x = (point[0]-.5)*zoom + 0.5
    y = point[1]*zoom
    # disable animating with time:
    # x += math.sin(time*0.0003)*.1
    # y += time*0.00003
    # y = y % 1.2
    point = ( min(max(0, x), 1) , min(max(0, y), 1) )

    pixel = (int(img.width*point[0]-1), int(img.height*point[1]-1))
    px_val = img.getpixel(pixel)
    
    # 3 brightness levels (2-bit):
    return (1 - (float(px_val[0]+px_val[1]+px_val[2])/255/3))

running = True
screen = pygame.display.set_mode((int((segs[0])*seg_aspect[0]*seg_size*spacing),
                                    int((segs[1])*seg_aspect[1]*seg_size*spacing)))
time = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill((0,0,0))

    for i in range(segs[0]):
        for j in range(segs[1]):

            for seg in "ABCDEFGP":
                pos = ((i+0.5)/(segs[0]), (j+0.5)/(segs[1]))
                lc = line_centre(lines[seg])
                point = (pos[0] + lc[0]/segs[0], pos[1] + lc[1]/segs[1])
                line_start = ( int((lines[seg][0][0]/segs[0]/seg_aspect[0]/spacing+pos[0])*screen.get_width()),
                                int((lines[seg][0][1]/segs[1]/seg_aspect[1]/spacing+pos[1])*screen.get_height()) )
                line_end = ( int((lines[seg][1][0]/segs[0]/seg_aspect[0]/spacing+pos[0])*screen.get_width()),
                                int((lines[seg][1][1]/segs[1]/seg_aspect[1]/spacing+pos[1])*screen.get_height()) )
                if seg == 'P':
                    line_start = (line_start[0], line_start[1] - int(seg_size*.07) - 1)
                    line_end = (line_end[0], line_end[1] + int(seg_size*.07))

                pygame.draw.line(screen, (127*int(2*surf_at_pt(point)),0,0), line_start, line_end, int(seg_size*.14))

    pygame.display.flip()

    while pygame.time.get_ticks() - time < (1000/60):
        pygame.time.wait(1)
    time = pygame.time.get_ticks()

