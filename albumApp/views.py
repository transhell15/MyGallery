from django.shortcuts import render, redirect

from albumApp.models import (
    Category,
    Photo,
)


# View created for Landing page
def LandingPageView(request):
    categories = Category.objects.all()

    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)
    context = {'categories': categories, "photos": photos}
    return render(request, "landing_page.html", context)


# view created for View photo page
def ViewPhotoPageView(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    context = {"photo": photo}
    return render(request, "viewphoto_page.html", context)


# View created for Add photo page
def AddPhotoPageView(request):
    categories = Category.objects.all()

    if request.method == "POST":
        images = request.FILES.getlist('images')
        description = request.POST.get('description')
        category_choice = request.POST

        if category_choice['category'] != 'none':
            category = Category.objects.get(id=category_choice['category'])
        elif category_choice['new_category'] != '':
            category, created = Category.objects.get_or_create(
                name=category_choice['new_category'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                image=image,
                description=description,
                category=category,
            )

        photo.save()
        return redirect('landing_page')

    context = {'categories': categories}
    return render(request, "addphoto_page.html", context)
