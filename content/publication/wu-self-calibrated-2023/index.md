---
abstract: Significance Pulse oximetry estimates the arterial oxygen saturation of
  hemoglobin (SaO2) based on relative changes in light intensity at the cardiac frequency.
  Commercial pulse oximeters require empirical calibration on healthy volunteers,
  resulting in limited accuracy at low oxygen levels. An accurate, self-calibrated
  method for estimating SaO2 is needed to improve patient monitoring and diagnosis.  Aim
  Given the challenges of calibration at low SaO2 levels, we pursued the creation
  of a self-calibrated algorithm that can effectively estimate SaO2 across its full
  range. Our primary objective was to design and validate our calibration-free method
  using data collected from human subjects.  Approach We developed an algorithm based
  on diffuse optical spectroscopy measurements of cardiac pulses and the modified
  Beer–Lambert law (mBLL). Recognizing that the photon mean pathlength ( ⟨ L ⟩ ) varies
  with SaO2 related absorption changes, our algorithm aligns/fits the normalized ⟨
  L ⟩ (across wavelengths) obtained from optical measurements with its analytical
  representation. We tested the algorithm with human freedivers performing breath-hold
  dives. A continuous-wave near-infrared spectroscopy probe was attached to their
  foreheads, and an arterial cannula was inserted in the radial artery to collect
  arterial blood samples at different stages of the dive. These samples provided ground-truth
  SaO2 via a blood gas analyzer, enabling us to evaluate the accuracy of SaO2 estimation
  derived from the NIRS measurement using our self-calibrated algorithm.  Results
  The self-calibrated algorithm significantly outperformed the conventional method
  (mBLL with a constant ⟨ L ⟩ ratio) for SaO2 estimation through the diving period.
  Analyzing 23 ground-truth SaO2 data points ranging from 41% to 100%, the average
  absolute difference between the estimated SaO2 and the ground truth SaO2 is 4.23
  % ± 5.16 % for our algorithm, significantly lower than the 11.25 % ± 13.74 % observed
  with the conventional approach.  Conclusions By factoring in the variations in the
  spectral shape of ⟨ L ⟩ relative to SaO2, our self-calibrated algorithm enables
  accurate SaO2 estimation, even in subjects with low SaO2 levels.
authors:
- Jingyi Wu
- J. Chris McKnight
- Eva-Maria S. Bønnelycke
- Gerardo Bosco
- Tommaso Antonio Giacon
- Jana M. Kainerstorfer
categories:
- PortaLite
date: '2023-12-18'
doi: 10.1117/1.JBO.28.11.115002
featured: false
projects:
- brain-fnirs-prefrontal-cortex
publication: '*Journal of Biomedical Optics*'
publication_types:
- '2'
publishDate: 2023-12-18 09:24:56.726718+00:00
tags: []
title: Self-calibrated pulse oximetry algorithm based on photon pathlength change
  and the application in human freedivers

---
