---
abstract: A lot of research has been done on the detection of mental workload (MWL)
  using various bio-signals. Recently, deep learning has allowed for novel methods
  and results. A plethora of measurement modalities have proven to be valuable in
  this task, yet studies currently often only use a single modality to classify MWL.
  The goal of this research was to classify perceived mental workload (PMWL) using
  a deep neural network (DNN) that flexibly makes use of multiple modalities, in order
  to allow for feature sharing between modalities. To achieve this goal, an experiment
  was conducted in which MWL was simulated with the help of verbal logic puzzles.
  The puzzles came in five levels of difficulty and were presented in a random order.
  Participants had 1 h to solve as many puzzles as they could. Between puzzles, they
  gave a difficulty rating between 1 and 7, seven being the highest difficulty. Galvanic
  skin response, photoplethysmograms, functional near-infrared spectrograms and eye
  movements were collected simultaneously using LabStreamingLayer (LSL). Marker information
  from the puzzles was also streamed on LSL. We designed and evaluated a novel intermediate
  fusion multimodal DNN for the classification of PMWL using the aforementioned four
  modalities. Two main criteria that guided the design and implementation of our DNN
  are modularity and generalisability. We were able to classify PMWL within-level
  accurate (0.985 levels) on a seven-level workload scale using the aforementioned
  modalities. The model architecture allows for easy addition and removal of modalities
  without major structural implications because of the modular nature of the design.
  Furthermore, we showed that our neural network performed better when using multiple
  modalities, as opposed to a single modality. The dataset and code used in this paper
  are openly available.
authors:
- Tenzing C. Dolmans
- Mannes Poel
- Jan Willem J.R. van 't Klooster
- Bernard P. Veldkamp
categories:
- Brite
date: 2021-01-01
doi: 10.3389/fnhum.2020.609096
featured: false
projects:
- brain-computer-interfaces
- brain-fnirs-prefrontal-cortex
publication: '*Frontiers in Human Neuroscience*'
publication_types:
- '2'
publishDate: 2021-03-05 16:32:21.360765+00:00
tags:
- GSR (galvanic skin response)
- PPG (photoplethysmography)
- brain-computer interface (BCI)
- deep learning
- device synchronisation
- eye tracking (ET)
- fNIRS (functional near infrared spectroscopy)
- multimodal deep learning architecture
title: Perceived Mental Workload Classification Using Intermediate Fusion Multimodal
  Deep Learning
url_pdf: https://www.frontiersin.org/articles/10.3389/fnhum.2020.609096/full

---
