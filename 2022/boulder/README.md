# Talk in Boulder CO

Talk should largely focus on WACCM and how and why I use it.

## Ideas

- What is the main goal/aim of the project
- Describe the model setup I use
- Explain steps I take when running the model, possibly a quick look at
  `volcano-cooking`
- Present results I showed on CHESS AM 22
- Present results from double-overlap simulation
- Discuss seasonal variability and ask for tips
- Possibly some future ideas/suggestions

## Abstract

In order to estimate the global temperature response and climate sensitivity to
radiative forcing, volcanic activity is an important testbed. This work uses a
non-parametric method for estimating the temperature response due to volcanic forcing.
To get good forcing and temperature data sets, simulations are performed in the
community Earth systems model version 2 (CESM2). The simulations are run using the
WACCM6 high-top atmosphere, with middle atmosphere that lack the tropospheric chemistry,
but that calculates the evolution of stratospheric aerosols from SO2 from large volcanic
eruptions.

Ensembles of simulations with one single eruption, shifted in time and with different
magnitude across the ensemble, is used as a baseline to look at the shape of the
temperature response to single-events. Further use of the single-events are made in
combination with a simulation of a double-event eruption, and how superposing
single-events may simulate such double-events.

Finally, long runs consisting of many events occurring with random arrival times and
magnitude are to be used to get a general shape representing the temperature response to
an arbitrary volcanic eruption. We obtain the shape using the Richardson-Lucy
deconvolution algorithm, thus every eruption during the full time series contribute to
the same estimate of the shape of the response.
