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

The dude creates a JS FIddle with a button that increases a counter object. He uses the v-on directive, which recieves an /event/ from the Vue template.

```
HTML
<script src="https://unpkg.com/vue/dist/vue.js">
</script>

<div id="app">
    <button v-on:click="increase">Click me</button>
    <p>{{ counter }}</p>
</div>
```

```
JS

new Vue({
    el: '#app',
    data: {
        counter: 0
    },
    methods: {
        inrease: function() {
            this.counter++;
        }
    }
});
```

### Getting Event Data from the Event Object

```
HTML
<script src="https://unpkg.com/vue/dist/vue.js">
</script>

<div id="app">
    <button v-on:click="increase">Click me</button>
    <p>{{ counter }}</p>
    <p v-on:mousemove="updateCoordinates">Coordinates: {{ x }} / {{ y }}</p>
</div>
```

```
JS

new Vue({
    el: '#app',
    data: {
        counter: 0,
        x: 0,
        y: 0
    },
    methods: {
        increase: function() {
            this.counter++;
        },
        updateCoordinates: function(event) {
            this.x = event.clientX;
            this.y = event.clientY;
        }
    }
});
```

### Passing your own Arguments with Events

The dude wants to add in a parameter so the previous counter increases by sending a parameter to the increase function. He also passes his own argument as well as the event object. The naming for this second one is important - ```$event```.

```
HTML

<button v-on:click="increase(2, $event)">Click me</button>

JS

increase: function(step, event) {
    this.counter += step;
}
```

### Modifying an Event - with Event Modifiers

The dude modifies the coordinae update event by adding a dead spot so that the coordinaes don't change in a certain area. He does it first by creating a method called dummy that stops propagation of the event.

```
dummy: function(event) {
    event.stopPropagation();
}
```

Then he does it by using a modifier (.stop). It does the same thing as the dummy solution. We can also make it .stop.prevent if you want to prevent default event object. In this case it won't do anything.

```
HTML
<script src="https://unpkg.com/vue/dist/vue.js">
</script>

<div id="app">
    <button v-on:click="increase(2, $event)">Click me</button>
    <p>{{ counter }}</p>
    <p v-on:mousemove="updateCoordinates">Coordinates: {{ x }} / {{ y }}
        - <span v-on:mousemove.stop="dummy">DEAD SPOT</span></p>
</div>
```

```
JS

new Vue({
    el: '#app',
    data: {
        counter: 0,
        x: 0,
        y: 0
    },
    methods: {
        increase: function(step, event) {
            this.counter += step;
        },
        updateCoordinates: function(event) {
            this.x = event.clientX;
            this.y = event.clientY;
        }
    }
});
```

### Listening to Keyboard Events

The dude creates an alert that uses a key modifiers. It is fired whenever the user releases the key. Both space and enter key will trigger the event.


```
HTML
<script src="https://unpkg.com/vue/dist/vue.js">
</script>

<div id="app">
    <button v-on:click="increase(2, $event)">Click me</button>
    <p>{{ counter }}</p>
    <p v-on:mousemove="updateCoordinates">Coordinates: {{ x }} / {{ y }}
        - <span v-on:mousemove.stop="dummy">DEAD SPOT</span></p>
    <input type="text" v-on:keyup.enter.space="alertMe">
</div>
```

```
JS

new Vue({
    el: '#app',
    data: {
        counter: 0,
        x: 0,
        y: 0
    },
    methods: {
        increase: function(step, event) {
            this.counter += step;
        },
        updateCoordinates: function(event) {
            this.x = event.clientX;
            this.y = event.clientY;
        },
        alertMe: function() {
            alert('Alert');
        }
    }
});
```

### Assignment 2: Events

The dude wants us to show an alert when a button is clicked. Then, listen to a keydown event on an nput and store it in a data property. We would need sccess to the input field. Then, listen to keydown but only refresh the property if enter is pressed.

```
<script src="https://npmcdn.com/vue/dist/vue.js"></script>

<div id="exercise">
    <!-- 1) Show an alert when the Button gets clicked -->
    <div>
        <button v-on:click="alertMe">Show Alert</button>
    </div>
    <!-- 2) Listen to the "keydown" event and store the value in a data property (hint: event.target.value gives you the value) -->
    <div>
        <input v-on:keydown="getVal" type="text">
        <p>{{ value }}</p>
    </div>
    <!-- 3) Adjust the example from 2) to only fire if the "key down" is the ENTER key -->
    <div>
        <input v-on:keydown.enter="getVal" type="text">
        <p>{{ value }}</p>
    </div>
</div>
```

