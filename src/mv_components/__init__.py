from .Exceptions import *
from typing import Any, Dict
from markupsafe import Markup
from jinja2 import Environment
from pydoc import locate

# Import Web Framework (Masonite or Flask)
try:
    from masonite.views import View
except ModuleNotFoundError:
    from flask import Flask, render_template_string, render_template


def config_loader() -> str:
    """
        Gets component directory from mv_component config file. Fallback to "components" directory in
        templates folder.
    return:
        str
    """
    COMPONENTS_DIR: str
    try:
        from config.mv_component import MVComponent
        COMPONENTS_DIR = MVComponent.get('PATH')
        return COMPONENTS_DIR
    except:
        COMPONENTS_DIR = "components"
        return COMPONENTS_DIR


def render_inline(jinja: str, **kwargs: Dict[str, Any]) -> str:
    """
        Renders component without supplying a template file. Usage example.

        return render_inline('<mv-ExampleComponent/>')

    return:
        str
    """
    env = Environment()
    env.add_extension('mv_components.mv_component_ext.MVComponentExt')
    kwargs = {**kwargs, **_render(), **_render_with_collection()}
    tmpl = env.from_string(f'{jinja}')
    output = Markup(tmpl.render(**kwargs))
    if output.startswith("{") and output.endswith("}"):
        tmp = Markup(f"{output}".lstrip("{").rstrip("}"))
        return env.from_string(f'{{{jinja}}}').render(**kwargs)
    return Markup(output)


def annotate_checker() -> bool:
    """
        Provides annotation for components. In html markup a comment string is added before and after the component.
        Annotation contains the name and directory of the component.
        <!-- BEGIN components/ExampleComponent/ExampleComponent.html -->

        <!-- End components/ExampleComponent/ExampleComponent.html -->

    return:
        bool
    """
    MV_COMPONENT_ANNOTATE: bool
    try:
        from config.mv_component import MVComponent
        MV_COMPONENT_ANNOTATE = MVComponent.get('ANNOTATE')
    except:
        MV_COMPONENT_ANNOTATE = False
    return MV_COMPONENT_ANNOTATE


def to_class(path: str) -> Any:
    """
        Converts string class path to a python class

    return:
        mixed
    """
    try:
        class_instance = locate(path)
    except ImportError:
        print('Module does not exist')
    return class_instance or None


def component_html_path(component: str) -> str:
    """
        Locates component html directory.

    return:
        str
    """
    if "." in component:
        component_ = component.split('.')[1]
        component_folder = component.split('.')[0]
        template_path = f'{config_loader()}/{component_folder}/{component_}.html'
    else:
        template_path = f'{config_loader()}/{component}.html'
    return template_path


def component_class_path(component: str) -> str:
    """
        Locates component python class directory.

    return:
        str
    """
    if "." in component:
        component_ = component.split('.')[1]
        component_folder = component.split('.')[0]

        component_py_path = f"templates.{config_loader()}.{component_folder}.{component_}.{component_}"
    else:
        component_py_path = f"templates.components.{component}.{component}"
    return component_py_path


def render_if(component_class: Any) -> Any:
    """
        Implementing a render_if function on a component class determines whether a component should render.

    return:
        mixed
    """
    try:
        render_if = component_class.render_if
    except AttributeError:
        render_if = lambda: None
    return render_if


def _render() -> Dict[str, Any]:
    def render(component: str, **kwargs: Dict[str, Any]) -> str:

        """
            Render a component.

        return:
            str
        """
        component = component.replace("mv-", "")
        content = ""
        if "caller" in kwargs:
            content = {"content": kwargs.get('caller')()}
            kwargs.pop('caller')
        component_class = to_class(component_class_path(component))(**kwargs)

        if render_if(component_class)() is True or render_if(component_class)() is None:
            arguments_from_component = component_class.__dict__
            try:
                arguments_from_component = kwargs
                if arguments_from_component:
                    payload = {**arguments_from_component, **component_class.__dict__, **content}
                else:
                    payload = component_class.__dict__
                template = render_template(component_html_path(component), **payload)
            except NameError:
                from masonite.facades import View
                from masonite.helpers import compact
                template = View.render(component_html_path(component), arguments_from_component).get_content()

            if annotate_checker() is True:
                comment_start = f"<!-- BEGIN {component_html_path(component)} --> \n"
                comment_end = f"\n <!-- END {component_html_path(component)} --> "
                return render_inline(comment_start + template + comment_end)
            else:
                return render_inline(template)
        else:
            return ""
    return dict(render=render)


def _render_with_collection() -> Dict[str, Any]:
    def render_with_collection(component: str, collection: str, **kwargs: Dict[str, Any]) -> str:
        """
            Render a component for each element in a collection. To use the feature, with_collection_parameter must be
            set on the component class. The value of this parameter should be the variable name of the collection in
            the class __init__ function.

            Example usage:

            class ExampleComponent:
                with_collection_parameter = "example"

                def __init__(self, example):
                    self.example = example # or some other call to a list or repository.


            In the view/template you can use it as follows.

            <mv-ExampleComponent collection="example" example={{ examples }} />

        return:
            str
        """
        component = component.replace("mv-", "")
        content = ""
        if "caller" in kwargs:
            content = {"content": kwargs.get('caller')()}
            kwargs.pop('caller')
        component_class = to_class(component_class_path(component))(**kwargs)
        arguments_from_component = component_class.__dict__

        results = ""
        try:
            for n in range(len(component_class.__dict__[f"{collection}"])):
                if f"{collection}_counter" in component_class.__dict__:
                    component_class.__dict__[f"{collection}_counter"] = n + 1
                arguments = {**component_class.__dict__, **{f"{collection}": arguments_from_component[collection][n]}, **content}
                scoped_class = component_class
                scoped_class.__dict__ = arguments
                if render_if(component_class)() is True or render_if(component_class)() is None:
                    try:
                        template = render_template(component_html_path(component), **arguments)
                    except NameError:
                        from masonite.facades import View
                        from masonite.helpers import compact
                        template = View.render(component_html_path(component), arguments).get_content()
                    if annotate_checker() is True:
                        comment_start = f"<!-- BEGIN {component_html_path(component)} --> \n"
                        comment_end = f"\n <!-- END {component_html_path(component)} --> "

                        results += f"{comment_start} {template} {comment_end}"
                    else:
                        results += template
                else:
                    results += ""
            return render_inline(results)
        except TypeError:
            return render_inline(results)
    return dict(render_with_collection=render_with_collection)


def MVComponent(app) -> Any:
    try:
        app.jinja_env.add_extension('mv_components.mv_component_ext.MVComponentExt')
        app.context_processor(_render)
        app.context_processor(_render_with_collection)
    except:
        pass

