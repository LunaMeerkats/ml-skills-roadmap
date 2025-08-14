# **Stage 1 — Foundations (Weeks 1–4)**

## **Week 1 – NumPy/pandas (Py) + STL basics (C++)**

| Day | Python                                    | C++                                   |
| --- | ----------------------------------------- | ------------------------------------- |
| Mon | NumPy arrays: creation, indexing, slicing | STL `vector`, loops, I/O basics       |
| Tue | NumPy broadcasting, math ops              | STL `map`, iterators, range-based for |
| Wed | pandas Series, DataFrame creation         | Read CSV into C++ (ifstream)          |
| Thu | pandas selection, filtering               | Parse CSV into vectors/maps           |
| Fri | pandas groupby, aggregation               | Simple aggregation (sum, avg)         |
| Sat | **Project:** CSV stats summary in pandas  | **Project:** Same in C++ STL          |
| Sun | Review + push to GitHub                   | Review + push to GitHub               |

---

## **Week 2 – Matplotlib/Seaborn (Py) + OpenCV plotting (C++)**

| Day | Python                             | C++                          |
| --- | ---------------------------------- | ---------------------------- |
| Mon | Matplotlib: line, bar, scatter     | OpenCV: image load, display  |
| Tue | Matplotlib customizations          | OpenCV: draw shapes, text    |
| Wed | Seaborn distplot, pairplot         | OpenCV: histograms           |
| Thu | Seaborn heatmap, boxplot           | OpenCV: color space changes  |
| Fri | Combine Matplotlib + Seaborn       | Combine OpenCV plot overlays |
| Sat | **Project:** Data histograms in Py | **Project:** Same in OpenCV  |
| Sun | Review + share notebook            | Review + commit C++ code     |

---

## **Week 3 – SQL (Py) + SQLite C++ API**

| Day | Python                            | C++                                 |
| --- | --------------------------------- | ----------------------------------- |
| Mon | `sqlite3` basics: SELECT, WHERE   | SQLite C API: connect, SELECT       |
| Tue | Aggregations, GROUP BY            | Execute aggregation queries         |
| Wed | Joins                             | Joins in SQLite C API               |
| Thu | Subqueries, CASE                  | Implement subqueries                |
| Fri | Window functions                  | Explore window queries              |
| Sat | **Project:** Query sales DB in Py | **Project:** Same in C++ SQLite API |
| Sun | Review & doc queries              | Review & doc queries                |

---

## **Week 4 – Statistics & Preprocessing (Py) + Eigen (C++)**

| Day | Python                                     | C++                        |
| --- | ------------------------------------------ | -------------------------- |
| Mon | Mean, median, variance                     | Eigen: matrix basics       |
| Tue | Hypothesis testing                         | Eigen: matrix math         |
| Wed | Correlation analysis                       | Eigen: correlation calc    |
| Thu | Outlier detection                          | Z-score in Eigen           |
| Fri | Scaling features                           | MinMax scaling in Eigen    |
| Sat | **Project:** Normalization in scikit-learn | **Project:** Same in Eigen |
| Sun | Review & blog write-up                     | Review & push code         |

---

# **Stage 2 — Core ML (Weeks 5–8)**

## **Week 5 – scikit-learn (Py) + mlpack (C++)**

| Day | Python                             | C++                                 |
| --- | ---------------------------------- | ----------------------------------- |
| Mon | Linear regression                  | mlpack: regression                  |
| Tue | Logistic regression                | mlpack: logistic regression         |
| Wed | Classification basics              | mlpack: decision tree               |
| Thu | Pipelines                          | mlpack: preprocess + model          |
| Fri | Metrics (RMSE, R²)                 | Manual metric calc                  |
| Sat | **Project:** Spam classifier in Py | **Project:** Spam classifier in C++ |
| Sun | Review & compare results           | Review & compare results            |

---

## **Week 6 – Model tuning**

| Day | Python                           | C++                               |
| --- | -------------------------------- | --------------------------------- |
| Mon | Accuracy, precision, recall      | Manual metrics in C++             |
| Tue | ROC/AUC plotting                 | ROC calc in C++                   |
| Wed | GridSearchCV                     | Manual param sweep                |
| Thu | RandomizedSearchCV               | Random param sweep                |
| Fri | Feature selection                | Feature selection in C++          |
| Sat | **Project:** Tuned classifier Py | **Project:** Tuned classifier C++ |
| Sun | Review & compare                 | Review & compare                  |

