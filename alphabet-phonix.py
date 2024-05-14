def findAlpha(alpha) : 
    if alpha == 'a' : return "For Apple"
    elif alpha == 'b' : return "For Ball"
    elif alpha == 'c' : return "For Circle"
    elif alpha == 'd' : return "For Diamond"
    elif alpha == 'e' : return "For Envelope"
    elif alpha == 'f' : return "For Fragment"
    elif alpha == 'g' : return "For Group"
    elif alpha == 'h' : return "For Half"
    elif alpha == 'i' : return "For Intersection"
    elif alpha == 'j' : return "For Joystick"
    elif alpha == 'k' : return "For Keyboard"
    elif alpha == 'l' : return "For Link"
    elif alpha == 'm' : return "For Mobile"
    elif alpha == 'n' : return "For Network"
    elif alpha == 'o' : return "For Ola"
    elif alpha == 'p' : return "For phonix"
    elif alpha == 'q' : return "For Quack"
    elif alpha == 'r' : return "For Rabit"
    elif alpha == 's' : return "For Spider"
    elif alpha == 't' : return "For Transparent"
    elif alpha == 'u' : return "For Unicode"
    elif alpha == 'v' : return "For Verbatim"
    elif alpha == 'w' : return "For Water"
    elif alpha == 'x' : return "For X-sheet"
    elif alpha == 'y' : return "For Yark"
    elif alpha == 'z' : return "For Zebracoin"
    else : return "Not Found"

def App () :
    print("--------------------------------")
    print("Alphabet Phonix")
    print("--------------------------------")
    alpha = input("* Enter Your Alphabet\n").lower()
    result = findAlpha(alpha)
    print("==>",alpha.upper(), result)
    App()
App()