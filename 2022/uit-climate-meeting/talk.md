<script type="text/javascript">
  window.MathJax = {
  options: {
    skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
    ignoreHtmlClass: 'tex2jax_ignore',
    processHtmlClass: 'tex2jax_process'
  },
  tex: {
    inlineMath: [['$','$'], ['\\(','\\)']],
    processEscapes: true,
    macros: {
      AA: "{\\unicode{x212B}}"
    },
    autoload: {
      color: [],
      colorv2: ['color']
    },
    packages: {'[+]': ['noerrors']}
  },
  chtml: {
    scale: 0.9
  },
  loader: {
    load: ['[tex]/noerrors']
  }
};
</script>

<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"
        type="text/javascript" >
</script>

<!-- .slide: data-background="#222" -->

# Running CESM2 with custom volcanic forcing

--

<!-- .slide: data-background="#990000" -->

## Plan

- Run CESM2 (community Earth system model) with volcanic forcing
- Volcanoes are the only external forcing <!-- .element: class="fragment" data-fragment-index="1" -->
- Poisson process <!-- .element: class="fragment" data-fragment-index="2" -->

--

#### Post industrial volcanoes

<!-- .slide: data-background="https://github.com/engeir/presentations/raw/main/2022/uit-climate-meeting/synthetic_volcanoes_historic.png" -->
<!-- .slide: data-background-size="95vw" -->

--

#### FPP generated volcanoes

<!-- .slide: data-background="https://github.com/engeir/presentations/raw/main/2022/uit-climate-meeting/synthetic_volcanoes_FPP.png" -->
<!-- .slide: data-background-size="95vw" -->

--

#### Large single volcano

<!-- .slide: data-background="https://github.com/engeir/presentations/raw/main/2022/uit-climate-meeting/synthetic_volcanoes_single.png" -->
<!-- .slide: data-background-size="95vw" -->

---

<!-- .slide: data-background="#222" -->

# Status

--

<!-- .slide: data-background="#222" -->

Create synthetic volcanic forcing data

--

<!-- .slide: data-background="#222" -->

| ![Aerosol forcing](https://github.com/engeir/presentations/raw/main/2022/uit-climate-meeting/AEROD_v_simple_vanilla.png) | ![Temperature](https://github.com/engeir/presentations/raw/main/2022/uit-climate-meeting/TREFHT_simple_vanilla.png) |
| -: | :- |
Unchanged historical run

Note:
How do I do this? Two images side-by-side should not be hard!?

--

<!-- .slide: data-background="#222" -->

| ![Aerosol forcing](https://github.com/engeir/presentations/raw/main/2022/uit-climate-meeting/AEROD_v_simple.png) | ![Temperature](https://github.com/engeir/presentations/raw/main/2022/uit-climate-meeting/TREFHT_simple.png) |
| -: | :- |
Historical run with large eruption in 1850-01-15

---

<!-- .slide: data-background="#222" -->

# Experiments

--

<!-- .slide: data-background="#222" -->

These are the model runs that are considered

- Small ensemble over 5 to 10 years -> Look at internal variability
- Longer run with volcanoes generated from an FPP

---

<!-- .slide: data-background="#222" -->

# Questions

- Appropriate frequency of volcanoes?
- Is the response the same as that you get from, say `$CO\_2$`? Solar?
- Is the response dependent on altitude? Magnitude/total emitted aerosols?
