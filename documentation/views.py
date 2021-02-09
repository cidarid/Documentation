from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import os
import mammoth
import shutil

from .models import Documentation, Category, Document
from documentation.forms import DocForm, CategoryForm, DocumentForm


# Displays the homepage, lists all categories
def index(request):
    # Creates a default category to use
    if Category.objects.count() <= 0:
        Category.objects.create(name="Uncategorized")
    return render(request, 'documentation/index.html')


# Displays all of the documentation inside of a specific category
def category_view(request, cat_slug, cat_pk):
    category = get_object_or_404(Category, pk=cat_pk)
    docs_in_category = Documentation.objects.filter(category=category)
    return render(request, 'documentation/category.html', {
        'category': category,
        'docs_in_category': docs_in_category,
    })


# Change category name
def edit_category(request, cat_slug, cat_pk):
    if request.method == 'POST':
        c = get_object_or_404(Category, pk=cat_pk)
        c.name = request.POST['name']
        c.save()
        return HttpResponseRedirect(c.get_absolute_url())
    category = get_object_or_404(Category, pk=cat_pk)
    form = CategoryForm(initial={
        'name': category.name,
    })
    return render(request, 'documentation/edit_category.html', {
        'form': form,
        'category': category,
    })


# Displays a specific piece of documentation
def detail(requests, cat_slug, doc_slug, cat_pk, doc_pk):
    category = get_object_or_404(Category, pk=cat_pk)
    documentation = get_object_or_404(Documentation, pk=doc_pk, category=category)
    return render(requests, 'documentation/detail.html', {
        'category': category,
        'documentation': documentation,
    })


# Handles editing documentation
def edit(requests, cat_slug, doc_slug, cat_pk, doc_pk):
    if requests.method == 'POST':
        category = get_object_or_404(Category, pk=cat_pk)
        d = get_object_or_404(Documentation, pk=doc_pk, category=category)
        d.doc_title = requests.POST['doc_title']
        d.doc_text = requests.POST['doc_text']
        d.category = Category.objects.get(id=requests.POST['category'])
        d.date_modified = timezone.now()
        d.save()
        return HttpResponseRedirect(d.get_absolute_url())
    category = get_object_or_404(Category, pk=cat_pk)
    documentation = get_object_or_404(Documentation, pk=doc_pk, category=category)
    form = DocForm(initial={
        'doc_title': documentation.doc_title,
        'doc_text': documentation.doc_text,
        'category': documentation.category,
    })
    return render(requests, 'documentation/edit.html', {
        'form': form,
        'documentation': documentation,
    })


# Handles creating new documentation
def new(request):
    if request.method == 'POST':
        d = Documentation(
            doc_title=request.POST['doc_title'],
            doc_text=request.POST['doc_text'],
            category=Category.objects.get(id=request.POST['category']),
            date_modified=timezone.now(),
            doc_type=Documentation.WRITTEN,
            date_published=timezone.now()
        )
        d.save()
        return HttpResponseRedirect(reverse('documentation:index'))
    form = DocForm()
    return render(request, 'documentation/new_documentation.html', {
        'form': form,
        'latest_category_list': Category.objects.all(),
    })


# Handles creating new categories
def new_category(request):
    if request.method == 'POST':
        c = Category(name=request.POST['name'])
        c.save()
        return HttpResponseRedirect(reverse('documentation:index'))
    form = CategoryForm()
    return render(request, 'documentation/new_category.html', {
        'form': form,
    })


# Handles uploading of files
def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            new_doc = Document(doc_file=request.FILES['doc_file'])
            new_doc.save()
            documentation = handle_uploaded_file(new_doc, request.POST)
            documentation.save()
            return HttpResponseRedirect(documentation.get_absolute_url())
    else:
        form = DocumentForm(initial={'category': Category.objects.get(pk=1)})

    documents = Document.objects.all()
    return render(request, 'documentation/upload.html', {'documents': documents, 'form': form})


def handle_uploaded_file(document, post):
    d = Documentation(
        doc_title=post['title'],
        doc_text="",
        category=Category.objects.get(id=post['category']),
        doc_type=Documentation.HTML,
        date_modified=timezone.now(),
        date_published=timezone.now()
    )
    with open(f'{document.doc_file.path}', 'rb') as docx_file:
        i_w = ImageWriter(d)
        result = mammoth.convert_to_html(docx_file, convert_image=mammoth.images.inline(i_w.convert_image))
        html = result.value  # The generated Markdown
        messages = result.messages  # Any messages, such as warnings during conversion
        with open("mammoth_test.html", "w", encoding="utf-8") as f:
            f.write(html)
    d.doc_text = html

    return d


class ImageWriter(object):
    def __init__(self, documentation):
        self._static_dir = f"/static/img/upload/{documentation.slug}/"
        self._reference_dir = "documentation" + self._static_dir
        os.mkdir(self._reference_dir)
        self._image_number = 1

    def convert_image(self, image):
        extension = image.content_type.partition("/")[2]
        image_filename = f"{self._image_number}.{extension}"
        with open(os.path.join(self._reference_dir, image_filename), "wb") as image_dest:
            with image.open() as image_source:
                shutil.copyfileobj(image_source, image_dest)

        self._image_number += 1

        return {
            "src": (self._static_dir + image_filename),
            "style": "max-width:80%;"
        }
