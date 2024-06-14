from django.shortcuts import render, get_object_or_404
from .models import Document
import markdown
from .markdown_extensions import makeExtension

def document_detail(request, slug):
    document = get_object_or_404(Document, slug=slug)
    
    # Convert Markdown content to HTML
    md = markdown.Markdown(extensions=[makeExtension()])
    document.content = md.convert(document.content)
    
    # Render the template with the document and sidebar data
    sidebar_data = get_sidebar_data()
    return render(request, 'documentation/document_detail.html', {
        'document': document,
        'sidebar_data': sidebar_data,
    })

def get_sidebar_data():
    categories = Document.objects.values_list('category', flat=True).distinct()
    sidebar_data = {}
    for category in categories:
        documents = Document.objects.filter(category=category)
        sidebar_data[category] = list(documents)
    return sidebar_data
