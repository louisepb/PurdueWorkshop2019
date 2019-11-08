
RenderWin = GetRenderWindow()

# Change x yarns to grey
for x in range (0, 4):
    RenderWin.SetYarnColor(x, COLOR(0.5, 0.5, 0.5))
  
# Change y yarns to purple
for y in range (4, 8):
  RenderWin.SetYarnColor(y, COLOR(0.5,0,0.5))


