import math

# Noktaların tanımlanması
points = []

# Kullanıcıdan noktaları alma
while True:
    point_str = input("Lütfen bir nokta girin (x,y) veya 'q' tuşuna basarak çıkın: ")
    if point_str.lower() == 'q':
        break
    try:
        x, y = map(float, point_str.split(','))
        points.append((x, y))
    except ValueError:
        print("Geçersiz giriş. Lütfen (x,y) formatında bir nokta girin.")

# Öklid Mesafesi için bir fonksiyon yazma
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması
if distances:
    min_distance = round(min(distances), 2)  # Sonucu 2 ondalık basamağa yuvarla
    print("Minimum mesafe:", min_distance)
else:
    print("Hiç nokta girilmedi.")