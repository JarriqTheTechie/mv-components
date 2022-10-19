---
description: >-
  A framework to create reusable server rendered view components with low
  coupling and easy testability.
---

# Installation

#### Install mv-components

```bash
pip install mv-components
```

#### **Add to Masonite application**

In your `app/providers/__init__.py` file add the following import

{% code title="app/providers/__init__.py" %}
```python
from mv_components.MVComponentProvider import MVComponentProvider
```
{% endcode %}



In your `config/providers.py` file add the following import and add `MVComponentProvider` to your list of **PROVIDERS**

```python
from app.providers import MVComponentProvider
```

