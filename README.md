---
description: >-
  A framework to create reusable server rendered view components with low
  coupling and easy testability.
---

# Installation

#### Install masonite-view-components

```
pip install masonite-view-components
```

#### **Add to Masonite application**

In your `app/providers/__init__.py` file add the following import



{% code title="app/providers/__init__.py" %}
```python
from masonite_view_components.MasoniteViewComponentProvider import MasoniteViewComponentProvider
```
{% endcode %}



In your `config/providers.py` file add the following import and add `MasoniteViewComponentProvider` to your list of **PROVIDERS**

```python
from app.providers import MasoniteViewComponentProvider
```

