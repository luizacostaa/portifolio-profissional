import re
import colorsys

def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return '#{:02X}{:02X}{:02X}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2]))

def boost_color(hex_code):
    if len(hex_code) != 7: return hex_code # skip rgba, etc.
    r, g, b = hex_to_rgb(hex_code)
    # convert to hls (0 to 1)
    h, l, s = colorsys.rgb_to_hls(r/255.0, g/255.0, b/255.0)
    
    # Increase saturation significantly, and tweak lightness for punchiness
    s = min(1.0, s * 1.6)
    # Increase contrast: pull lightness away from 0.5 towards extremes slightly
    if l > 0.5:
        l = min(1.0, l * 1.1)
    else:
        l = max(0.0, l * 0.9)
        
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return rgb_to_hex((r*255, g*255, b*255))

with open("versao_final.html", "r") as f:
    text = f.read()

# We want to replace hex colors in the :root section basically.
# Let's find matches like #AABBCC
def replace_match(match):
    original = match.group(0)
    new_color = boost_color(original)
    return new_color

new_text = re.sub(r'#[0-9a-fA-F]{6}\b', replace_match, text)

with open("versao_final.html", "w") as f:
    f.write(new_text)

print("Colors boosted!")
