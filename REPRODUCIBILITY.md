# Reproduce the checks

From the repository root with Python 3.9 or newer:

    python3 -I scripts/verify_repository.py
    python3 -I verification/src/replay.py

The replay uses exact fractions and enumerates every set partition in three ten-atom instances. It also visits every allocation of the six ordinary atoms among the two anchored blocks and an ordinary-only bucket. A separate finite loop checks both branches of the single-block cost formula. [Recorded output](verification/logs/replay.txt)

The general inequality and the bit-model complexity argument are proved in the [paper](paper/manuscript.pdf). [Build the PDF](paper/BUILD.md) · [Regenerate and use the explorer](visualization/README.md)
