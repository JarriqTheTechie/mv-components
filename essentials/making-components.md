# Making Components

Components provide a way to encapsulate logic and layouts. Additionally, they provide a way to keep code organized and reusable. In masonite-view-components we have two kinds of components.&#x20;

1. Anonymous Components
2. Class-based Components



### Class-based Components

To create a class-based component, you can use the following command. <mark style="color:red;">`python craft mv-component:make`</mark> <mark style="color:red;"></mark><mark style="color:red;">.</mark> The command takes one argument which is the name of the component. To illustrate we will create a trivial Button component.

```
python craft mv-component:make Button
```

Running the command creates two files within your component's directory. The files are stored as <mark style="color:red;">`templates/components/Button.py`</mark> & <mark style="color:red;">`templates/components/Button.html`</mark>. By default, the components directory is <mark style="color:red;">`templates/components`</mark>. This behavior can be changed but that will be discussed later.&#x20;

### Anonymous Components

Anonymous components are simple html files within the component's directory. Anonymous components have no matching python class files.



