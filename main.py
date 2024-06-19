import csv
import matplotlib.pyplot as plt
import statistics

def load_data_from_csv(csv_file):
    data = []
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def generate_report(data):
    reports = ["ID, Name, Score"]
    for row in data:
        report_line = f"{row['ID']}, {row['Name']}, {row['Score']}"
        reports.append(report_line)
    return reports

def save_reports_to_file(reports, output_file):
    with open(output_file, 'w') as file:
        for report in reports:
            file.write(report + "\n")

def generate_graph(data):
    ids = [row['ID'] for row in data]
    scores = [int(row['Score']) for row in data]

    plt.figure(figsize=(10, 5))
    plt.bar(ids, scores, color='blue')
    plt.xlabel('ID')
    plt.ylabel('Score')
    plt.title('Scores par ID')
    plt.savefig('scores_graph.png')
    plt.show()

def generate_statistics(data):
    scores = [int(row['Score']) for row in data]

    mean_score = statistics.mean(scores)
    median_score = statistics.median(scores)
    stdev_score = statistics.stdev(scores)

    return {
        'mean': mean_score,
        'median': median_score,
        'stdev': stdev_score
    }

def save_statistics_to_file(statistics, output_file):
    with open(output_file, 'w') as file:
        file.write("Statistiques des scores:\n")
        file.write(f"Moyenne: {statistics['mean']}\n")
        file.write(f"Médiane: {statistics['median']}\n")
        file.write(f"Écart-type: {statistics['stdev']}\n")

def main():
    csv_file = 'data.csv'
    report_file = 'reports.txt'
    stats_file = 'statistics.txt'

    data = load_data_from_csv(csv_file)

    reports = generate_report(data)

    save_reports_to_file(reports, report_file)

    generate_graph(data)

    stats = generate_statistics(data)

    save_statistics_to_file(stats, stats_file)

    print("Les rapports ont été générés et sauvegardés, le graphique a été créé, et les statistiques ont été calculées et sauvegardées.")

if __name__ == "__main__":
    main()
