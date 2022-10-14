# Rendering Components

### Inline Components

The basic way to render components is using the following syntax.&#x20;

```html
<x-Button/>
```

Alternatively, you can use the following function call within your template.&#x20;

```
{{ render('Button') }}
```

### Properties

****

**Passing Properties to components**

You can pass data to Masonite View Components using html attributes. All primitive datatypes are supported as well as custom objects.

****

**Passing values as strings**

```
<x-Button data="{{ value }}"/>.
```

****

**Passing objects**

```
<x-Button data={{ value }}/>
```
