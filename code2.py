cap = cv2. VideoCapture(video_path) # відкриває відео для читання
frames = [] # список для збереження кадрів
max_frames = 30 # 30 кадрів для прикладу обмеження

# читання відео покадрово, зберігає в frames
while len(frames) < max_frames:
ret, frame = cap. read()
if not ret:
break
frames. append (frame) 

cap. release() # звільняє ресурс відео
print(f"✅ Зчитано кадрів: {len (frames) }") # показує скільки кадрів зчитано