---

## **Week 7 – PyTorch (Py) + LibTorch (C++)**

| Day | Python                           | C++                                    |
| --- | -------------------------------- | -------------------------------------- |
| Mon | Tensors & ops                    | LibTorch tensors                       |
| Tue | Define NN                        | LibTorch: define NN                    |
| Wed | Training loop                    | LibTorch: forward, backward            |
| Thu | Optimizers                       | LibTorch: SGD/Adam                     |
| Fri | Datasets/loaders                 | LibTorch: dataset API                  |
| Sat | **Project:** MNIST classifier Py | **Project:** Load trained model in C++ |
| Sun | Review & compare perf            | Review & compare perf                  |

---

## **Week 8 – Deployment basics**

| Day | Python                             | C++                                |
| --- | ---------------------------------- | ---------------------------------- |
| Mon | FastAPI basics                     | gRPC basics                        |
| Tue | Serve model                        | Serve model                        |
| Wed | Docker basics                      | Docker basics                      |
| Thu | Dockerize API                      | Dockerize C++ service              |
| Fri | Test API                           | Test gRPC                          |
| Sat | **Project:** Deploy spam model API | **Project:** Deploy gRPC inference |
| Sun | Review & polish                    | Review & polish                    |

---

# **Stage 3 — Big Data, MLOps & Cloud (Weeks 9–12)**

## **Week 9 – Spark (Py) + Multithreading (C++)**

| Day | Python                        | C++                              |
| --- | ----------------------------- | -------------------------------- |
| Mon | PySpark setup                 | std::thread basics               |
| Tue | PySpark DataFrames            | Threaded loop                    |
| Wed | PySpark transforms            | Thread-safe data structures      |
| Thu | PySpark aggregations          | Parallel aggregations            |
| Fri | PySpark joins                 | Parallel joins                   |
| Sat | **Project:** Process 1M+ rows | **Project:** Same in C++ threads |
| Sun | Review & doc                  | Review & doc                     |

---

## **Week 10 – Airflow (Py) + CLI Automation (C++)**

| Day | Python                           | C++                         |
| --- | -------------------------------- | --------------------------- |
| Mon | Airflow setup                    | CLI arg parsing             |
| Tue | DAG basics                       | Shell command execution     |
| Wed | Operators                        | File manipulation           |
| Thu | Scheduling                       | Timed jobs                  |
| Fri | Dynamic DAGs                     | Config files                |
| Sat | **Project:** ML retrain pipeline | **Project:** CLI job runner |
| Sun | Review & commit                  | Review & commit             |

---

## **Week 11 – MLflow (Py) + Logging (C++)**

| Day | Python                            | C++                       |
| --- | --------------------------------- | ------------------------- |
| Mon | MLflow setup                      | Logging basics            |
| Tue | Log params                        | Log to file               |
| Wed | Log metrics                       | Log metrics to file       |
| Thu | Save artifacts                    | Save binary outputs       |
| Fri | Compare runs                      | Compare logs              |
| Sat | **Project:** MLflow experiment Py | **Project:** Log C++ runs |
| Sun | Review & share                    | Review & share            |

---

## **Week 12 – Cloud deployment**

| Day | Python                                                         | C++                   |
| --- | -------------------------------------------------------------- | --------------------- |
| Mon | AWS/GCP setup                                                  | Cross-compile for ARM |
| Tue | Deploy to SageMaker                                            | Deploy to Jetson/RPi  |
| Wed | API test                                                       | API test              |
| Thu | Monitoring basics                                              | Health checks         |
| Fri | CI/CD basics                                                   | Auto-build scripts    |
| Sat | **Final Project:** End-to-end pipeline (Py train → C++ deploy) | Integrate with cloud  |
| Sun | Final polish                                                   | Final polish          |

---

## 🔹 Extra Notes

* **Daily Git pushes** → Keep Python & C++ repos separate but linked in a README.
* **Language switching rule:** Always code the Python version first for clarity, then port to C++.
* **Performance checks:** Whenever possible, time both implementations.
