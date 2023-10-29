# Mildew detection in cherry leaves

predictive analytics project that can detect mildew in cherry leaves.

To run this project just type "streamlit run app.py" in the terminal. 
Just make sure you have all the requirements.

## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We created then a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from client's crop fields. The images show cherry leaves that are healthy and cherry leaves that contain powdery mildew, which is a fungal disease that affects a wide range of plants. The cherry plantation crop is one of their finest products in the portfolio and the company is concerned about supplying the market with a product of compromised quality.



## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is to manually verify if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If it has powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees located in multiple farms across the country. As a result, this manual process is not scalable due to time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that is capable of detecting instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project to all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy and that contains powdery mildew.
* 2 - The client is interested to predict if a cherry leaf is healthy or contains powdery mildew.


## Hypothesis and how to validate?
* Hypothesis:

Machine Learning can accurately differentiate between healthy and powdery mildew-affected cherry leaves: We hypothesize that a well-trained machine learning model can effectively distinguish between the two categories of cherry leaves based on image analysis.
Validation:

Data Collection and Annotation: Gather a diverse dataset of cherry leaf images, including both healthy and powdery mildew-affected leaves from different farms and conditions.

Model Development: Build and train a deep learning model, such as a Convolutional Neural Network (CNN), using the annotated dataset. Ensure proper data preprocessing, augmentation, and optimization techniques.

Validation and Testing: Split the dataset into training and testing subsets. Validate the model's performance on the testing subset using metrics such as accuracy, precision, recall, and F1-score.

Cross-Validation: Apply cross-validation techniques, such as k-fold cross-validation, to ensure the model's generalizability across different datasets and scenarios.

Real-time Testing: Deploy the model in a real-time or batch processing mode in the field. Continuously monitor and validate its performance against manual inspections.

User Feedback: Gather feedback from field employees who previously conducted manual inspections to assess the model's practical performance and accuracy.

Iterative Refinement: If the initial model doesn't meet performance benchmarks, refine the model, gather more data, or apply transfer learning to improve its accuracy.

The validation process aims to ensure that the machine learning model can reliably differentiate between healthy and powdery mildew-affected cherry leaves, leading to the successful implementation of the automated detection system.







## Rationale to map the business requirements to the Data Visualizations and ML tasks
* List your business requirements and a rationale to map them to the Data Visualizations and ML tasks.


## ML Business Case
* 1. Executive Summary:

Farmy & Foods is facing a significant challenge in their cherry plantation operations due to the presence of powdery mildew in cherry leaves. Their current manual inspection process is time-consuming, inefficient, and not scalable given the scale of their operations. To address this issue, we propose the development of a machine learning (ML) system for instant detection and classification of cherry leaves as healthy or containing powdery mildew. Successful implementation of this system can not only enhance the efficiency of cherry inspection but also provide a template for similar projects across various crops.

2. Problem Statement:

Farmy & Foods spends a substantial amount of time and resources on manual verification of cherry tree health, particularly detecting powdery mildew on leaves. This process is not scalable and consumes valuable labor resources. The primary objectives are:

To visually differentiate between a healthy cherry leaf and a leaf with powdery mildew.
To predict, using a machine learning model, whether a cherry leaf is healthy or contains powdery mildew.
3. Proposed Solution:

Implement a machine learning system for automated detection and classification of cherry leaves into two categories: healthy and powdery mildew-affected. The key components of the solution include:

Data Collection: Gather a comprehensive dataset of cherry leaf images, including healthy and powdery mildew-affected leaves from various farms.

Data Annotation: Annotate the dataset to label each image as either "healthy" or "powdery mildew-affected."

Model Development: Build a deep learning model, such as a Convolutional Neural Network (CNN), to learn the visual patterns that distinguish healthy and affected leaves.

Training and Validation: Train the model on a portion of the dataset and validate its performance using another portion to ensure robustness and accuracy.

Deployment: Deploy the trained model to analyze cherry leaf images in real-time or batch processing, enabling instant identification of leaf health.

Integration: Integrate the ML system into the company's existing infrastructure and processes for seamless adoption.

4. Benefits and Impact:

Time Efficiency: The ML system will drastically reduce the time required for leaf inspection. An automated process can process images almost instantly, saving significant labor hours.

Cost Reduction: By automating the detection process, Farmy & Foods can reduce labor costs associated with manual inspections.

Scalability: The system can easily scale to handle thousands of cherry trees, making it suitable for Farmy & Foods' extensive plantation operations.

Accuracy: ML models can achieve high accuracy in classifying leaf health, reducing the chances of misidentifying affected leaves.

Potential for Expansion: If successful, this project can be replicated for other crops, such as pest detection, further improving crop management across multiple farms.

5. Risks and Challenges:

Data Quality: The success of the model depends on the quality and diversity of the cherry leaf image dataset. Incomplete or biased data can lead to model inaccuracies.

Model Training: Proper model training and validation are crucial. Overfitting or underfitting can affect the model's performance.

Integration: The successful integration of the ML system into existing operations and infrastructure is vital. Proper testing and adjustments may be required.

6. Project Timeline:

The project can be divided into several phases:

Data Collection and Annotation: 2 months
Model Development and Training: 3 months
Validation and Fine-tuning: 1 month
Deployment and Integration: 1 month
Testing and Optimization: Ongoing

7. Investment and ROI:

Investment will be required for data collection, model development, hardware, and integration. The ROI will primarily come from reduced labor costs, increased efficiency, and the potential for expanded applications in other crops. A detailed financial analysis is needed to estimate the specific ROI.

8. Conclusion:

The implementation of a machine learning system for the automated detection of cherry leaf health offers a practical solution to Farmy & Foods' challenges. It not only improves the efficiency and accuracy of cherry inspection but also opens the door for similar initiatives in other crops. The successful adoption of this technology will position Farmy & Foods as a leader in innovative and sustainable agriculture practices.

## Dashboard Design
* List all dashboard pages and its content, either block of information or widgets, like: buttons, checkbox, image, or any other item that your dashboard library supports.
* Eventually, during the project development, you may revisit your dashboard plan to update a give feature (for example, in the beginning of the project you were confident you would use a given plot to display an insight but eventually you needed to use another plot type).


## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly in case all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.


## Main Data Analysis and Machine Learning Libraries



## Credits 

* In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign up page are from This Open Source site
- The images used for the gallery page were taken from this other open source site



## Acknowledgements (optional)
* In case you would like to thank the people that provided support through this project.
