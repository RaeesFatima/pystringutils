from pystringutils import to_snake_case, to_upper_case, to_lower_case, to_kebab_case, to_pascal_case, to_camel_case

def test_to_snake_case():
    assert to_snake_case("Hello World!") == "hello_world_"

def test_to_upper_case():
    assert to_upper_case("Hello World!") == "HELLO WORLD!"

def test_to_lower_case():
    assert to_lower_case("Raees fatima") == "raees Fatima"

def test_to_kebab_case():
    assert to_kebab_case("Raees fatima") == "raees-fatima"

def test_to_pascal_case():
    assert to_pascal_case("raees fatima") == "RaeesFatima"

def test_to_camel_case():
    assert to_camel_case("raees fatima") == "raeesFatima"