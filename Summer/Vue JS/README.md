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

We can access the title property in our HTML but if we wanted our function sayHello to access the title property, we would have to use this.title since we are working within the Vue instance.

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
            return this.title;
        }
    }
});
```

### Binding to Attributes

The dude adds a link property in data. He makes an anchor tag and tries to pass in the link. It fails because you can't use the {{ }} syntax for HTML element attributes.

```
<a href="{{ link }}">Google</a> // will not work
```

To bind the link property you have to use a directive called v-bind. We don't need the {{}} because we're using a Vue directive

```
<a v-bind:href="link">Google</a>
```

### Understanding and Using Directives

A directive is basically an instruction you place in your code. VueJS ships with a few built-in directives that cover a good amount of use cases. You can also write your own directives.

```
<a v-bind:href="link">Google</a>
```

- v-bind tells us to bind something to the data
- After the colon you put the attribute you are binding to

### Disable Re-rendering with v-once

The dude adds an h1 {{ title }}. Without v-once, the code will print out 'Hello' twice. Once as the h1 title and again in the p tag. When the title property is changed in sayHello, all usages of title are re-rendered. To keep the first title to remain 'Hello World' we can use v-once so it doesn't re-render.

```
HTML
<script src="https://unpkg.com/vue/dist/vue.js">
</script>

<div id="app">
    <h1 v-once>{{ title }}</h1> 
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
            this.title = 'Hello';
            return this.title;
        }
    }
});
```

### How to Output Raw HTML

The guy adds the raw HTML code for the link to the Vue instance. By default VueJS escapes HTML and only renders text, which is good to avoid cross-side scripting. To render HTML content, you need to use a directive called v-html.

```
HTML
<script src="https://unpkg.com/vue/dist/vue.js">
</script>

<div id="app">
    <h1 v-once>{{ title }}</h1> 
    <p>{{ sayHello() }} - <a v-bind:href="link">Google</a></p>
    <hr>
    <p v-html="finishedLink"></p>
</div>
```

```
JS

new Vue({
    el: '#app',
    data: {
        title: 'Hello World',
        link: 'http://google.com',
        finishedLink: '<a href="http://google.com">Google</a>'
    },
    methods: {
        sayHello: function() {
            this.title = 'Hello';
            return this.title;
        }
    }
});
```

### Assignment: Outputting Data to Templates
- print out name and age using string interpolation
- function to triplE age
- generate a random number
- bind image to src


```
HTML
<script src="https://unpkg.com/vue/dist/vue.js"></script>

<div id="exercise">
   <!-- 1) Fill the <p> below with your Name and Age - using Interpolation -->
    <p>VueJS is pretty cool - {{ name }} ({{ age }})</p>
    <!-- 2) Output your age, multiplied by 3 -->
    <p>{{ age*3 }}</p>
    <!-- 3) Call a function to output a random float between 0 and 1 (Math.random()) -->
    <p>{{ randNum() }}</p>
    <!-- 4) Search any image on Google and output it here by binding the "src" attribute -->
    <div>
        <img v-bind:src="link" style="width:100px;height:100px">s
    </div>
    <!-- 5) Pre-Populate this input with your name (set the "value" attribute) -->
    <div>
        <input type="text" v-bind:value="name">
    </div>
</div>
```
```
JS

new Vue({
	el: '#exercise',
  data: {
  	name: 'Suhavi',
    age: 22,
    link: "https://pngimg.com/uploads/cactus/cactus_PNG23623.png"
  }, 
  methods: {
    randNum: function() {
    	return Math.random()*100;
    }
  }
});
```

### Listening to Events