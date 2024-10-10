import numpy as np
import matplotlib.pyplot as plt

def buildA(order, xs):
    A = np.empty((0, len(xs)))
    for i in range(order + 1):
        A = np.vstack((xs**i, A))
    return A.T

if __name__ == '__main__':
    midterm_range = np.array([0, 125])
    final_range = np.array([0, 100])

    # Load score data
    class_kr = np.loadtxt('week5/data/class_score_kr.csv', delimiter=',')
    class_en = np.loadtxt('week5/data/class_score_en.csv', delimiter=',')
    data = np.vstack((class_kr, class_en))

    midterm_scores = data[:, 0]
    final_scores = data[:, 1]
            
    A = buildA(1, midterm_scores)  
    coeff = np.linalg.pinv(A) @ final_scores  
    slope = coeff[0]
    y_intercept = coeff[1]
    line = [slope, y_intercept]

    # Pradict scores
    final = lambda midterm: line[0] * midterm + line[1]
    
    # Plot scores and the estimated line
    while True:
        try:
            given = input('Q) Please input your midterm score (Enter or -1: exit)? ')
            if given == '' or float(given) < 0:
                break
            print(f'A) Your final score is expected to {final(float(given)):.3f}.')
        except Exception as ex:
            print(f'Cannot answer the question. (message: {ex})')
            break

    plt.figure()
    plt.plot(data[:, 0], data[:, 1], 'r.', label='The given data')
    plt.plot(midterm_range, final(midterm_range), 'b-', label='Prediction')
    plt.xlabel('Midterm scores')
    plt.ylabel('Final scores')
    plt.xlim(midterm_range)
    plt.ylim(final_range)
    plt.grid()
    plt.legend()
    plt.show()
