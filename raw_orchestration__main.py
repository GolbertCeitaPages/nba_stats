from raw_orchestration_player import trigger_player_p
from raw_orchestration_opponent import trigger_opponent_p
from raw_orchestration_team import trigger_team_p
from raw_orchestration_award_misc import trigger_award_p


def trigger():
    trigger_player_p(True,True,True,True,True,True,True,True)
    trigger_opponent_p(True,True,True)
    trigger_team_p(True,True,True,True)
    trigger_award_p(True,True,True,True,True,True)
    


if __name__ == "__main__":
    trigger()