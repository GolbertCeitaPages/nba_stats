from raw_extract_kaggle_data import getkaggle_data
from raw_transform_nba_data import drop_columns,replace_na,remove_rows,merge_frames,divide_columns
from raw_load_kaggle_data import insert_data

def trigger_opponent_p(opponent_stats_per_100_poss=False,
                       opponent_stats_per_game=False,
                       opponent_totals=False):
    # load data into all dataframes
    if opponent_stats_per_100_poss == True:
        df_Opponent_Stats_Per_100_Poss = getkaggle_data('Opponent Stats Per 100 Poss.csv')
        print("Opponent Stats per 100 Possessions EXTRACTED")
        df_Opponent_Stats_Per_100_Poss = replace_na(df_Opponent_Stats_Per_100_Poss,['opp_x3p_per_100_poss','opp_x3pa_per_100_poss','opp_x3p_percent'],'float')
        print("Opponent Stats per 100 Possessions TRANSFORMED")
        insert_data(df_Opponent_Stats_Per_100_Poss,"opponent_stats_per_100_poss")
        print("Opponent Stats per 100 Possessions LOADED")

    if opponent_stats_per_game == True:
        df_Opponent_Stats_Per_Game = getkaggle_data('Opponent Stats Per Game.csv')
        print("Opponent Stats per Game EXTRACTED")
        df_Opponent_Stats_Per_Game = replace_na(df_Opponent_Stats_Per_Game,['opp_fg_per_game','opp_fga_per_game','opp_fg_percent',
                                                                        'opp_x3p_per_game','opp_x3pa_per_game','opp_x3p_percent',
                                                                        'opp_x2p_per_game','opp_x2pa_per_game','opp_x2p_percent',
                                                                        'opp_ft_per_game','opp_fta_per_game','opp_ft_percent',
                                                                        'opp_orb_per_game','opp_drb_per_game','opp_trb_per_game',
                                                                        'opp_ast_per_game','opp_stl_per_game','opp_blk_per_game',
                                                                        'opp_tov_per_game','opp_pf_per_game'],'float')
        df_Opponent_Stats_Per_Game = remove_rows(df_Opponent_Stats_Per_Game,'team','League Average')
        print("Opponent Stats per Game TRANSFORMED")
        insert_data(df_Opponent_Stats_Per_Game,"opponent_stats_per_game")
        print("Opponent Stats per Game LOADED")

    if opponent_totals == True:
        df_Opponent_Totals = getkaggle_data('Opponent Totals.csv')
        print("Opponent Stats EXTRACTED")
        df_Opponent_Totals = replace_na(df_Opponent_Totals,['opp_fg','opp_fga','opp_fg_percent',
                                                            'opp_x3p','opp_x3pa','opp_x3p_percent',
                                                            'opp_x2p','opp_x2pa','opp_x2p_percent',
                                                            'opp_ft','opp_fta','opp_ft_percent',
                                                            'opp_orb','opp_drb','opp_trb',
                                                            'opp_ast','opp_stl','opp_blk',
                                                            'opp_tov','opp_pf'],'float')
        df_Opponent_Totals = remove_rows(df_Opponent_Totals,'team','League Average')
        print("Opponent Stats TRANSFORMED")
        insert_data(df_Opponent_Totals,"opponent_totals")
        print("Opponent Stats LOADED")

    print("Pipeline completed successfully!")