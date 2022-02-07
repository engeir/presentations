<!-- .slide: data-background="#222" -->

# Running CESM2 with synthetic volcanic forcing

--

<!-- .slide: data-background="#990000" -->

## Plan

- Run CESM2 (community Earth system model) with volcanic forcing <!-- .element: class="fragment" data-fragment-index="1" -->
- Volcanoes are the only external forcing <!-- .element: class="fragment" data-fragment-index="2" -->
- Obtain estimate of the temperature response <!-- .element: class="fragment" data-fragment-index="3" -->

---

<!-- .slide: data-background="#222" -->

# Example

--

<!-- .slide: data-background-color="#222" -->
<!-- .slide: data-background="https://github.com/engeir/presentations-files/raw/main/2021/fysikermotet/noresm/noresm_raw_dark.png" -->
<!-- .slide: data-background-size="95vw" -->

--

<!-- .slide: data-background-color="#222" -->
<!-- .slide: data-background="https://github.com/engeir/presentations-files/raw/main/2021/fysikermotet/noresm/response_func_noresm1_choose_dark.png" -->
<!-- .slide: data-background-size="95vw" -->

--

<!-- .slide: data-background-color="#222" -->
<!-- .slide: data-background="https://github.com/engeir/presentations-files/raw/main/2021/fysikermotet/noresm/noresm_raw_with_est_dark.png" -->
<!-- .slide: data-background-size="95vw" -->

--

> FPP — filtered Poisson process

<!-- .slide: style:"color=red" -->
<!-- .slide: data-background-color="#002f4b" -->
<!-- .slide: data-background-video-loop="true" -->
<!-- .slide: data-background-video="https://github.com/engeir/presentations-files/raw/main/2021/fysikermotet/animation.mp4" -->
<!-- .slide: data-background-size="contain" -->

---

<!-- .slide: data-background="#222" -->

# Status

--

<!-- .slide: data-background="#222" -->

Creating synthetic volcanic forcing data

--

<!-- .slide: data-transition="slide-in fade-out" -->
<!-- .slide: data-background-transition="slide-in fade-out" -->
<!-- .slide: style="top:0" -->
<!-- .slide: data-background="https://github.com/engeir/presentations/raw/main/2022/uit-climate-meeting/assets/synthetic_volcanoes_historic.png" -->
<!-- .slide: data-background-size="95vw" -->
<!-- .slide: data-background-color="#000" -->

### Post industrial volcanoes

</br>
</br>
</br>
</br>
</br>
</br>
</br>

--

<!-- .slide: data-transition="fade" -->
<!-- .slide: data-background="https://github.com/engeir/presentations/raw/main/2022/uit-climate-meeting/assets/synthetic_volcanoes_FPP.png" -->
<!-- .slide: data-background-size="95vw" -->
<!-- .slide: data-background-color="#000" -->

### FPP generated volcanoes

</br>
</br>
</br>
</br>
</br>
</br>
</br>

--

<!-- .slide: data-transition="fade-in slide-out" -->
<!-- .slide: data-background="https://github.com/engeir/presentations/raw/main/2022/uit-climate-meeting/assets/synthetic_volcanoes_single.png" -->
<!-- .slide: data-background-size="95vw" -->
<!-- .slide: data-background-size="95vw" -->
<!-- .slide: data-background-color="#000" -->

### Large single volcano

</br>
</br>
</br>
</br>
</br>
</br>
</br>

--

<!-- .slide: data-background="#222" -->
<!-- .slide: data-transition="slide-in fade-out" -->

| ![Aerosol forcing](https://github.com/engeir/presentations/raw/main/2022/uit-climate-meeting/assets/AEROD_v_simple_vanilla.png) | ![Temperature](https://github.com/engeir/presentations/raw/main/2022/uit-climate-meeting/assets/TREFHT_simple_vanilla.png) |
| -: | :- |
Historical run, unchanged

Note:
How do I do this? Two images side-by-side should not be hard!?

--

<!-- .slide: data-transition="fade" -->
<!-- .slide: data-background="#222" -->

| ![Aerosol forcing](https://github.com/engeir/presentations/raw/main/2022/uit-climate-meeting/assets/AEROD_v_simple.png) | ![Temperature](https://github.com/engeir/presentations/raw/main/2022/uit-climate-meeting/assets/TREFHT_simple.png) |
| -: | :- |
Historical run with large eruption in 1850-01-15

---

<!-- .slide: data-background="#222" -->

# Experiments

--

<!-- .slide: data-background="#222" -->
<!-- .slide: data-transition="fade" -->

1. Small ensemble over 5 to 10 years &#8594; Look at internal variability
2. Longer run with volcanoes generated from an FPP <!-- .element: class="fragment" data-fragment-index="1" -->
3. Volcanoes that cluster together <!-- .element: class="fragment" data-fragment-index="2" -->

---

<!-- .slide: data-background="#222" -->

# Questions

--

<!-- .slide: data-background="#222" -->

What is an appropriate frequency of volcanoes?

![Aerosol forcing](https://github.com/engeir/presentations/raw/main/2022/uit-climate-meeting/assets/AEROD_v_simple_vanilla.png)
<!-- .element: class="fragment" -->

--

<!-- .slide: data-background="#222" -->

Is the response the same as that you get from, say CO<sub>2</sub>?

What about solar?

--

<!-- .slide: data-background="#222" -->
<!-- .slide: data-transition="slide-in fade-out" -->

Is the response dependent on altitude? Magnitude/total emitted aerosols?

--

<!-- .slide: data-background="#222" -->
<!-- .slide: data-transition="fade" -->

- What is an appropriate frequency of volcanoes?
- Is the response the same as that you get from, say CO<sub>2</sub>? What about solar?
- Is the response dependent on altitude? Magnitude/total emitted aerosols?

---

<!-- .slide: data-background="#222" -->

# iFrame background

--

<!-- .slide: data-background-iframe="https://flottflyt.com" -->

---

<!-- .slide: data-background="#222" -->

# Code

--

<!-- .slide: data-background="#222" -->

```python
def main() -> None:
    for i in range(3):
        print(f"Do nothing, just print line {i}")

if __name__ == "__main__":
    main()
```

---

<!-- .slide: data-background="#222" -->

# Math

--

<!-- .slide: data-background="#222" -->

&theta;

--

<!-- .slide: data-background="#222" -->

<math>
<mrow>
  <mrow>
    <msup>
      <mi>a</mi>
      <mn>2</mn>
    </msup>
    <mo>+</mo>
    <msup>
      <mi>b</mi>
      <mn>2</mn>
    </msup>
  </mrow>
  <mo>=</mo>
  <msup>
    <mi>c</mi>
    <mn>2</mn>
  </msup>
</mrow>
</math>

a<sup>2</sup>+b<sup>2</sup>=c<sup>2</sup>

<math>
 <mrow>
  <mi>cos(</mi>
  <msup>
   <mi>x</mi>
   <mn>3</mn>
  </msup>
  <mi>)</mi>
 </mrow>
</math>

<!-- ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}) -->
