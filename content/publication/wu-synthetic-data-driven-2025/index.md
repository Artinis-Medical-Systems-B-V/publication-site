---
abstract: Optical monitoring of cardiac pulsations using near-infrared spectroscopy
  (NIRS), photoplethysmography (PPG), and diffuse correlation spectroscopy (DCS) is
  often hindered by motion artifacts and noise. We introduce a synthetic-data-driven
  framework using a long short-term memory (LSTM) network to trace and denoise pulsatile
  optical waveforms without reliance on annotated clinical datasets. Physiologically
  realistic pulsatile signals are generated, corrupted with parameterized artifacts,
  and used to train the LSTM model. Applied to experimental NIRS, PPG, and DCS signals,
  the model recovered beat-to-beat morphology more effectively than widely used wavelet
  and temporal derivative distribution repair (TDDR) filters. Heart rate (HR) extraction
  from LSTM-processed signals closely matched ECG-derived measurements (mean absolute
  error = 0.59 bpm, root mean square error = 0.74 bpm). This flexible approach shows
  potential for rapid adaptation across various devices and noise conditions.
authors:
- Jingyi Wu
- Shaojie Bai
- Zeynep Ozkaya
- Justin A. Patel
- Emily Skog
- Alexander Ruesch
- Matthew A. Smith
- Jana M. Kainerstorfer
categories:
- PortaLite
date: '2025-11-19'
doi: 10.1364/BOE.574286
featured: false
projects:
- brain-fnirs-prefrontal-cortex
publication: '*Biomedical Optics Express*'
publication_types:
- '2'
publishDate: 2025-11-19 08:15:13.929206+00:00
tags: []
title: Synthetic-data-driven LSTM framework for tracing cardiac pulsation in optical
  signals

---
