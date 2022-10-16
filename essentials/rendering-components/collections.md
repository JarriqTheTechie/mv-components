# Collections

In typical templates you would iterate over a collection using a for loop. In our example we have a collection of cars defined in our controller which we expose to our view.&#x20;

```python
from masonite.views import View
from application.models.Cars import Cars

class CarsController(Controller):

  # Template is templates/cars/index.html
  def show(self, view: View):
    view.render('cars.index', {
    	"cars": Cars.all()
    })
```

We will render first using they typical jinja pattern then using the MV-Component way.&#x20;

#### Typical Jinja Pattern

{% code title="templates/cars/index.html" %}
```django
{% raw %}
{% for car in cars %}
    <p>{{ car.model }} / {{ car.make }}</>
{% endfor %}
{% endraw %}
```
{% endcode %}

#### MV-Component Pattern

To use this pattern, a class-based component must be created. e.g. lets make a <mark style="color:red;">`CarListComponent`</mark>&#x20;

```
python craft view-component:make CarListComponent
```

This will create two files in your components directory. In our example we will get the following files  <mark style="color:red;">`templates/components/CardListComponent.py`</mark> & <mark style="color:red;">`templates/components/CardListComponent.html`</mark>

To enable our collections feature we add a <mark style="color:red;">`with_collection_parameter`</mark> to our CardListComponent. This allows us to avoid writing a for-loop as seen above.&#x20;

#### Component

{% code title="CardListComponent.py" %}
```python
class CardListComponent:
    with_collection_parameter = "cars"
    
    def __init__(self, cars=cars):
        self.cars = cars
```
{% endcode %}

{% code title="CardListComponent.html" %}
```django
<p>{{ car.model }} / {{ car.make }}</>
```
{% endcode %}

{% code title="templates/cars/index.html" %}
```html
<x-CarListComponent collection="cars" cars={{ cars }}/>
```
{% endcode %}

#### Collection Counter

Additionally, Masonite View Components allows you to define a collection indexer/counter. This is helpful in many instances.&#x20;

```python
CardListComponent.py
class CardListComponent:
    with_collection_parameter = "cars"
    
    def __init__(self, cars=cars, cars_counter:int):
        self.cars = cars
        self.counter = cars_counter
```

In our component's html file we can now do this. &#x20;

```django
<p>{{ car.model }} / {{ car.make }} - Index #{{ counter }}</>
```
