# Configuration (optional)

You can change some of the default behavior of MV-Components by creating and modifying its configuration file.&#x20;

New projects do not have a configuration file. To generate a configuration file we run the following command. <mark style="color:red;">`python craft mv-component:config`</mark> This command generates a file <mark style="color:red;">`config/mv_component.py`</mark>

{% code title="config/mv_component.py" %}
```python
MVComponent = {
    ...
}
```
{% endcode %}

Currently, only two (2) configurations are supported.&#x20;

<mark style="color:red;">`PATH`</mark> which sets the location of the components directory within the templates folder. This field accepts a <mark style="color:red;">`string`</mark>.&#x20;

<mark style="color:red;">`ANNOTATE`</mark> which wraps your component with a html comment marking the beginning and end of the component. Should be set as false in production environment. This field only accepts <mark style="color:red;">`True`</mark> or <mark style="color:red;">`False`</mark>.

