from flask import Flask, render_template, request

app = Flask(__name__)

surveys = [
    {
        'question': 'Quelle équipe a remporté la Coupe du Monde 2018 ?',
        'options': ['France', 'Croatie', 'Brésil'],
        'answer': 0  # France                                                                                                                                                                                                                                                 \                                                                                                             

    },
    {
        'question': 'Qui est le meilleur buteur de l\'histoire de la Coupe du Monde ?',
        'options': ['Pelé', 'Ronaldo', 'Miroslav Klose'],
        'answer': 2  # Miroslav Klose                                                                                                                                                                                                                                         \                                                                                                             

    },
    {
        'question': 'Où se déroulera la Coupe du Monde 2022 ?',
        'options': ['Qatar', 'Russie', 'Brésil'],
        'answer': 0  # Qatar                                                                                                                                                                                                                                                  \                                                                                                             

    },
    {
         'question': 'Qui est le meilleur buteur de tout les temps au psg?',
        'options': ['Kylian Mbappe', 'Zlatan Ibrahimovic', 'Edinson cavani'],
        'answer': 0  # Kylian Mbappe                                                                                                                                                                                                                                                  \

    },
    {
        'question': 'Quelle est la nationnalité de Novak Djokovic?',
        'options': ['Serbe', 'Allemand', 'Espagnol'],
        'answer': 0  # Serbe                                                                                                                                                                                                                                                           \
    },
    {
        'question': 'Qui a remporté le Ballon d\'Or 2021 ?',
        'options': ['Lionel Messi', 'Cristiano Ronaldo', 'Mohamed Salah'],
        'answer': 0  # Lionel Messi
    },
    {
        'question': 'Quelle équipe a remporté la Ligue des champions de l\'UEFA 2021 ?',
        'options': ['Chelsea', 'Manchester City', 'Real Madrid'],
        'answer': 0  # Chelsea
    },
    {
        'question': 'Qui est le recordman de victoires en Grand Chelem en tennis masculin ?',
        'options': ['Roger Federer', 'Rafael Nadal', 'Novak Djokovic'],
        'answer': 2  # Novak Djokovic
    },
    {
        'question': 'Qui est le joueur de basketball le plus titré en NBA ?',
        'options': ['Michael Jordan', 'Kareem Abdul-Jabbar', 'Bill Russell'],
        'answer': 2  # Bill Russell
    },
    {
        'question': 'Quel est le plus grand stade de football du monde en capacité ?',
        'options': ['Camp Nou (Barcelone)', 'Maracanã (Rio de Janeiro)', 'Rungrado May Day (Pyongyang)'],
        'answer': 2  # Rungrado May Day (Pyongyang)
    },
    {
        'question': 'Qui a détenu le record du monde du saut en hauteur masculin pendant plus de 20 ans ?',
        'options': ['Javier Sotomayor', 'Stefan Holm', 'Jesse Owens'],
        'answer': 0  # Javier Sotomayor
    },
    {
        'question': 'Quel pays a remporté le plus de médailles d\'or aux Jeux olympiques d\'été 2016 ?',
        'options': ['États-Unis', 'Chine', 'Royaume-Uni'],
        'answer': 0  # États-Unis
    },
    {
        'question': 'Qui est le joueur de football le plus cher de l\'histoire ?',
        'options': ['Kylian Mbappé', 'Neymar Jr.', 'Paul Pogba'],
        'answer': 1  # Neymar Jr.
    },
    {
        'question': 'Quelle équipe a remporté la Coupe du Monde de la FIFA 2006 ?',
        'options': ['Italie', 'France', 'Brésil'],
        'answer': 0  # Italie
    },
    {
        'question': 'Qui est le premier athlète à avoir couru le marathon en moins de deux heures ?',
        'options': ['Eliud Kipchoge', 'Kenenisa Bekele', 'Mo Farah'],
        'answer': 0  # Eliud Kipchoge
    },
    {
        'question': 'Quel est le record du monde du 100 mètres masculin ?',
        'options': ['9,58 secondes', '9,63 secondes', '9,69 secondes'],
        'answer': 0  # 9,58 secondes
    },
    {
        'question': 'Quel pays a remporté le plus de médailles aux Jeux olympiques d\'hiver 2018 ?',
        'options': ['Norvège', 'Allemagne', 'Canada'],
        'answer': 0  # Norvège
    }
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html', surveys=surveys)

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        total_score = len(surveys) * 10  # Chaque question vaut 10 points
        score = 0
        responses = {}
        for index, question in enumerate(surveys):
            user_answer = request.form.get(question['question'])
            correct_answer = question['options'][question['answer']]
            if user_answer == correct_answer:
                score += 10;
           
            responses[question['question']] = user_answer

        if score >= 140:
            level = "Légende"
        elif score <= 30:
            level = "Null"
        elif score <= 50:
            level = "Amateur"
        elif score <= 100:
            level = "Normal"
        else:
            level = "Star"

        return render_template('results.html', score=score, total_score=total_score, responses=responses, level=level)
    else:
        return render_template('survey.html', questions=surveys)

if __name__ == '__main__':
    app.run(debug=True)
