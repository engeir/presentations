<script src="plugin/markdown/markdown.js"></script>
<script>
  Reveal.initialize({
    plugins: [ RevealMarkdown ]
  });
</script>

<!-- .slide: data-background="#000000" -->

### A slide with a dark background

Try to press the down arrow key.

--

<!-- .slide: data-background="#ff8888" -->

### Another slide

Try **Esc** and **F** keys.

- A bullet point
- Another convincing argument

---

### Code blocks are no problem

Here we have some Python code:

```python [1|3-4|6-7]
from itertools import cycle

fizz = cycle(['', '', 'Fizz'])
buzz = cycle(['', '', '', '', 'Buzz'])

for i in range(1, 101):
    print((next(fizz) + next(buzz)) or i)
```

[Source](https://github.com/olemb/nonsense/blob/master/fizzbuzz/itertools_cycle.py)

<aside class="notes">
    Shhh, these are your private notes 📝
</aside>

---

### Images (1/2)

An image fetched from the web:

![Sample image](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/The_Young_Cicero_Reading.jpg/316px-The_Young_Cicero_Reading.jpg)
