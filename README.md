# SubGraph_DP_NAM
This is a source code.

# Directory Structure

- Algorithms/  python codes.
- Datasets/  text files.
- Drawing pictures/  python codes.
- Experimental Results/  text files.

# Usage

(1) Users may directly utilize the facebook or CA-AstroPh datasets available within the `Datasets`. Alternatively, they can download any dataset from https://snap.stanford.edu/index.html. It is important to note that the datasets are formatted as edge lists, which are text files structured as follows:

user1 user2

user3 user4

...

Comments, if any, are permitted at the beginning of the file and are denoted by a hash symbol (#).

(2) Replace the `file_path` in the Python script within the `Algorithms` directory with the path to the desired dataset you wish to analyze. Subsequently, execute the corresponding Python program to obtain the experimental results.

Within the `Algorithms` directory, there are four folders, each representing a distinct algorithm:

- **2STAR**: This algorithm is designed to address the statistical problem of counting 2-stars within a graph.
- **TriOR (Triangle's One Round Algorithm)**: This is a triangle counting algorithm that operates with a single round of queries.
- **TriTR (Triangle's Two Round Algorithm)**: This algorithm extends the triangle counting process to two rounds of queries.
- **TriMTR (Triangle's Modified Two Round Algorithm)**: An optimized version of TriTR, this algorithm reduces the amount of data transmission required.
- **QuaTR (Quadrangle's Two Round Algorithm)**: This algorithm is tailored for counting quadrangles and involves two rounds of queries.

For the latter three algorithms, which are two-round algorithms, the process is segmented into several blocks to clearly identify the primary sources of statistical error. Taking TriTR as an example:

- **TriTR_0**: Represents the data structure without the addition of noise in the second round.
- **TriTR_1**: Builds upon TriTR_0 by incorporating the output from GraphProjection, which ensures the privacy of the graph's edges at the outset.
- **TriTR_2**: Further extends TriTR_1 by introducing noise in the second round, culminating in the output that represents the complete TriTR algorithm as detailed in the paper.

TriTR_2 embodies the full TriTR algorithm as presented in the academic paper, incorporating all necessary privacy-preserving measures and noise addition to safeguard the integrity of the data throughout the two-round query process.

To distinguish between the **Randomized Response** and **Laplace Mechanism**, we have implemented separate Python programs for each triangle and quadrangle counting algorithm, utilizing the corresponding mechanism. For instance, in the case of **TriOR**, the programs are named as follows:  

- **TriOR_RR**: Implements the **Randomized Response** mechanism.  
- **TriOR_Lap**: Implements the **Laplace Mechanism**.  

This naming convention is consistently applied across all algorithms to clearly indicate the privacy-preserving mechanism employed. For example:  
- For **TriTR**:  
  - **TriTR_RR**: Randomized Response version.  
  - **TriTR_Lap**: Laplace Mechanism version.  
- For **QuaTR**:  
  - **QuaTR_RR**: Randomized Response version.  
  - **QuaTR_Lap**: Laplace Mechanism version.  

This approach allows for a clear comparison of the performance and accuracy of each mechanism within the context of the respective algorithms.

(3) To compare the performance of different algorithms, you can use the programs provided in the **`Drawing pictures`** directory to generate comparative graphs. After obtaining the experimental results, follow these steps to create **$\epsilon$ - Relative Error** plots, which visually illustrate the accuracy of each algorithm.

The existing data is retrieved from the **`Experimental Results`** directory, which is organized into two subfolders based on the datasets: **`Facebook`** and **`CA-AstroPh`**. Each folder contains the experimental results for the aforementioned algorithms. For example, the file **`QuaTR_RR_2.txt`** corresponds to the results generated by running the **`QuaTR_RR_2.py`** script. 

It is important to note that there are also files like **`QuaTR_RR_0.8.txt`**, which represent the experimental results obtained by scaling the privacy budget **`epsilon_list`** in **`QuaTR_RR_0.py`** by a factor of **0.8**. This scaling is done to study the impact of varying privacy budgets on the algorithm's performance and accuracy. 


# Execution Environment

Python version: 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)]

Python implementation: CPython

Python compiler: MSC v.1937 64 bit (AMD64)

OS: Windows 11

Processor: Intel64 Family 6 Model 165 Stepping 2, GenuineIntel

Machine: AMD64

Platform: Windows-11-10.0.22631-SP0

# External Libraries used in our source code
- math

- numpy

- time

- scipy.stats

All the required libraries can be easily installed using the `pip install ...` command.
