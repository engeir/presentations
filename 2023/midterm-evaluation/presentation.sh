#!/bin/sh

#
# Depends on `sent` and `pnglatex`. See further dependencies therein.
#
# sent: https://tools.suckless.org/sent/
# pnglatex: https://github.com/mneri/pnglatex
#
# Run this script as
#
#   $ sh ./presentation.sh
#
# to generate the presentation, and present with
#
#   $ sent ./sent.sent
#

# Clear the text file and set the title
echo "Global Temperature Response to Volcanic Activity" >sent.sent
echo "" >>sent.sent

# Create all image files
pnglatex -S -e displaymath -b Transparent -F White -d 2000 -f "\Delta T(t)=\int_{\infty}^{t}G(t-s)[F(s)\mathrm{d}s+\sigma \mathrm{d}B(s)]" -o pic/gen/lin_model.png
pnglatex -S -e displaymath -b Transparent -F White -d 2000 -f "T_K(t)=\sum_{k=1}^K A_k \phi\left( \frac{t-t_k}{\tau_\mathrm{d}} \right)" -o pic/gen/sum.png
pnglatex -S -e displaymath -b Transparent -F White -d 2000 -f "T_K(t)=[\phi*f_K]\left(\frac{t}{\tau_\mathrm{d}}\right)" -o pic/gen/conv.png
pnglatex -S -e displaymath -b Transparent -F White -d 2000 -f "\phi^{(n+1)}=\phi^{(n)}\frac{(T_K-\langle T_K\rangle)*\hat{f}_K+b}{\phi^{(n)}*f_K*\hat{f}_K+b}" -o pic/gen/deconv.png

# Generate the text file.
echo "Motivation and background

@pic/gen/lin_model.png

Filtered Poisson Process

@pic/gen/sum.png

@pic/gen/conv.png

Deconvolution algorithm

@pic/gen/deconv.png

Model setup
  1. Synthetic eruptions are given to CESM2
  2. Run using the BWma1850 compset

Results

Single-volcano events

Double-volcano events

Do non-linear effects become important as an eruption
occur when the temperature is in a perturbed state?

CESM1 Last Millennium Ensemble

@./pic/cesm_lme_deconvolution_delta_old-daily-3000it_zoomed-frc.png

@./pic/cesm_lme_deconvolution_delta_new2_zoomed-temp.png

@./pic/cesm_lme_deconvolution_delta_new2_zoomed.png

Deconvolution Issues

@./pic/f_orig.png

@./pic/f_forward.png

Going Forward

Paper 1
Linear response to volcanic forcing
in different climate states in CESM2

Paper 2
Pulse estimation from simulation data
with a deconvolution method

Paper 3
Assessment of non-linear responses
in the LongRunMIP ensemble" >>sent.sent

# Finally, why not have a look at the result!
sent ./sent.sent
