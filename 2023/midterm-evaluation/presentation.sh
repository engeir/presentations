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

pnglatex -S -b Transparent -F White -d 2000 -f "\mathrm{CO_2}" -o pic/co2.png
printf "@pic/co2.png\n\n" >>sent.sent

pnglatex -S -b Transparent -F White -d 2000 -f "T_K(t)=\sum_{k=1}^K A_k \phi\left( \frac{t-t_k}{\tau_\mathrm{d}} \right)" -o pic/sum.png
printf "@pic/sum.png\n\n" >>sent.sent

pnglatex -S -b Transparent -F White -d 2000 -f "T_K(t)=[\phi*f_K]\left(\frac{t}{\tau_\mathrm{d}}\right)" -o pic/conv.png
printf "@pic/conv.png\n\n" >>sent.sent

pnglatex -S -b Transparent -F White -d 2000 -f "\phi^{(n+1)}=\phi^{(n)}\frac{(T_K-\langle T_K\rangle)*\hat{f}_K+b}{\phi^{(n)}*f_K*\hat{f}_K+b}" -o pic/deconv.png
printf "@pic/deconv.png\n\n" >>sent.sent

# Finally, why not have a look at the result!
# sent ./sent.sent
