from .models import MarqueeText

def marquee_text_processor(request):
    # Fetch the first marquee text or return None if it doesn't exist
    marquee_text = MarqueeText.objects.first()
    return {'marquee_text': marquee_text}
