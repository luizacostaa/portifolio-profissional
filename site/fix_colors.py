with open("versao_final.html", "r") as f:
    content = f.read()

# Replace tailwind classes
content = content.replace("teal-400", "cyan-400")
content = content.replace("teal-500", "cyan-500")
content = content.replace("teal-600", "cyan-600")

# Update turquoise variables
content = content.replace("--turquoise: #14B8A6;", "--turquoise: #06B6D4;")
content = content.replace("--turquoise-light: #2DD4BF;", "--turquoise-light: #22D3EE;")
content = content.replace("--turquoise-dark: #0D9488;", "--turquoise-dark: #0891B2;")
content = content.replace("rgba(20, 184, 166", "rgba(6, 182, 212")

# Update scrollbar thumb gradient
old_scrollbar = """    ::-webkit-scrollbar-thumb {
      background: var(--turquoise);
      border-radius: 4px;
    }"""
new_scrollbar = """    ::-webkit-scrollbar-thumb {
      background: linear-gradient(135deg, #EC4899 0%, #8B73F3 100%);
      border-radius: 4px;
    }"""
content = content.replace(old_scrollbar, new_scrollbar)

# Update hover of scrollbar
old_scrollbar_hover = """    ::-webkit-scrollbar-thumb:hover {
      background: var(--turquoise-light);
    }"""
new_scrollbar_hover = """    ::-webkit-scrollbar-thumb:hover {
      background: linear-gradient(135deg, #F472B6 0%, #A78BFA 100%);
    }"""
content = content.replace(old_scrollbar_hover, new_scrollbar_hover)

# Update gradient text to explicitly use the tech_rosa pink-to-purple gradient
old_gradient = """    .gradient-text {
      background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }"""
new_gradient = """    .gradient-text {
      background: linear-gradient(135deg, #EC4899 0%, #8B73F3 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }"""
content = content.replace(old_gradient, new_gradient)

# Update Javascript SDK defaults for the color
content = content.replace("primary_action_color: '#14B8A6'", "primary_action_color: '#06B6D4'")

# Update section divider to pink and blue gradient like tech_rosa
content = content.replace(
"""    .section-divider {
      background: linear-gradient(90deg, transparent 0%, var(--turquoise) 50%, transparent 100%);
      height: 1px;
    }""",
"""    .section-divider {
      background: linear-gradient(90deg, transparent 0%, #06B6D4 25%, #8B73F3 75%, transparent 100%);
      height: 1px;
    }""")

with open("versao_final.html", "w") as f:
    f.write(content)

print("Modification complete.")