```
JS

new Vue({
    el: '#exercise',
    data: {
        value: ''
    },
    methods: {
    	alertMe: function() {
      	alert('Alert');
      },
      getVal: function(event) {
      	this.value = event.target.value;
      }
    }
});
```

### Writing JavaScript Code in the Templates

The dude tells us that we can write simple javascript statements in the template.

```
<button v-on:click="counter++">Click me</button>
<p>{{ counter  2 > 10 ? 'Greater than 10' : 'nop' }}</p>
```

### Using Two-Way-Binding

The dude tells us how to populate the name of a user but everytime it's changed, it gets updated. He uses the v-model property

```
HTML

<script src="https://npmcdn.com/vue/dist/vue.js"></script>

<div id="app">
    <input type="text" v-model="name">
    <p>{{ name }}</p>
</div>

JS

new Vue({
    el: '#app',
    data: {
        name: 'Max'
    }
})
```

### Reacting to Changes with Computed Properties

The dude has a data property ```result``` that gets updated when a button is clicked. He adds a new property, ```computed```, which allows us to store properties. Everything stored and computed can be used like a property in the data object of the Vue instance. ```computed``` will only be executed because it only runs when ```counter``` is affected. The result is not being recalculated but it is being cached. 

```
HTML

<script src="https://npmcdn.com/vue/dist/vue.js"></script>

<div id="app">
    <button v-on:click="counter++">Increase</button>
    <button v-on:click="counter--">Decrease</button>
    <button v-on:click="secondCounter++">Increase Second</button>
    <p>Counter: {{ counter }} | {{ secondCounter }}</p>
    <p>Result: {{ result() }} | {{ output }}</p>
</div>

JS

new Vue({
    el: '#app',
    data: {
        counter: 0,
        secondCounter: 0
    },
    computed: {
        output: function() {
            return this.counter > 5 ? 'greater than 5' : 'nop';
        }

    }
    methods: {
        result: function() {
            return this.counter > 5 ? 'greater than 5' : 'nop';
        }
    }
})
```

### An Alternative to Computed Properties: Waiting for Changes

Instead of using computed property, we can use the watch object. In computed we set up the property and then set up the function for how it's computed. FOr watch, you set the name of the property you want to watch (```counter```). Then you specify the code you want to execute when ```counter``` is affected. Computed properties are more optimized than watch properties. Computed properties also won't work if you need asynchronous tasks to be run. Computed properties always run immediately (synchronously).


```
HTML

<script src="https://npmcdn.com/vue/dist/vue.js"></script>

<div id="app">
    <button v-on:click="counter++">Increase</button>
    <button v-on:click="counter--">Decrease</button>
    <button v-on:click="secondCounter++">Increase Second</button>
    <p>Counter: {{ counter }} | {{ secondCounter }}</p>
    <p>Result: {{ result() }} | {{ output }}</p>
</div>

JS

new Vue({
    el: '#app',
    data: {
        counter: 0,
        secondCounter: 0
    },
    computed: {
        output: function() {
            return this.counter > 5 ? 'greater than 5' : 'nop';
        }
    },
    watch: {
        counter: function(value) {
            var vm = this;
            setTimeout(function() {
                vm.counter = 0;
            }, 2000);
        }
    }
})
```

### Saving Time with Shorthands
- replace the ```v-on:click``` with ```@click```
- ```v-bind:href``` --> ```:href```


### Assigment 3: Reactive Properties

The objective is to show a result 

```
HTML
<script src="https://npmcdn.com/vue/dist/vue.js"></script>

<div id="exercise">
    <!-- 1) Show a "result" of 'not there yet' as long as "value" is not equal to 37 - you can change "value" with the buttons. Print 'done' once you did it -->
    <div>
        <p>Current Value: {{ value }}</p>
        <button @click="value += 5">Add 5</button>
        <button @click="value += 1">Add 1</button>
        <p>{{ result }}</p>
    </div>
    <!-- 2) Watch for changes in the "result" and reset the "value" after 5 seconds (hint: setTimeout(..., 5000) -->
    <div>
        <input type="text">
        <p>{{ value }}</p>
    </div>
</div>

JS
new Vue({
  el: '#exercise',
  data: {
    value: 0
  },
  computed: {
		result: function() {
    	    return this.value < 37 ? 'not there yet' : 'done';
    }
   },
   watch: {
   	value: function(value) {
    	var vm = this;
      setTimeout(function() {
      	vm.value = 0;
      }, 5000);
    }
   }
});
```

### Dynamic Styling with CSS Classes - Basics