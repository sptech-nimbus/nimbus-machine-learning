from flask import Flask, request, jsonify, Response
from model.athlete_historic import AthleteHistoric, AthleteHistoricAVG
app = Flask(__name__)

@app.post('/generate-forecast')
def home():
    data = request.get_json()

    challenger_historics = generate_historic_list(data.get('challengerHistorics', []))
    challenged_historics = generate_historic_list(data.get('challengedHistorics', []))

    challenger_avg = generate_historic_avg(challenger_historics)
    challenged_avg = generate_historic_avg(challenged_historics)

    return data

def generate_historic_list(historics):
    historic_list = []

    for historic in historics:
        historic = AthleteHistoric(**historic)
        historic_list.append(historic)
    
    return historic_list

def generate_historic_avg(historics):
    offReboundsAVG = 0
    defReboundsAVG = 0
    blocksAVG = 0
    foulsAVG = 0
    turnoversAVG = 0
    assistsAVG = 0
    freeThrowConvertedAVG = 0
    freeThrowAttempedAVG = 0
    stealsAVG = 0
    threePointsConvertedAVG = 0
    threePointsAttempedAVG = 0
    twoPointsConvertedAVG = 0
    twoPointsAttempedAVG = 0

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

    return AthleteHistoricAVG(
        round(offReboundsAVG / len(historics), 2),
        round(defReboundsAVG / len(historics), 2),
        round(blocksAVG / len(historics), 2),
        round(foulsAVG / len(historics), 2),
        round(turnoversAVG / len(historics), 2),
        round(assistsAVG / len(historics), 2),
        round(freeThrowConvertedAVG / len(historics), 2),
        round(freeThrowAttempedAVG / len(historics), 2),
        round(stealsAVG / len(historics), 2),
        round(threePointsConvertedAVG / len(historics), 2),
        round(threePointsAttempedAVG / len(historics), 2),
        round(twoPointsConvertedAVG / len(historics), 2),
        round(twoPointsAttempedAVG / len(historics), 2)
    )

app.run(debug=True, port=5729)