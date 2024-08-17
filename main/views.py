from django.shortcuts import render

# Create your views here.
def main_view(request):
    if request.method == 'POST':
        noun = request.POST.get('noun', '')
        verb = request.POST.get('verb', '')
        adjective = request.POST.get('adjective', '')
        adverb = request.POST.get('adverb', '')
        combined_sentence = f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!"

        return render(request, 'index.html', {'combined_sentence': combined_sentence})
    
    return render(request, 'index.html')