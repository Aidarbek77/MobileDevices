from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField()  # Дата выпуска
    image = models.ImageField(upload_to='device_images/')
    category = models.CharField(max_length=100)
    feature =models.CharField(max_length=100)
    features = models.ManyToManyField(feature, related_name="devices")

    def __str__(self):
        return f"{self.name} ({self.manufacturer})"

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Feature(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Review(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="reviews")
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

def add_review(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    if request.method == "POST":
        author = request.POST.get("author")
        content = request.POST.get("content")
        if author and content:
            Review.objects.create(device=device, author=author, content=content)
            return redirect('device_detail', device_id=device.id)
    return render(request, 'devices/add_review.html', {'device': device})
