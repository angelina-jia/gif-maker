import imageio.v3 as iio
print("🎬 Starting GIF creation...")
filenames = ['my_melody_gif1.png', 'my_melody_gif2.png']
images = []
for filename in filenames:
    try:
        print(f"📸 Loading {filename}...")
        images.append(iio.imread(filename))
        print(f"✅ Successfully loaded {filename}")
    except Exception as e:
        print(f"❌ Error loading {filename}: {e}")

print(f"🖼️  Total images loaded: {len(images)}")
print("🎞️  Creating GIF...")
iio.imwrite('team.gif', images, duration=500, loop=0)
print("🎉 GIF 'team.gif' created successfully!")
