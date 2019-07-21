# Vue JS

## Let's Create our First VueJS Application

```
HTML
<script src="https://unpkg.com/vue/dist/vue.js">
</script>

<div id="app">
    <p>{{ title }}</p>
</div>
```

````
JS

new Vue({
    el: '#app',
    data: {
        title: 'Hello World'
    }
});
````