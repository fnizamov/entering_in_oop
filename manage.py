from main.scripts import Response, Parsing


categories = {
    "monitors": 'monitory_bishkek'
}

response = Response(category=categories["monitors"])
parsing = Parsing(response=response)

parsing.build()
