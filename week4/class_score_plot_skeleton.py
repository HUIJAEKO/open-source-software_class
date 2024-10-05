import matplotlib.pyplot as plt

def read_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            if not line.startswith('#'): #
                data.append([int(word) for word in line.split(',')])
    return data

if __name__ == '__main__':
    # Load score data
    class_kr = read_data('week4/data/class_score_kr.csv')
    class_en = read_data('week4/data/class_score_en.csv')

    # Prepare midterm, final, and total scores for KR
    midterm_kr, final_kr = zip(*class_kr)
    total_kr = [40/125 * midterm + 60/100 * final for (midterm, final) in class_kr]

    # Prepare midterm, final, and total scores for EN
    midterm_en, final_en = zip(*class_en)
    total_en = [40/125 * midterm + 60/100 * final for (midterm, final) in class_en]

    # Plot midterm/final scores as points
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.scatter(midterm_kr, final_kr, color='red', label='KR')
    plt.scatter(midterm_en, final_en, color='blue', label='EN')
    plt.title('Midterm, Final Scores')
    plt.xlabel('Midterm Scores')
    plt.ylabel('Final Scores')
    plt.legend()
    plt.ylim(0, 100)
    plt.xlim(0, 125)
    plt.grid(True)  

    # Plot total scores as a histogram
    plt.subplot(1, 2, 2)
    bins = range(0, 105, 5) 
    plt.hist(total_kr, bins=bins, color='red', label='KR')
    plt.hist(total_en, bins=bins, color='blue', label='EN')
    plt.title('Total Scores')
    plt.xlabel('Total Score')
    plt.ylabel('The number of Students')
    plt.xlim(0, 100)  
    plt.ylim(0, 8)    
    plt.legend()

    plt.tight_layout()
    plt.show()