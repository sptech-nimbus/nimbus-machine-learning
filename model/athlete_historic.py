class AthleteHistoric:
    def __init__(self,
                 id,
                 observations,
                 minutes,
                 athlete,
                 offRebounds, 
                 defRebounds,
                 gameId,
                 blocks, 
                 fouls,
                 trainingId,
                 turnovers, 
                 assists, 
                 freeThrowConverted, 
                 freeThrowAttemped,
                 steals,
                 threePointsConverted,
                 threePointsAttemped,
                 twoPointsConverted,
                 twoPointsAttemped):
        self.id = id
        self.observations = observations
        self.athlete = athlete
        self.gameId = gameId
        trainingId = trainingId
        self.minutes = minutes or 0
        self.offRebounds = offRebounds or 0
        self.defRebounds = defRebounds or 0
        self.blocks = blocks or 0
        self.fouls = fouls or 0
        self.turnovers = turnovers or 0
        self.assists = assists or 0
        self.freeThrowConverted = freeThrowConverted or 0
        self.freeThrowAttemped = freeThrowAttemped or 0
        self.steals = steals or 0
        self.threePointsConverted = threePointsConverted or 0
        self.threePointsAttemped = threePointsAttemped or 0
        self.twoPointsConverted = twoPointsConverted or 0
        self.twoPointsAttemped = twoPointsAttemped or 0

    def info(self):
        return (f"Off Rebounds: {self.offRebounds}, Def Rebounds: {self.defRebounds}, "
                f"Blocks: {self.blocks}, Fouls: {self.fouls}, Turnovers: {self.turnovers}, "
                f"Assists: {self.assists}, Free Throws: {self.freeThrowConverted}/{self.freeThrowAttemped}, "
                f"Steals: {self.steals}, 3-Points: {self.threePointsConverted}/{self.threePointsAttemped}, "
                f"2-Points: {self.twoPointsConverted}/{self.twoPointsAttemped}")

class AthleteHistoricAVG:
    def __init__(self,
                 offRebounds, 
                 defRebounds,
                 blocks,
                 fouls,
                 turnovers,
                 assists, 
                 freeThrowConverted, 
                 freeThrowAttemped,
                 steals,
                 threePointsConverted,
                 threePointsAttemped,
                 twoPointsConverted,
                 twoPointsAttemped):
        self.offRebounds = offRebounds
        self.defRebounds = defRebounds
        self.blocks = blocks
        self.fouls = fouls
        self.turnovers = turnovers
        self.assists = assists
        self.freeThrowConverted = freeThrowConverted
        self.freeThrowAttemped = freeThrowAttemped
        self.steals = steals
        self.threePointsConverted = threePointsConverted
        self.threePointsAttemped = threePointsAttemped
        self.twoPointsConverted = twoPointsConverted
        self.twoPointsAttemped = twoPointsAttemped

    def info(self):
        return (f"Off Rebounds: {self.offRebounds}, Def Rebounds: {self.defRebounds}, "
                f"Blocks: {self.blocks}, Fouls: {self.fouls}, Turnovers: {self.turnovers}, "
                f"Assists: {self.assists}, Free Throws: {self.freeThrowConverted}/{self.freeThrowAttemped}, "
                f"Steals: {self.steals}, 3-Points: {self.threePointsConverted}/{self.threePointsAttemped}, "
                f"2-Points: {self.twoPointsConverted}/{self.twoPointsAttemped}")