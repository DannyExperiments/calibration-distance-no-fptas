# Why exact anchor loads matter

[Download the offline explorer ZIP](https://raw.githubusercontent.com/DannyExperiments/calibration-distance-no-fptas/v1.0.0/visualization/calibration-distance-no-fptas-explorer.zip). Extract it and open index.html. Move each ordinary atom between either anchor and the ordinary-only bucket. The explorer computes the exact calibrated means, unnormalized loss and the lower bound from aggregate deficit. It can also find the best assignment of the six ordinary atoms by exact enumeration.

The diagrams show ordinary masses to scale. Each heavy anchor pair is a schematic base. The dashed guides mark the target load of 15. The two cases have the same total ordinary mass. Weights 4, 5 and 6 can fill each anchor exactly. With three 4s and three 6s all possible loads are even. The minimum loss for that instance exceeds the baseline by 4800/3607 before normalization. The exact replay verifies that these best intact-anchor assignments also minimize over every partition of each depicted ten-atom instance.

To regenerate the GIF, run the following with Python 3 and Pillow already installed.

    python3 visualization/render.py

Arial is the default on macOS. Set Q460_FONT and Q460_BOLD_FONT to paths to suitable fonts on other systems.
