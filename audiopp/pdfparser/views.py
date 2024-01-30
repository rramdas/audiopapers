from django.shortcuts import get_object_or_404, render
from .models import Paper
from django.views.generic import ListView
from .forms import PaperForm


def create_paper(request):
    new_paper = None

    if request.method == 'POST':

        paper_form = PaperForm(request.POST, request.FILES)

        if paper_form.is_valid():
            # create a new paper object but avoid saving it yet
            new_paper = paper_form.save(commit=False)

            # set the pdf field of the new paper to the uploaded file
            new_paper.pdf = request.POST['pdf']
            new_paper.title = request.POST['title']

            # now save the paper object
            new_paper.save()

            return render(request, 'paper_list.html', {'form': paper_form})
    else:
        form = PaperForm()
    return render(request, 'create.html', {'form': form})


def paper_list(request):
    papers = Paper.objects.all()
    return render(request,
                  'paper_list.html',
                  {'papers': papers})


def paper_detail(request, paper_id):
    paper = get_object_or_404(Paper, pk=paper_id)
    return render(request,
                  'paper_detail.html',
                  {'paper': paper})


def download(request, paper_id):
    paper = get_object_or_404(Paper, pk=paper_id)
    file_path = os.path.join(settings.MEDIA_ROOT, paper.pdf.name)
    return render(request,
                  'download.html',
                  {'paper': paper})

class PaperListView(ListView):
    queryset = Paper.objects.all()
    context_object_name = 'papers'
    paginate_by = 10
    template_name = 'paper_list.html'
