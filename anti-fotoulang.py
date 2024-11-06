from PIL import Image
import imageio

def create_non_repeating_gif(image_path, output_gif_path, duration_per_image=2, fps=30, total_duration=60):
    img = Image.open(image_path)
    width, height = img.size
    
    image_duration = duration_per_image * fps
    black_frame_duration = (total_duration - duration_per_image) * fps 
    
    frames = []
    
    for _ in range(image_duration):
        frames.append(img)
    
    black_frame = Image.new('RGB', (width, height), color='black')
    for _ in range(black_frame_duration):
        frames.append(black_frame)
    
    frames[0].save(output_gif_path, save_all=True, append_images=frames[1:], duration=1000/fps, loop=0)
    print(f"GIF berhasil dibuat dan disimpan di: {output_gif_path}")

image_path = 'image1.jpg' 

output_gif_path = 'output_non_repeating.gif'

create_non_repeating_gif(image_path, output_gif_path)

