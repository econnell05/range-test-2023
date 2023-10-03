range-test-2023
==============================

A short description of your project

Project Organization
--------------------

    .
    ├── AUTHORS.md
    ├── LICENSE
    ├── README.md
    ├── bin
    ├── config
    ├── data
    │   ├── external
    │   ├── interim
    │   ├── processed
    │   └── raw
    ├── docs
    ├── notebooks
    ├── reports
    │   └── figures
    └── src
        ├── data
        ├── external
        ├── models
        ├── tools
        └── visualization


## Scenario 

### Scenario 1
 - Parameters: [[-3, 0], [0, 4.5]]
 - Result: [0, 0]
 ### Scenario 2
 - Parameters: [[-3, -1], [0, 4.5]]
 - Result: "No Overlap" 

### Scenario 3
- Parameters: [-3, 1]
- Result: "Enter at least 2 ranges"

### Scenario 4
 - Parameters: [[-3, 2], [0, 4.5]]
 - Result: [-3, 2] 

 ### Scenario 5
 - Parameters: [[-3, 5], [0, 4.5], [-1, 2]]
 - Result: [0, 2] 