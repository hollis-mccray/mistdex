import json, pprint

class options():
    def __init__(self):
        self.games = []
        self.sources = {}
        self.load()

    def load(self):
        with open("data/sources.json") as infile:
            json_data = infile.read()
            sources = json.loads(json_data)
            for system in sources["games"]:
                game = Game(system["name"])
                self.games.append(game)
                for source in system["sources"]:
                    option = game.add_source(source["name"], source["active"])
                    self.sources[source["name"]] = option

    def save(self):
        game_data = [game.toJSON() for game in self.games]
        data = {
            "games": game_data
        }
        with open("data/sources.json", "w") as outfile:
            outfile.write(json.dumps(data,indent=4))

    def menu(self):
        choice = '?'
        while choice not in ['x', 'X']:
            sources = {}
            print()
            print("Sources:")
            print()
            i = 1
            for game in self.games:
                print(game.name)
                for source in game.sources:
                    print(f"{i:>3}. {source.menu_text()}")
                    sources[str(i)] = source
                    i += 1
                print()
            print("X. Main menu")
            print()
            choice = input("Select an Option: ")
            if choice in sources:
                sources[choice].toggle()
        self.save()


class Game():
    def __init__(self, name: str):
        self.name = name
        self.sources = []

    def add_source(self, name, active):
        source = Source(name, active)
        self.sources.append(source)
        return source

    def toJSON(self):
        source_data = [source.toJSON() for source in self.sources]
        data = {
            "name": self.name,
            "sources": source_data,
        }
        return data

class Source():
    def __init__(self, name: str, active:bool):
        self.name = name
        self.active = active

    def toJSON(self):
        data = {
            "name": self.name,
            "active": self.active,
        }
        return data

    def menu_text(self):
        if self.active:
            return f"[*] {self.name}"
        else:
            return f"[ ] {self.name}"

    def toggle(self):
        self.active = not self.active