from raw_extract_kaggle_data import getkaggle_data
from raw_transform_nba_data import drop_columns,replace_na,remove_rows,merge_frames,divide_columns
from raw_load_kaggle_data import insert_data

def trigger_team_p(team_stats=False,
                   team_stats_per_game=False,
                   team_summaries=False,
                   team_totals=False):
    
    if team_stats == True:
        # load data into dataframe    
        df_Team_Stats_Per_100_Poss = getkaggle_data('Team Stats Per 100 Poss.csv')
        print('Team Stats Per 100 Poss EXTRACTED!')
        # Transform team stats per 100 poss
        df_Team_Stats_Per_100_Poss = replace_na(df_Team_Stats_Per_100_Poss,['x3p_per_100_poss','x3pa_per_100_poss','x3p_percent'],'float')
        print('Team Stats Per 100 Poss TRANSFORMED!')
        # Insert data into the table
        insert_data(df_Team_Stats_Per_100_Poss,"team_stats_per_100_poss")
        print('Team Stats Per 100 Poss LOADED!')

    if team_stats_per_game == True:
        df_Team_Stats_Per_Game = getkaggle_data('Team Stats Per Game.csv')
        print('Team Stats Per Game EXTRACTED!')
        df_Team_Stats_Per_Game = replace_na(df_Team_Stats_Per_Game,['mp_per_game',
                                                                    'x3p_per_game','x3pa_per_game','x3p_percent',
                                                                    'orb_per_game','drb_per_game','trb_per_game',
                                                                    'stl_per_game','blk_per_game','tov_per_game'],'float')
        print('Team Stats Per Game TRANSFORMED!')
        insert_data(df_Team_Stats_Per_Game,"team_stats_per_game")
        print('Team Stats Per Game LOADED!')

    if team_summaries == True:
        df_Team_Summaries = getkaggle_data('Team Summaries.csv')
        print('Team Summaries EXTRACTED!')
        df_Team_Summaries = replace_na(df_Team_Summaries,['age','w','l',
                                                          'o_rtg','d_rtg','n_rtg',
                                                          'pace','x3p_ar','tov_percent',
                                                          'orb_percent','opp_e_fg_percent','opp_tov_percent',
                                                          'opp_drb_percent','opp_ft_fga','attend','attend_g'],'float')
        df_Team_Summaries = replace_na(df_Team_Summaries,['arena'])
        df_Team_Summaries = remove_rows(df_Team_Summaries,'team','League Average')
        print('Team Summaries TRANSFORMED!')
        insert_data(df_Team_Summaries,"team_summaries")
        print('Team Summaries LOADED!')
    
    if team_totals == True:
        df_Team_Totals = getkaggle_data('Team Totals.csv')
        print('Team Totals EXTRACTED!')
        df_Team_Totals = replace_na(df_Team_Totals,['mp',
                                                    'x3p','x3pa','x3p_percent',
                                                    'orb','drb','trb','stl',
                                                    'blk','tov'],'float')
        df_Team_Totals = remove_rows(df_Team_Totals,'team','League Average')
        print('Team Totals TRANSFORMED!')
        insert_data(df_Team_Totals,"team_totals")
        print('Team Totals LOADED!')
    print("Pipeline completed successfully!")