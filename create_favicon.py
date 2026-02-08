from PIL import Image, ImageDraw

def create_heart_favicon():
    size = (64, 64)
    image = Image.new('RGBA', size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # Heart shape coordinates
    # Simplified Bezier curve approximation or polygon
    # M 32 60 C 10 40 5 25 5 15 C 5 5 15 0 25 5 C 32 10 32 10 32 10 C 32 10 32 10 39 5 C 49 0 59 5 59 15 C 59 25 54 40 32 60 Z
    
    # Custom polygon points for a heart
    points = [
        (32, 60), (10, 35), (5, 20), (15, 5), (32, 15), 
        (49, 5), (59, 20), (54, 35)
    ]
    # Drawing two circles and a triangle approach for simpler PIL drawing
    
    # Left circle
    draw.ellipse((4, 4, 34, 34), fill='#ff6b9d')
    # Right circle
    draw.ellipse((30, 4, 60, 34), fill='#ff6b9d')
    # Triangle
    draw.polygon([(6, 20), (58, 20), (32, 60)], fill='#ff6b9d')
    
    image.save('favicon.png')
    print("favicon.png created")

if __name__ == "__main__":
    create_heart_favicon()
