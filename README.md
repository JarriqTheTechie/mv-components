
  
# masonite-view-components
A framework to create reusable server rendered view components with low coupling and easy testability.    
    
    
    
    
## Requirements    
1. Python 3.6+    
2. Masonite Framework or Flask
    
## Installation    
    
     pip install masonite-view-components
     or 
     https://github.com/JarriqTheTechie/masonite-view-components.git 


## How to Add to your Project  (Masonite)  
In your `app/providers/__init__.py` file add the following import

    from masonite_view_components.MasoniteViewComponentProvider import MasoniteViewComponentProvider
<br>
In your `config/providers.py` file add the following import and add `MasoniteViewComponentProvider` to your list of **PROVIDERS**

    from app.providers import MasoniteViewComponentProvider   


## How to Add to your Project  (Flask)  
    
    from masonite_view_components import MasoniteViewComponent, render_inline

	app = Flask(__name__)
	MasoniteViewComponent(app)
	MASONITE_VIEW_COMPONENT_ANNOTATE = True # or False to disable annotation


## Making Components 
Components read from the following directory of your project.    
`templates/components`    

Components require two files to be created.     
1. FooComponent.html eg. `NameComponent.html` 
2. FooComponentComponent.py eg. `NameComponent.py` 
<hr> 
*templates/components/NameComponent.py*    

     class NameComponent:      
	     def __init__(self, name):      
	         self.name= name    

<hr> 
   
*templates/components/NameComponent.html*    
 

    <h1>{{ name }}</h1>    

 
      
## Using the Components    
masonite_view_componentsComponents can be used in any of the following ways.     
    
Calling the render method from Jinja template. eg.    
*templates/index.html* 

    <x-NameComponent name="Jane Doe"/> 

   
 <hr>    
    
In a controller you can render the masonite_view_componentsComponents by returning the component using the following syntax.    

    from masonite_view_components import render_inline
    return render_inline('<x-NameComponent name="Jane Doe"/> ')    

 
## Parameters 
### Passing Parameters    
Underneath the hood, components are simply python classes with a matching html template. Parameters are passed to the __init__ function of the component class.     
    
For example, lets use our NameComponent which has the "name" instance variable. Here's how we would pass a name to the component.     
    
    <x-NameComponent name="Jane Doe"/> 

    
    
## Properties    
Components pass data to instance variables of the component class.    
    

    import random    
    class ButtonComponent: 
	    def __init__(self, text, variant="danger"): 
		    self.text = text 
		    self.variant = random.choice(["primary", "success", "danger", "warning", "info", "secondary"])    
    
    
## Nested Components 
Component nesting is supported and doesn't require subclassing in the .py file. This can be done entirely in the .html component file.    
    
## API    
#**render()** Render a component in a template    
    
`<x-ProductComponent name="Gatorade" price=2.25/>`  
<hr>    
    
#**render_inline()** Returning the string representation of a component    
    
 `render_inline('<x-ProductComponent name="Gatorade", price=2.25/>')`  
<hr>     
    
#**render_with_collection()** Render a component for each element in a collection    
*sample collection*  
 
 `fruit = [{"name": "apple", "vendor": "Super Value"}, {"name": "grapes", "vendor": "Buy for Less"}, {"name": "banana", "vendor": "Cost Right"}]`    
    
 

    <x-FruitPickerComponent collection="fruit" fruit=fruit/>  

  
This replaces `{% for fruit in fruits %}{% endfor %}`    
<hr>     
    
#**render_if()** Determine whether the component should render    
If the result of the .render_if() method is False then the component will not render.     
    
    class ListComponent:       
	    with_collection_parameter = "fruit"      
              
		def __init__(self, fruit, fruit_counter=int):        
			self.fruit = fruit      
            self.fruit_counter = ""      
              
	        def render_if(self):      
	            return self.fruit["name"] == "grapes"   
<hr> 
 
 ## Roadmap 
Component Create Commands <br>
Visual Studio Code Language Extension <br>
Component Previewer <br>
