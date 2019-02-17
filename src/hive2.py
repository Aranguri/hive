from src.interactive_conditional_samples import interact_model
from src.generate_unconditional_samples import sample_model

'''
Categories
* fact:
    * category: 'fact'
    * text format: a topic, related facts
* verify:
    * category: 'verify'
    * text format: an statement (eg, )
    * description:
* opinion
    * category: 'opinion'
    * text format: a topic (eg, climate change, immigration) or a question (eg is cybersecurity good?)
    * description: ask for public opinion in a topic
* topic:
    * category: 'topics'
    * text format: an array with topics (eg, ['real estate', 'houses', 'mortgage'])
    * description: it will return similar topics.
'''

def model_wrapper(category, text):
    if category == 'fact':
        pass
    elif category == 'verify':
        pass
    elif category == 'opinion':
        text = f'What do people think about {text}? What is your opinion on {text}? What are common beliefs on {text}?'
        length = 100
    elif category == 'topic':
        # text = f'Tell me a topic related to {text[0]}. What is a similar subject to {text[1]}?'
        text = ', '.join(text)
        text = f'{text}, '
        length = 10

    text = interact_model(text, nsamples=1, batch_size=1, length=length, top_k=10000)

    if category == 'fact':
        pass
    elif category == 'verify':
        pass
    elif category == 'opinion':
        pass
    elif category == 'topic':
        text = text.replace(', and', ', ')
        text = text.replace(' and ', ', ')
        text = text.replace('.', ',')
        topics = text.split(', ')
        topics = topics[:-1]
        text = ', '.join(topics)
        text = text.replace('\xa0', '')
        text = text.replace('etc', '')
        text = text.replace('.', '')

# interact_model('apa la papa', nsamples=100, batch_size=1, length=128, top_k=100)
for _ in range(3):
    print(model_wrapper('topic', ['mortgage', 'landed property', 'immoveables', 'real estate']))
    # print(model_wrapper('opinion', ['mortgage', 'landed property', 'immoveables', 'real estate']))
