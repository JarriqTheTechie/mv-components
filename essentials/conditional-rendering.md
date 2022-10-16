# Conditional Rendering

Components can optionally implement a <mark style="color:red;">`render_if`</mark> method which allows components to render only If the result of the <mark style="color:red;">`render_if()`</mark> method is <mark style="color:red;">`False`</mark>. Using our CarListComponent from our previous example, lets implement this.&#x20;

```python
CardListComponent.py
class CardListComponent:
    with_collection_parameter = "cars"
    
    def __init__(self, cars=cars, cars_counter:int):
        self.cars = cars
        self.counter = cars_counter
        
    def render_if(self):
        return with_collection_parameter == "trucks":
            
```

Now if we try to render our component it will not render.&#x20;
