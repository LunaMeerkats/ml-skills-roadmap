# **Stage 1 — Foundations (Weeks 1–4)**

## **Week 1 – NumPy/pandas (Py) + STL basics (C++)**

| Day | Python                                                                                                                                         | C++                                                                                                                                                        |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mon | [NumPy Quickstart – array creation/indexing/slicing](https://numpy.org/doc/stable/user/quickstart.html)                                        | [cppreference – `std::vector`](https://en.cppreference.com/w/cpp/container/vector)                                                                         |
| Tue | [NumPy broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html), [ufuncs](https://numpy.org/doc/stable/reference/ufuncs.html) | [cppreference – `std::map`](https://en.cppreference.com/w/cpp/container/map), [Range-based for loop](https://en.cppreference.com/w/cpp/language/range-for) |
| Wed | [pandas Series/DataFrame intro](https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html)                                          | [C++ File I/O basics](https://en.cppreference.com/w/cpp/io)                                                                                                |
| Thu | [pandas selection & indexing](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html)                                           | [Parsing CSV into containers](https://stackoverflow.com/questions/1120140/how-can-i-read-and-parse-csv-files-in-c)                                         |
| Fri | [pandas groupby & aggregation](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html)                                           | [Summing/averaging a vector](https://en.cppreference.com/w/cpp/algorithm/accumulate)                                                                       |
| Sat | Kaggle dataset practice ([Kaggle Datasets](https://www.kaggle.com/datasets))                                                                   | Replicate CSV stats in C++                                                                                                                                 |
| Sun | [Pro Git Book – Git basics](https://git-scm.com/book/en/v2)                                                                                    | Same                                                                                                                                                       |

---

## **Week 2 – Matplotlib/Seaborn (Py) + OpenCV plotting (C++)**

| Day | Python                                                                                            | C++                                                                                                         |
| --- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Mon | [Matplotlib Pyplot intro](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)       | [OpenCV – load/display image](https://docs.opencv.org/master/db/deb/tutorial_display_image.html)            |
| Tue | [Matplotlib customization](https://matplotlib.org/stable/tutorials/introductory/customizing.html) | [OpenCV – draw shapes/text](https://docs.opencv.org/master/dc/da5/tutorial_py_drawing_functions.html)       |
| Wed | [Seaborn distributions](https://seaborn.pydata.org/tutorial/distributions.html)                   | [OpenCV – histograms](https://docs.opencv.org/master/d8/dbc/tutorial_histogram_calculation.html)            |
| Thu | [Seaborn categorical plots](https://seaborn.pydata.org/tutorial/categorical.html)                 | [OpenCV – color conversions](https://docs.opencv.org/master/d8/d01/group__imgproc__color__conversions.html) |
| Fri | [Seaborn figure functions](https://seaborn.pydata.org/tutorial/function_overview.html)            | [OpenCV overlays](https://docs.opencv.org/master/d7/d1b/group__imgproc__misc.html)                          |
| Sat | Project: data visualizations                                                                      | Same in OpenCV                                                                                              |
| Sun | [nbviewer – share notebooks](https://nbviewer.org/)                                               | Commit code                                                                                                 |

---

## **Week 3 – SQL (Py) + SQLite C++ API**

| Day | Python                                                                                        | C++                                                      |
| --- | --------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| Mon | [sqlite3 Python docs](https://docs.python.org/3/library/sqlite3.html)                         | [SQLite C API intro](https://www.sqlite.org/cintro.html) |
| Tue | [SQL GROUP BY](https://www.sqltutorial.org/sql-group-by/)                                     | Implement in C++ API                                     |
| Wed | [SQL JOINs](https://www.sqltutorial.org/sql-join/)                                            | Implement in C++ API                                     |
| Thu | [SQL CASE & subqueries](https://www.sqltutorial.org/sql-case/)                                | Same in C++                                              |
| Fri | [SQL window functions](https://www.sqltutorial.org/sql-window-functions/)                     | Same                                                     |
| Sat | Practice dataset – [SQLite sample DB](https://www.sqlitetutorial.net/sqlite-sample-database/) | Same                                                     |
| Sun | Review & doc queries                                                                          | Same                                                     |

---

## **Week 4 – Statistics & Preprocessing (Py) + Eigen (C++)**

| Day | Python                                                                                           | C++                                                                          |
| --- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| Mon | [Python statistics module](https://docs.python.org/3/library/statistics.html)                    | [Eigen getting started](https://eigen.tuxfamily.org/dox/GettingStarted.html) |
| Tue | [Hypothesis testing intro](https://www.itl.nist.gov/div898/handbook/prc/section2/prc2.htm)       | Eigen math ops                                                               |
| Wed | [Correlation in pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html) | Compute correlation in Eigen                                                 |
| Thu | [Outlier detection – z-score](https://en.wikipedia.org/wiki/Standard_score)                      | Implement in Eigen                                                           |
| Fri | [Feature scaling – scikit-learn](https://scikit-learn.org/stable/modules/preprocessing.html)     | Implement MinMax in Eigen                                                    |
| Sat | Project: normalization pipeline                                                                  | Same                                                                         |
| Sun | [How to write tech blogs](https://simonwillison.net/2020/Jul/10/self-rewriting-readmes/)         | Same                                                                         |

---

# **Stage 2 — Core ML (Weeks 5–8)**

## **Week 5 – scikit-learn (Py) + mlpack (C++)**

| Day | Python                                                                                                                           | C++                                                                                                                |
| --- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Mon | [Linear regression – scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html) | [mlpack regression](https://www.mlpack.org/doc/stable/mlpack_tutorials.html#tutorial_regression)                   |
| Tue | [Logistic regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)            | [mlpack logistic regression](https://www.mlpack.org/doc/stable/mlpack_tutorials.html#tutorial_logistic_regression) |
| Wed | [Classification intro](https://scikit-learn.org/stable/supervised_learning.html)                                                 | [mlpack decision trees](https://www.mlpack.org/doc/stable/mlpack_tutorials.html#tutorial_decision_trees)           |
| Thu | [Pipelines](https://scikit-learn.org/stable/modules/compose.html)                                                                | mlpack preprocess + model                                                                                          |
| Fri | [Regression metrics](https://scikit-learn.org/stable/modules/model_evaluation.html)                                              | Implement metrics in C++                                                                                           |
| Sat | Spam classifier project                                                                                                          | Same                                                                                                               |
| Sun | Review results                                                                                                                   | Review results                                                                                                     |

---

## **Week 6 – Model tuning**

| Day | Python                                                                                                                  | C++                   |
| --- | ----------------------------------------------------------------------------------------------------------------------- | --------------------- |
| Mon | [Classification metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics)          | Manual metrics in C++ |
| Tue | [ROC/AUC](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html)                                  | Implement ROC in C++  |
| Wed | [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)             | Manual param sweep    |
| Thu | [RandomizedSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html) | Random sweep          |
| Fri | [Feature selection](https://scikit-learn.org/stable/modules/feature_selection.html)                                     | Feature selection C++ |
| Sat | Tuned classifier project                                                                                                | Same                  |
| Sun | Review & compare                                                                                                        | Review & compare      |

---

## **Week 7 – PyTorch (Py) + LibTorch (C++)**

| Day | Python                                                                                    | C++                                                                                            |
| --- | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Mon | [Tensors](https://pytorch.org/tutorials/beginner/introyt/tensors_deeper_tutorial.html)    | [LibTorch tensors](https://pytorch.org/cppdocs/tensors.html)                                   |
| Tue | [Define NN](https://pytorch.org/tutorials/beginner/nn_tutorial.html)                      | [LibTorch model definition](https://pytorch.org/cppdocs/frontend.html)                         |
| Wed | [Training loop](https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html)       | LibTorch training loop                                                                         |
| Thu | [Optimizers](https://pytorch.org/docs/stable/optim.html)                                  | [LibTorch optimizers](https://pytorch.org/cppdocs/api/structtorch_1_1optim_1_1_optimizer.html) |
| Fri | [Datasets & DataLoader](https://pytorch.org/tutorials/beginner/basics/data_tutorial.html) | LibTorch dataset API                                                                           |
| Sat | MNIST classifier                                                                          | Load trained model in C++                                                                      |
| Sun | Compare perf                                                                              | Compare perf                                                                                   |

---

## **Week 8 – Deployment basics**

| Day | Python                                                         | C++                                                           |
| --- | -------------------------------------------------------------- | ------------------------------------------------------------- |
| Mon | [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/)     | [gRPC C++ basics](https://grpc.io/docs/languages/cpp/basics/) |
| Tue | Model serving                                                  | Same                                                          |
| Wed | [Docker getting started](https://docs.docker.com/get-started/) | Same                                                          |
| Thu | Dockerize API                                                  | Dockerize gRPC service                                        |
| Fri | API testing – [Postman](https://learning.postman.com/)         | gRPC testing                                                  |
| Sat | Deploy spam model API                                          | Deploy gRPC inference                                         |
| Sun | Review & polish                                                | Review & polish                                               |

---

# **Stage 3 — Big Data, MLOps & Cloud (Weeks 9–12)**

## **Week 9 – Spark (Py) + Multithreading (C++)**

| Day | Python                                                                                      | C++                                                                   |
| --- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Mon | [PySpark intro](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) | [std::thread basics](https://en.cppreference.com/w/cpp/thread/thread) |
| Tue | PySpark DataFrames                                                                          | Thread loops                                                          |
| Wed | PySpark transforms                                                                          | Thread-safe data structures                                           |
| Thu | PySpark aggregations                                                                        | Parallel aggregations                                                 |
| Fri | PySpark joins                                                                               | Parallel joins                                                        |
| Sat | Large dataset project                                                                       | Same in C++ threads                                                   |
| Sun | Review & doc                                                                                | Review & doc                                                          |

---

## **Week 10 – Airflow (Py) + CLI Automation (C++)**

| Day | Python                                                                                       | C++                                                           |
| --- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Mon | [Airflow quickstart](https://airflow.apache.org/docs/apache-airflow/stable/start/index.html) | [C++ command-line parsing](https://cliutils.github.io/CLI11/) |
| Tue | DAG basics                                                                                   | Shell execution                                               |
| Wed | Operators                                                                                    | File manipulation                                             |
| Thu | Scheduling                                                                                   | Timed jobs                                                    |
| Fri | Dynamic DAGs                                                                                 | Config files                                                  |
| Sat | ML retrain pipeline                                                                          | CLI job runner                                                |
| Sun | Review & commit                                                                              | Review & commit                                               |

---

## **Week 11 – MLflow (Py) + Logging (C++)**

| Day | Python                                                                                     | C++                 |
| --- | ------------------------------------------------------------------------------------------ | ------------------- |
| Mon | [MLflow intro](https://mlflow.org/docs/latest/getting-started/intro-quickstart/index.html) | Logging basics      |
| Tue | Log params                                                                                 | Log to file         |
| Wed | Log metrics                                                                                | Log metrics to file |
| Thu | Save artifacts                                                                             | Save binary outputs |
| Fri | Compare runs                                                                               | Compare logs        |
| Sat | MLflow experiment project                                                                  | Log C++ runs        |
| Sun | Review & share                                                                             | Review & share      |

---

## **Week 12 – Cloud deployment**

| Day | Python                                                                                                                                                | C++                     |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| Mon | [AWS SageMaker intro](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) / [Vertex AI intro](https://cloud.google.com/vertex-ai/docs/start) | Cross-compiling for ARM |
| Tue | Deploy to SageMaker/Vertex                                                                                                                            | Deploy to Jetson/RPi    |
| Wed | API testing                                                                                                                                           | API testing             |
| Thu | Monitoring basics                                                                                                                                     | Health checks           |
| Fri | CI/CD basics – [GitHub Actions](https://docs.github.com/en/actions)                                                                                   | Auto-build scripts      |
| Sat | End-to-end ML pipeline (Py train → C++ deploy)                                                                                                        | Integrate with cloud    |
| Sun | Final polish                                                                                                                                          | Final polish            |
