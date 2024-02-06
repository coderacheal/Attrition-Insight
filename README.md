<a name="readme-top"></a>

<div align="center">
  <h1><b>Attrition Meter</b></h1>
</div>

<!-- TABLE OF CONTENTS -->

# 📗 Table of Contents

- [📗 Table of Contents](#-table-of-contents)
- [Attrition Meter ](#attrition-meter-)
  - [🛠 Built With ](#-built-with-)
    - [Tech Stack ](#tech-stack-)
  - [Key Features ](#key-features-)
  - [💻 Getting Started ](#-getting-started-)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
    - [Install](#install)
    - [Usage](#usage)
  - [👥 Authors ](#-authors-)
  - [🔭 Future Features ](#-future-features-)
  - [🤝 Contributing ](#-contributing-)
  - [⭐️ Show your support ](#️-show-your-support-)
  - [🙏 Acknowledgments ](#-acknowledgments-)
  - [📝 License ](#-license-)

<!-- PROJECT DESCRIPTION -->

# Attrition Meter <a name="about-project"></a>

**Attrition Meter** is a data application that allows users to interact with a machine learning model, view data visualizations on the data and see the values of their input saved for future use.

Features
1. **Age**: Age of employee
2. **Attrition**: Employee attrition status
3. **Department**: Department of work
4. **DistanceFromHome**: what is their distance from hime
5. **Education**: 1-Below College; 2- College; 3-Bachelor; 4-Master; 5-Doctor;
6. **EducationField**: The field they studies in in the University
7. **EnvironmentSatisfaction**: 1-Low; 2-Medium; 3-High; 4-Very High;
8. **JobSatisfaction**: 1-Low; 2-Medium; 3-High; 4-Very High;
9. **MaritalStatus**: Whether they are married, single or divorced
10. **MonthlyIncome**: How much an employee makes a month
11. **NumCompaniesWorked**: Number of companies worked prior to IBM
12. **WorkLifeBalance**: 1-Bad; 2-Good; 3-Better; 4-Best;
13. **YearsAtCompany**: Current years of service in IBM

## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

<details>
  <summary>GUI</summary>
  <ul>
    <li><a href="">Streamlit</a></li>
  </ul>
</details>

<details>
<summary>Database</summary>
  <ul>
    <li><a href="">Microsoft SQL Server</a></li>
  </ul>
</details>

<details>
<summary>Language</summary>
  <ul>
    <li><a href="">Python</a></li>
  </ul>
</details>

<details>
<summary>Model</summary>
  <ul>
    <li><a href="">Sklearn</a></li>
  </ul>
</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- Features -->

## Key Features <a name="key-features"></a>

- **A data application that presents visualizations on both the exploratory data and the KPIs**
- **A predicitons page to predict by specifying the model you want to use**
- **View proprietory data loaded in real-time form the remote server**
- **Predictions are save for further analysis in the future and users can view the history of their prediction input values**


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>


To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project you need:

- Python
- Streamlit

### Setup

Clone this repository to your desired folder:


```sh
  cd my-folder
  git clone https://github.com/coderacheal/Attrition-Meter.git
```

Change into the cloned repository

```sh
  cd Attrition-Meter
  
```

Create a virtual environment

```sh

python -m venv env

```

Activate the virtual environment

```sh
    virtual_env/Scripts/activate
```


### Install

Here, you need to recursively install the packages in the `requirements.txt` file using the command below 

```sh
   pip install -r requirements.txt
```


### Usage

To run the project, execute the following command:


```sh
    streamlit run 1_🏠_Home.py

```

- A webpage opens up to view the app
- Login to the app with `username=coderacheal` and `password:abc`
- Finally test a prediction by clicking on the predicitons page
- **Note**: Users may not be able to access the View Data page as the secrets file is not checked into git

<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

🕵🏽‍♀️ **Racheal Appiah-kubi**

- GitHub: [GitHub Profile](https://github.com/coderacheal)
- Twitter: [Twitter Handle](https://twitter.com/racheal_kubi)
- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/racheal-appiah-kubi/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FUTURE FEATURES -->

## 🔭 Future Features <a name="future-features"></a>


- **Add a front end application for users**
  
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUPPORT -->

## ⭐️ Show your support <a name="support"></a>

If you like this project kindly show some love, give it a 🌟 **STAR** 🌟

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGEMENTS -->

## 🙏 Acknowledgments <a name="acknowledgements"></a>

I would like to thank all the free available resource made available online

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


