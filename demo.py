import jinja2
from jinja2 import Environment, FileSystemLoader
environment = Environment(loader=FileSystemLoader("."))

results_filename = "demo.html"
results_template = environment.get_template("template.html")

results = []
for i in range(10):
    if i % 3:
        expected = 'FAILED'
        expected_color = 'text-danger'
    else:
        expected = 'SKIPPED'
        expected_color = 'text-warning'
    results.append({
        'index': i,
        'name': 'pepe_{0}'.format(i),
        'actual': {
            'text': 'PASSED',
            'class': 'text-success'
        },
        'expected': {
            'text': expected,
            'class': expected_color
        },
        # 'img': {
        #     'actual': 'img/demo/bliss.jpg',
        #     'expected': 'img/demo/bliss.jpg',
        #     'diff': 'img/demo/bliss.jpg',
        # }
        'img': {
            'actual': 'img/demo/bliss.jpg',
            'expected': 'img/demo/bliss.jpg',
            'diff': 'img/demo/bliss.jpg',
        }
    })


context = {
    "titleText": 'Results',
    "documentation": 'https://github.com/curtisrlee/SimpleReportGen',
    "tests": [
        {
            'name': 'Test 1',
            'results': results
        },
        {
            'name': 'Test 2',
            'results': results
        },
        {
            'name': 'Test 3',
            'results': results
        },
    ],
}

with open(results_filename, mode="w", encoding="utf-8") as results:
    results.write(results_template.render(context))
    print(f"... wrote {results_filename}")