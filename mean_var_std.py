import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(numbers).reshape((3,3))
    
    calculations = {
        'mean': [
            list(np.mean(matrix, axis=0)),
            list(np.mean(matrix, axis=1)),
            np.mean(matrix).item()
        ],
        'variance': [
            list(np.var(matrix, axis=0)),
            list(np.var(matrix, axis=1)),
            np.var(matrix).item()
        ],
        'standard deviation': [
            list(np.std(matrix, axis=0)),
            list(np.std(matrix, axis=1)),
            np.std(matrix).item()
        ],
        'max': [
            list(np.max(matrix, axis=0)),
            list(np.max(matrix, axis=1)),
            np.max(matrix).item()
        ],
        'min': [
            list(np.min(matrix, axis=0)),
            list(np.min(matrix, axis=1)),
            np.min(matrix).item()
        ],
        'sum': [
            list(np.sum(matrix, axis=0)),
            list(np.sum(matrix, axis=1)),
            np.sum(matrix).item()
        ]
    }
    
    return calculations
