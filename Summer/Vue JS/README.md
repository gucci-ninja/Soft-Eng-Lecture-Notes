# Vue JS

## Section 1: Getting Started

### Creating our First VueJS Application

In this part the dude wrote some code on JS Fiddle that binds to an element on the page and renders the text 'Hello World'. On input, the Hello World text changes to the input the user enters. He used the cdn link for Vue JS.

- el is the element, kind of works like a class/id selector
- {{ var }} is the syntax to render things that have been declared using a Vue instance
- v-on:input is an event that gets called when input is entered
- data stores the variables that will be accessible in the DOM
- methods stores the methods that will be accesible in the DOM
- in methods, data properties get proxied to the DOM
- you can access elements from data in methods by doing this.title for title

```
HTML
<script src="https://unpkg.com/vue/dist/vue.js">
</script>

<div id="app">
    <input type="text" v-on:input="changeTitle">
    <p>{{ title }}</p>
</div>
```

```
JS

new Vue({
    el: '#app',
    data: {
        title: 'Hello World'
    },
    methods: {
        changeTitle: function(event) {
            this.title = event.target.value;
        }
    }
});
```
### Course Structure

- Interacting with DOM using Templates
- Understanding the VueJS Instance - JSFiddle
- Vue CLI - actual setup
- Components - how to communicate between components
- Forms
- Directives, Filters, Mixins
- Animations and Transitions
- Working with Http - communicating with server
- Routing (Single Page Apps)
- State Management (SPA)
- Deploying a VueJS App

### Course Resources
- 4 projects
    1. Basics, Template Interaction
    2. Components
    3. Animations
    4. Final - Routing, State Management
- Quick exercises
- Solutions in the last lecture of each module

## Section 2: Using VueJS to Interact with the DOM

### Understanding the VueJS Template

The dude makes another app on JS Fiddle and explains the connection between the Vue instance and the HTML.

- the {{ }} syntax is also called Interpolation or String Interpolation
- Vue js does not use the html code at run time, it creates a template and stores it internally
- this code is then rendered as HTML in the DOM

### How the VueJS Template Syntax and Instance Work Together

Data stored in the Vue instance can be outputted in our template pretty easily - {{ data_object }}. You can also execute a method from the Vue instance like this - {{ method_name() }}. 

```
HTML
<script src="https://unpkg.com/vue/dist/vue.js">
</script>

<div id="app">
    <p>{{ sayHello() }}</p>
</div>
```

```
JS

new Vue({
    el: '#app',
    data: {
        title: 'Hello World'
    },
    methods: {
        sayHello: function() {
            return 'Hello';
        }
    }
});
```
### Accessing Data in the Vue Instance