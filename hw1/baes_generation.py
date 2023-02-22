import pprint
import random

# возможные элементы стиля
styles = {
    'прическа':[
        'нет волос',
        'длинные в пучок',
        'длинные волнистые',
        'длинные прямые',
        'короткая волнистые',
        'короткая прямые',
        'короткая курчавые'
    ],
    'цвет волос':[
        'черный',
        'блонд',
        'каштановый',
        'пастельный розовый',
        'рыжий',
        'серебристо серый',
    ],
    'аксесуар':[
        'нет очков',
        'круглые очки',
        'солнцезащитные очки',
    ],
    'одежда':[
        'худи',
        'комбинезон',
        'футболка с круглым вырезом',
        'футболка с V-вырезом',
    ],
    'цвет одежды':[
        'черный',
        'синий',
        'серый',
        'зеленый',
        'оранжевый',
        'розовый',
        'красный',
        'белый'
    ],
}
# количество элементов стиля в наблюдаемых данных
styles_count = {
    'прическа':[
        7,
        0,
        1,
        23,
        1,
        11,
        7
    ],
    'цвет волос':[
        7,
        6,
        2,
        3,
        8,
        24,
    ],
    'аксесуар':[
        11,
        22,
        17,
    ],
    'одежда':[
        7,
        18,
        19,
        6,
    ],
    'цвет одежды':[
        4,
        5,
        6,
        8,
        6,
        8,
        7,
        6
    ],
}

assert styles.keys() == styles_count.keys(), "A number of style elements in the data differs"

style_counter_match = all(
    [
        len(list(styles.values())[i]) == len(list(styles_count.values())[i])
        for i in range(len(list(styles.keys())))
    ]
)

assert style_counter_match, "A number of counters in observations "\
    "doesn't match a number of possible values for style element at least once"

pp = pprint.PrettyPrinter()

count_per_style = {k: sum(l) for k, l in styles_count.items()}

probas_per_style_item = {
    k: list(map(lambda x: x / count_per_style[k], v))
    for k, v in styles_count.items()
}

print('Probas within each style:', end='\n')
pp.pprint(probas_per_style_item)

style_generator = {
    k: random.choices(styles[k], weights=v)[0] 
    for k, v in probas_per_style_item.items()
}

print('\nExample of new style:', end='\n')
pp.pprint(style_generator)

# Additive smoothing
# Get style parts that should be smoothed
style_need_smooting = set(
    k for k, v in styles_count.items() 
    for count in v if count == 0
)

# Update these parts
for k in style_need_smooting:
    styles_count[k] = [count + 1 for count in styles_count[k]]
    count_per_style[k] = sum(styles_count[k])
    probas_per_style_item[k] = list(
        map(lambda x: x / count_per_style[k], styles_count[k])
    )

print('\nProbas within each style, but additive smoothing edition:', end='\n')
pp.pprint(probas_per_style_item)

# Generate again
style_generator = {
    k: random.choices(styles[k], weights=v)[0] 
    for k, v in probas_per_style_item.items()
}

print('\nExample of new style:', end='\n')
pp.pprint(style_generator)