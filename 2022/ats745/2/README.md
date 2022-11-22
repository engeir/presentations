# ATS745 Presentation 2

Suggestions:

- Focus on MAM?

This presentation was part of the course ATS745.

Find the source code for the presentation at
`engeir/slides/content/2022-09-30-ats745-1.md`
([permalink](https://github.com/engeir/slides/blob/194ff0947cb8db46e541ca85bb79c2d134d77555/content/2022-09-30-ats745-1.md),
[dynamic link](https://github.com/engeir/slides/blob/main/content/2022-09-28-ats745-1.md)),
and the finished slides at
[slides.eirikenger.xyz](https://slides.eirikenger.xyz/2022-09-30-ats745-1.html).

## Notes

Marsh et al. 2013

- Studies of greenhouse gas, energetic particles, solar cycle, ozon hole and
  geoengineering
- Important to resolve the stratosphere to correctly simulate the tropospheric weather
- Chemistry module in WACCM4 based on version 3 of the Model for Ozone and Related
  Chemical Tracers
- No detailed description of tropospheric chemistry beyond methane and CO oxidation
- Heating from stratospheric volcanic aerosols is the same as in CCMVal2
  - Volcanic aerosol SAD is prescribed from a monthly zonal-mean time series derived
    from observations
- WACCM explicitly represents the radiative transfer of carbon dioxide, methane, nitrous
  oxide, and two halogens
- Heating rates vary as the irradiance varies in each spectral band, unlike in CAM4,
  where heating in all bands are scaled uniformly with the variation in TSI
- The absence of TMS and the differing horizontal resolution makes it difficult to
  determine if simulation differences are due to these model features or to the vertical
  extension of the model into the thermosphere and inclusion of interactive chemistry
- Sea level pressure (SLP) and precipitation rates are significantly different
- SLP and precipitation rates may have more to do with horizontal resolution or the
  addition of TMS (turbulent mountain stress)
- "Cold pole problem"
- Stratospheric sudden warmings (SSWs) are the dominant mode of variability in the NH
  winter stratosphere, and reproducing their frequency is a critical benchmark for any
  high-top climate model
  - The reduced frequency in December relative to January is in agreement with
    observations, and an improvement over the specified SST WACCM simulations reported
    by de la Torre et al. (2012)
  - This indicate a severe lack of internal variability in the NH winter polar
    stratosphere in CCSM4
  - The cause of the increase in SSWs with TMS, they suggest, is related to a
    TMS-induced change in the tropospheric circulation and orographic gravity wave drag,
    which modifies the upward propagation of stationary planetary waves and the
    initiation of SSWs
- Closely related to SSWs are variations in the northern annular mode (NAM) index
- Coincident with a major SSW there is a large negative perturbation in the NAM
- WACCM maintains the improvement found in CAM4 in blocking frequencies over Western
  Europe compared to CAM3
- It seems unlikely that the mechanisms by which TMS drives the large differences in
  SSWs is through its effect on blocking
- WACCM accurately reproduces the long-term decrease in column ozone from approximately
  250 Dobson units (DU) in 1960 to 150 DU for present day
- Both models overestimate the short-term cooling following large volcanic eruptions
- CCSM4 predicts too low stratospheric polar temperatures
- We find that the Arctic sea ice extent is more realistic in WACCM
