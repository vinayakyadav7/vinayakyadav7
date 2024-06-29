# generate_snake.py

import datetime
import os

def generate_snake():
    # Replace this with your logic to generate SVG content
    today = datetime.date.today()
    svg_content = f'<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="black" /><text x="10" y="50" font-family="Verdana" font-size="35" fill="white">{today}</text></svg>'
    return svg_content

if __name__ == "__main__":
    svg_content = generate_snake()
    if not os.path.exists('dist'):
        os.makedirs('dist')
    with open('dist/github-contribution-grid-snake.svg', 'w') as f:
        f.write(svg_content)
