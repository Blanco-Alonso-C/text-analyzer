# Text Analysis & Linguistic Statistics Project

---

## About the project

This project was developed by two students as a collaborative interdisciplinary exercise between Physics and English Studies, for learning and practice.

The goal is to explore how computational tools can be used to analyze natural language through both linguistic and statistical approaches.

The program performs a basic text analysis including lexical processing, simple NLP-like segmentation, and statistical evaluation of text structure. It also includes a basic attempt to estimate whether a text may be AI-generated.

This project was developed for educational purposes, and we deliberately avoided using NLP libraries such as spaCy or NLTK.

---

## Authors and contributions

### Barral Silva, P (English Philology student)
- Linguistic analysis
- NLP logic
- Lexical classification
- Text interpretation rules

GitHub: https://github.com/p-barral  
LinkedIn: https://www.linkedin.com/in/pedro-barral-silva-1a41b4409/

### Blanco Alonso, C (Physics student)
- Statistical analysis
- NumPy processing
- Matplotlib visualizations
- Project structure

GitHub: https://github.com/Blanco-Alonso-C  
LinkedIn: https://www.linkedin.com/in/carme-xiu-b-6030a0269/



---

## Features

- Word, sentence, and paragraph analysis
- Basic AI-generated text detection (experimental and not accurate)
- Detection of explicit and offensive language
- Language scoring (Spanish vs English estimation)
- Stylistic and structural text evaluation
- Lexical frequency analysis
- Statistical metrics (mean, variance, dispersion analysis)
- Visualization of results using Matplotlib
- Sample texts (can be extended)

---

## To do

- Improve AI detection or remove it
- Reduce error sensitivity
- Improve proper noun recognition
- Improve formal vs informal detection
- Improve contraction detection
- Add expressiveness parameters
- Improve sentence segmentation (especially with ! and ? symbols)

---

## Example output (sample text)

No file found. Default text will be used


Text analyzed

This text has 1485 words.  
This text has 46 sentences.

There might be 1.0 errors. Check it.

We give you 0.00 formal points  
We give you 0.07 weirdness points

We found 0.0 explicit words  
We found 0.0 offensive words

IA score out of 100: 0.00  
Spanish score out of 100: 100.00  
English score out of 100: 0.00

Do you want to save the image in outputs? (y/n)

---

## Requirements

Python 3.x  
NumPy  
Matplotlib  
Seaborn  

Install dependencies:

pip install -r requirements.txt

---

## How to run

Add your text inside file.txt  
Run the program:

python main.py

---

## Visualization

The program generates:

- Letter frequency distribution  
- Most common words  
- Most common numbers  
- Most common symbols  

---

## Note

This text analysis and AI detection tool is not professionally certified or backed by any official organization. Its results may be inaccurate or incomplete and should not be used for decision-making.

The creators assume no responsibility for how the information is used.

AI detection in particular is a complex problem and typically requires more advanced models and libraries that were intentionally not used in this project.
