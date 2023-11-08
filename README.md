# Human-Centered AI B Network Science: Fundamentals and Applications
Repository for the class of Human-centered AI at Univ. of Tsukuba

## Introduction
This is a repository for the class of Human-centered AI B at Univ. of Tsukuba by Prof. Tsugawa.

## Requirement
Please install networkx, pandas, and numpy.
```bash
pip3 install networkx pandas numpy seaborn
```

## Usage
### Calculating network features 
```bash
python3 calc_feature.py data/ba.txt
```

### Calculating centrality
```bash
python3 calc_centrality.py data/advice.txt
```
For obtaining relation between centrality and citation count as introduced in the lecture, 
```bash
python3 calc_cent_citation.py data/apscoauthor.csv data/citation_count.txt >result.txt
```
For obtaining a pairplot,
```bash
python3 pair_plot.py result.txt
```

### Community Detection
For obtaining communities of the Karate-club network,
```bash
python3 community_karate.py
```
For obtaining communities of an Email network and calculating the RandIndex as introduced in the lecture,
```bash
python3 community_email.py email-Eu-core.txt email-Eu-core-department-labels.txt
```
Data is available from
http://snap.stanford.edu/data/email-Eu-core.html

### Simulation of SIR model
For a single simulation run
```bash
python3 sir.py data/er.txt
```
For 100 simulation runs, and calculating avearge
```bash
sh bin/run-sir.sh data/er.txt
```

### Hints for assignments

Run a simulation of SIR model with random vaccination
```bash
python3 sir_random_immunization.py data/ba.txt
```
Run a simulation of SIR model from random seed.
```bash
python3 sir_random_seeding.py data/ba.txt
```

## Network datasets
Public repositories of network datasets
- http://snap.stanford.edu/data/index.html
- http://networksciencebook.com/translations/en/resources/data.html
