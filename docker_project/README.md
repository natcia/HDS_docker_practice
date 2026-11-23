# Mock decision-tree evaluation
Invented ECG features, ages and labels; not a medical model.
Start Docker Desktop, then run these commands inside docker_project:

    docker build -t semester-project .
    docker run --rm semester-project

Expected confusion matrix: [[2, 1], [1, 2]].
Rows = actual classes 0, 1; columns = predicted classes 0, 1.
Rebuild after changing project files. Only load model files you trust.
