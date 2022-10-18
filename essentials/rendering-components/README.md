# Rendering Components

### Inline Components

The basic way to render components is using the following syntax.&#x20;

```html
<mv-Button/>
```

#### Additional Content / Slots

In the previous example we've used a component with self-closing syntax. But what if we wanted to pass additional content to the component? We would use the following syntax.&#x20;

```html
<mv-Button>Click Me</mv-Button>
```

The text "click me" is now available within the component view using the variable <mark style="color:red;">`content`</mark>.

Our component view would look as follows.&#x20;

<pre class="language-django" data-title="Button.html"><code class="lang-django"><strong>&#x3C;button class="btn btn-primary">{{ content }}&#x3C;/button></strong></code></pre>
