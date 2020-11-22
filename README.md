<h1 align="center">
  Music genre predictor with ML4Kids
</h1>

<p align="center">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/lucasleonardobs/genre-predictor-ml4kids">

  <a href="https://www.linkedin.com/in/lucasleonardobs/">
    <img alt="Made by" src="https://img.shields.io/badge/made%20by--gree">
    <img src="https://img.shields.io/badge/Lucas%20Leonardo-gree">
  </a>
  <a href="https://www.linkedin.com/in/w-alves/">
    <img src="https://img.shields.io/badge/Wesley%20Alves-gree">
  </a>
</p>

<p align="center">
  <a href="#-about-the-project">About the project</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-technologies">Technologies</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-getting-started">Getting started</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-license">License</a>
</p>

## 👨🏻‍💻 About the project

### Authors

|                   Tasks                    | Name                                                 |
| :----------------------------------------: | ---------------------------------------------------- |
|    Data Collection and Data Preparation    | [Lucas Leonardo](https://github.com/lucasleonardobs) |
| Machine Learning Engineering and Operation | [Wesley Alves](https://github.com/w-alves/l)         |

### **Context**

The main idea of this project submitted as AI Project of the Introduction to Computing discipline, at CIn - Federal University of Pernambuco is is to train an artificial intelligence that manages to classify a song between **funk**, **rap** and **sertanejo** based on her lyrics. For that, we used IBM Watson Assistant together with Machine Learning For Kids to carry out the training.

In order to automate the process as a whole, a Python pipeline was created that works as follows:

1. **Data collection:** The data used for training and testing were collected in an automated way from the creation of a script for data scraping. This script was applied to the ranking of the most accessed songs of each genre chosen on the site Letras.mus.br.

2. **Prepare the data:** After collecting the data, we perform a simple preparation step that consists of limiting the letters to 1000 characters (in order to respect the ML4Kids limit) and performing a stratified train test split. This separation was carried out in order to create a dataset for training and another for the validation of the model, stratifying the proportion of approximately 33% for each label.

3. **Train the model:** In order to avoid the delay of manually registering 500 lyrics through the ML4Kids interface, we also implemented in Python a script that performs requests using the API_KEY provided.
4. **Test the model:** The platform in question also has a limitation regarding the testing of the model, there we were unable to input categorized data and check the performance on that data. In order to solve this imbroglio, we developed a script that generates predictions from API_KEY and compares with the expected results, generating a confusion matrix and a classification report.

In these steps mentioned above, we used the **Scrapy** libraries to scrape the data, **Pandas** and **Scikit-learn** to prepare and separate the data, **Scikit-learn/Mlextend/Matplotlib** to generate and plot the results.

In addition, a friendly interface was created in Python, with the help of **Streamlit**, so that any user can interact with the model in a friendly way.

## Results

For this multi-class classification problem, a simple and efficient way to observe the results obtained is through the confusion matrix. Below we can see the matrix generated with the tests performed here:

![](https://i.imgur.com/fb8u1bj.png)

Furthermore, it is also important that we look at the precision and recall metrics. Given the above, we can say that the model has an excellent performance given the limited amount of data used during training, since we have achieved overall good results in both precision and recall.

|              | precision          | recall             | f1-score           | support |
| ------------ | ------------------ | ------------------ | ------------------ | ------- |
| hip_hop      | 0.8529411764705882 | 0.7073170731707317 | 0.7733333333333334 | 41.0    |
| funk         | 0.7906976744186046 | 0.8292682926829268 | 0.8095238095238095 | 41.0    |
| sertanejo    | 0.8085106382978723 | 0.9047619047619048 | 0.853932584269663  | 42.0    |
| weighted avg | 0.8173116104432866 | 0.8145161290322581 | 0.8125992854553927 | 124.0   |

An important observation to make is that, in the interface created for the user, when a prediction is generated with less than 65% confidence, the result is not informed to the user, indicating an uncertainty of the model.

## 🚀 Technologies

Technologies we use to develop this predictor

- [Python](https://www.python.org)
- [Scrapy](https://scrapy.org)
- [Streamlit](https://www.streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Numpy](https://numpy.org/)
- [Scikit-learn](https://scikit-learn.org/stable/)
- [Matplotlib](https://matplotlib.org/)
- [mlxtend](https://rasbt.github.io/mlxtend/)
- [Decouple](https://github.com/henriquebastos/python-decouple)

## 💻 Getting started

### **Requirements**

To use this application you must have [Python](https://www.python.org/downloads/) installed in your OS and you must have installed the external packages listed at `requirements.txt`.

### **Usage**

1. Clone this repository

   ```
   $ git clone https://github.com/lucasleonardobs/genre-predictor-ml4kids
   ```

2. Open the prompt at the project directory.

3. Install the requirements.txt

   ```
   $ pip install -r requirements.txt
   ```

4. Access [ML4Kids](https://machinelearningforkids.co.uk/), register and sync the IBM account (check the tutorial [here](https://github.com/IBM/taxinomitis-docs/raw/master/docs/pdf/machinelearningforkids-ibmer.pdf))

5. Create a project with the following rules.

   > Recognizing: text
   >
   > Language: Portuguese

6. Go to "Train model", create three labels: **hip_hop**, **sertanejo **and **funk**.

7. Return to project page and go to "Make" and copy your API_KEY.![](https://i.imgur.com/KfzcQzQ.png)

8. Create a .env file in the project directory with some text editor and add your API_KEY. See the example below.

   ```
   $ API_KEY="7884ef60-2c17-11eb-8469"
   ```

9. Run the pipeline via command prompt

   ```
   $ python pipeline.py
   ```

After the first run, you do not need anymore to run the pipeline again, just run the following line in the command prompt:

```
$ streamlit run main.py
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with 💜 by [Lucas Leonardo](https://www.linkedin.com/in/lucasleonardobs/) n [Wesley Alves](https://www.linkedin.com/in/w-alves) 👋 [See our linkedin]
