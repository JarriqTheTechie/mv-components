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

. We will render first using they typical jinja pattern then using the Masonite View Component way.&#x20;

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

#### Masonite View Component Pattern

{% code title="templates/cars/index.html" %}
```html
<x-CarComponent collection="cars" cars={{ cars }}/>
```
{% endcode %}
