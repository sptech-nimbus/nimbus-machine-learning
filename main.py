from flask import Flask, request, jsonify

app = Flask(__name__)

# Função para calcular os pontos de cada atleta e a soma total
def calculate_statistics(challenger_historics, challenged_historics):
    total_points_Challenger = 0  # Soma total de pontos
    total_players_Challenger = 0  # Contador de atletas

    total_points_Challenged = 0  # Soma total de pontos
    total_players_Challenged = 0  # Contador de atletas

    # Calculando para o time Challenger
    for athlete_historic in challenger_historics:
        points = (athlete_historic["twoPointsConverted"] * 2) + (athlete_historic["threePointsConverted"] * 3)
        total_points_Challenger += points

    # Calculando para o time Challenged
    for athlete_historic in challenged_historics:
        points = (athlete_historic["twoPointsConverted"] * 2) + (athlete_historic["threePointsConverted"] * 3)
        total_points_Challenged += points


    print("pontos challenger" ,  total_points_Challenger)
    print("pontos challenged" , total_points_Challenged)


    tot_points_teams = total_points_Challenger + total_points_Challenged;

    formatted_tot_points_teams = round(tot_points_teams, 2);

    print(formatted_tot_points_teams);

    # Calculando a média de pontos
    average_points_Challenger = total_points_Challenger 
    average_points_Challenged = total_points_Challenged 

    # Inicializando opponent_points (a média do time adversário)
    # opponent_points_Challenged = 100  # Média do time Challenger
    # opponent_points_Challenger = 100 # Média do time Challenged

    # Calculando a porcentagem de vitória
    win_percentage_Challenger = (average_points_Challenger / (average_points_Challenger + average_points_Challenged)) * 100
    win_percentage_Challenged = (average_points_Challenged / (average_points_Challenger + average_points_Challenged)) * 100

    formatted_win_percentage_Challenger = round(win_percentage_Challenger, 2)
    formatted_win_percentage_Challenged = round(win_percentage_Challenged, 2)

    # Retornando os resultados
    return {
        "ChallengerWinPercentage": formatted_win_percentage_Challenger,
        "ChallengedWinPercentage": formatted_win_percentage_Challenged
    }

@app.route('/generate-forecast', methods=['POST'])
def generate_forecast():
    try:
        # Recebe os dados JSON da requisição
        data = request.get_json()
        challenger_historics = data["challengerHistorics"]  # Acessando o histórico do time Challenger
        challenged_historics = data["challengedHistorics"]  # Acessando o histórico do time Challenged

        # Realiza os cálculos para ambos os times
        results = calculate_statistics(challenger_historics, challenged_historics)

        print("Resultados calculados:", results)

        # Retorna os resultados como JSON
        return jsonify(results), 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True, port=5729)
