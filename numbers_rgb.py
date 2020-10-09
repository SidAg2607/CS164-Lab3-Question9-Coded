def bitosm(binaryx):
    s1 = list(binaryx)
    if s1[0] == "0":
        s1[0] = "1"
    else:
        s1[0] = "0"
    return s1

def bitooc(binaryx):
    s1 = list(binaryx)
    q = 0
    while(q<8):
        if s1[q] == "1":
            s1[q] = "0"
            q+=1
        else:
            s1[q] = "1"
            q+=1
    onedec = 0
    t = 0
    while(t<8):
        onedec += int(s1[7-t])*(2**t)
        t+=1
    return onedec
    
def twodec(onedecx):
    if onedecx == 255:
        return 0
    else:
        return onedecx+1

def recurse():

  rgb1 = int(input("1st part of rgb color code: "))
  rgb2 = int(input("2nd part of rgb color code: "))
  rgb3 = int(input("3rd part of rgb color code: "))

  
  binary1 = ""
  binary2 = ""
  binary3 = ""
    
  i = 0
  while(i<8):
    binary1 = str(rgb1%2) + binary1
    rgb1 = int(rgb1/2)
    binary2 = str(rgb2%2) + binary2
    rgb2 = int(rgb2/2)
    binary3 = str(rgb3%2) + binary3
    rgb3 = int(rgb3/2)
    i+=1

  signmag1 = "".join(bitosm(binary1))
  signmag2 = "".join(bitosm(binary2))
  signmag3 = "".join(bitosm(binary3))

  smdec1 = 0
  smdec2 = 0
  smdec3 = 0

  j = 0
  while(j<8):
    smdec1 += int(signmag1[7-j])*(2**j)
    smdec2 += int(signmag2[7-j])*(2**j)
    smdec3 += int(signmag3[7-j])*(2**j)
    j += 1
    
  onedec1 = bitooc(binary1)
  onedec2 = bitooc(binary2)
  onedec3 = bitooc(binary3)

  twodec1 = twodec(onedec1)
  twodec2 = twodec(onedec2)
  twodec3 = twodec(onedec3)

  print("\nSign Magnitude: " + str(smdec1) + ", " + str(smdec2) + ", " + str(smdec3))
    
  print("\nOne's Complement: " + str(onedec1) + ", " + str(onedec2) + ", " + str(onedec3))
    
  print("\nTwo's Complement: " + str(twodec1) + ", " + str(twodec2) + ", " + str(twodec3))

  print("___________________________________________\n")

  recurse()

recurse()
