<!-- .slide: data-background="#222" -->

# Running CESM2 with custom volcanic forcing

--

<!-- .slide: data-background="#990000" -->

## Plan

- Run CESM2 (community Earth system model) with volcanic forcing <!-- .element: class="fragment" data-fragment-index="1" -->
- Volcanoes are the only external forcing <!-- .element: class="fragment" data-fragment-index="2" -->
- Obtain estimate of the temperature response <!-- .element: class="fragment" data-fragment-index="3" -->

---

<!-- .slide: data-background="#222" -->

# Status

--

<!-- .slide: data-background="#222" -->

Create synthetic volcanic forcing data

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

--

<!-- .slide: data-background="#222" -->

| ![Aerosol forcing](https://github.com/engeir/presentations/raw/main/2022/uit-climate-meeting/AEROD_v_simple_vanilla.png) | ![Temperature](https://github.com/engeir/presentations/raw/main/2022/uit-climate-meeting/TREFHT_simple_vanilla.png) |
| -: | :- |
Historical run, unchanged

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
- Volcanoes that cluster together

---

<!-- .slide: data-background="#222" -->

# Questions

--

<!-- .slide: data-background="#222" -->

What is an appropriate frequency of volcanoes?

--

<!-- .slide: data-background="#222" -->

Is the response the same as that you get from, say CO<sub>2</sub>?

What about solar?

--

<!-- .slide: data-background="#222" -->

Is the response dependent on altitude? Magnitude/total emitted aerosols?

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

<!-- ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}) -->
