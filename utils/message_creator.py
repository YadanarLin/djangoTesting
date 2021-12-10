from line_bot.models import TrainInfo

def create_single_text_message(message):
    if message=='thank you':
        message='welcome!'
    test_message=[
        {
            'type' : 'text',
            'text' : message
        }
    ]
    return test_message

test=TrainInfo(id=123,railway='Test',operator='Testing',information='Normal')
#print(models.TrainInfo.objects.all())
test.save()