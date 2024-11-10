from flask import Flask, request, jsonify
from model.athlete_historic import AthleteHistoric, AthleteHistoricAVG

app = Flask(__name__)

import pickle
with open('modelo.pkl', 'rb') as f:
    modelo = pickle.load(f)

@app.post('/generate-forecast')
def home():
    data = request.get_json()

    challenger_historics = generate_historic_list(data.get('challengerHistorics', []))
    challenged_historics = generate_historic_list(data.get('challengedHistorics', []))

    challenger_avg = generate_historic_avg(challenger_historics)
    challenged_avg = generate_historic_avg(challenged_historics)

    entrada = [[
        challenger_avg.twoPointsConverted, 
        challenged_avg.twoPointsConverted
    ]]
    
    probabilidade = modelo.predict_proba(entrada)[0] 
    probabilidade_desafiante = round(probabilidade[1] * 100, 2)
    probabilidade_desafiado = round(probabilidade[0] * 100, 2)

    return jsonify({
        "challenger_avg": challenger_avg.info(),
        "challenged_avg": challenged_avg.info(),
        "forecast": {
            "challengerWinProbability": f"{probabilidade_desafiante}%",
            "challengedWinProbability": f"{probabilidade_desafiado}%"
        }
    })

def generate_historic_list(historics):
    historic_list = []
    for historic in historics:
        historic = AthleteHistoric(**historic)
        historic_list.append(historic)

    return historic_list

def generate_historic_avg(historics):
    if not historics:
        return AthleteHistoricAVG(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    
    offReboundsAVG = defReboundsAVG = blocksAVG = foulsAVG = turnoversAVG = assistsAVG = 0
    freeThrowConvertedAVG = freeThrowAttempedAVG = stealsAVG = threePointsConvertedAVG = 0
    threePointsAttempedAVG = twoPointsConvertedAVG = twoPointsAttempedAVG = 0

    for historic in historics:
        offReboundsAVG += historic.offRebounds
        defReboundsAVG += historic.defRebounds
        blocksAVG += historic.blocks
        foulsAVG += historic.fouls
        turnoversAVG += historic.turnovers
        assistsAVG += historic.assists
        freeThrowConvertedAVG += historic.freeThrowConverted
        freeThrowAttempedAVG += historic.freeThrowAttemped
        stealsAVG += historic.steals
        threePointsConvertedAVG += historic.threePointsConverted
        threePointsAttempedAVG += historic.threePointsAttemped
        twoPointsConvertedAVG += historic.twoPointsConverted
        twoPointsAttempedAVG += historic.twoPointsAttemped

    total = len(historics)
    return AthleteHistoricAVG(
        round(offReboundsAVG / total, 2),
        round(defReboundsAVG / total, 2),
        round(blocksAVG / total, 2),
        round(foulsAVG / total, 2),
        round(turnoversAVG / total, 2),
        round(assistsAVG / total, 2),
        round(freeThrowConvertedAVG / total, 2),
        round(freeThrowAttempedAVG / total, 2),
        round(stealsAVG / total, 2),
        round(threePointsConvertedAVG / total, 2),
        round(threePointsAttempedAVG / total, 2),
        round(twoPointsConvertedAVG / total, 2),
        round(twoPointsAttempedAVG / total, 2)
    )

app.run(debug=True, port=5729)
