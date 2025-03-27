from raw_extract_kaggle_data import getkaggle_data
from raw_transform_nba_data import drop_columns,replace_na,remove_rows,merge_frames,divide_columns
from raw_load_kaggle_data import insert_data

def trigger_player_p(advanced=False,
                     per_100_poss=False,
                     per_36_minutes=False,
                     player_per_game=False,
                     player_play_by_play=False,
                     player_season_info=False,
                     player_shooting=False,
                     player_totals=False):
    
    if advanced == True:
        df_Advanced = getkaggle_data('Advanced.csv')
        print("Advanced EXTRACTED")
        df_Advanced = drop_columns(df_Advanced,['birth_year'])
        df_Advanced = replace_na(df_Advanced,['ts_percent','x3p_ar','f_tr',
                                              'orb_percent','drb_percent','trb_percent',
                                              'ast_percent','stl_percent','blk_percent','tov_percent','usg_percent',
                                              'ws_48','obpm','dbpm','bpm','vorp'],'float')
        df_Advanced = divide_columns(df_Advanced,['orb_percent','drb_percent','trb_percent','ast_percent',
                                                  'stl_percent','blk_percent','tov_percent','usg_percent'])
        print("Advanced TRANSFORMED")
        insert_data(df_Advanced, "advanced")
        print("Advanced LOADED")

    if per_100_poss == True:
        df_Per_100_Poss = getkaggle_data('Per 100 Poss.csv')
        print("Player per 100 Possessions EXTRACTED")
        df_Per_100_Poss = replace_na(df_Per_100_Poss,['gs','mp',
                                                      'x3p_per_100_poss','x3pa_per_100_poss','x3p_percent',
                                                      'ft_percent','tov_per_100_poss','o_rtg','d_rtg'],'float')
        df_Per_100_Poss = drop_columns(df_Per_100_Poss,['birth_year'])
        print("Player per 100 Possessions TRANSFORMED")
        insert_data(df_Per_100_Poss,"per_100_poss")
        print("Player per 100 Possessions LOADED")

    if per_36_minutes == True:
        df_Per_36_Minutes = getkaggle_data('Per 36 Minutes.csv')
        print("Player per 36 Minutes EXTRACTED")
        df_Per_36_Minutes = replace_na(df_Per_36_Minutes,['gs','mp',
                                                          'fg_per_36_min','fga_per_36_min',
                                                          'x3p_per_36_min','x3pa_per_36_min','x3p_percent',
                                                          'x2p_per_36_min','x2pa_per_36_min',
                                                          'ft_per_36_min','fta_per_36_min',
                                                          'orb_per_36_min','drb_per_36_min','trb_per_36_min',
                                                          'ast_per_36_min','stl_per_36_min','blk_per_36_min',
                                                          'tov_per_36_min','pf_per_36_min','pts_per_36_min'],'float')
        df_Per_36_Minutes = drop_columns(df_Per_36_Minutes,['birth_year'])
    print("Player per 36 Minutes TRANSFORMED")
    insert_data(df_Per_36_Minutes,"per_36_minutes")
    print("Player per 36 Minutes LOADED")

    if player_per_game == True:
        df_Player_Per_Game = getkaggle_data('Player Per Game.csv')
        df_Player_Per_Game = replace_na(df_Player_Per_Game,['gs','mp_per_game','fg_percent',
                                                            'x3p_per_game','x3pa_per_game','x3p_percent',
                                                            'x2p_percent','e_fg_percent','ft_percent',
                                                            'orb_per_game','drb_per_game','trb_per_game',
                                                            'ast_per_game','stl_per_game','blk_per_game',
                                                            'tov_per_game','pf_per_game'],'float')
        df_Player_Per_Game = drop_columns(df_Player_Per_Game,['birth_year'])
    print("Player per Game TRANSFORMED")
    insert_data(df_Player_Per_Game,"player_per_game")
    print("Player per Game LOADED")

    if player_play_by_play == True:
        df_Player_Play_By_Play = getkaggle_data('Player Play By Play.csv')
        print("Player Play by Play EXTRACTED")
        df_Player_Play_By_Play = replace_na(df_Player_Play_By_Play,['pg_percent','sg_percent','sf_percent','pf_percent','c_percent','offensive_foul_drawn'],'float')
        df_Player_Play_By_Play = drop_columns(df_Player_Play_By_Play,['birth_year'])
        print("Player Play by Play TRANSFORMED")
        insert_data(df_Player_Play_By_Play,"player_play_by_play")
        print("Player Play by Play LOADED")

    if player_season_info == True:
        df_Player_Season_Info = getkaggle_data('Player Season Info.csv')
        df_Player_Season_Info = drop_columns(df_Player_Season_Info,['birth_year'])
        print("Player Season Info TRANSFORMED")
        insert_data(df_Player_Season_Info,"player_season_info")
        print("Player Season Info LOADED")

    if player_shooting == True:
        df_Player_Shooting = getkaggle_data('Player Shooting.csv')
        df_Player_Shooting = replace_na(df_Player_Shooting,['percent_fga_from_x2p_range','percent_fga_from_x0_3_range','percent_fga_from_x3_10_range',
                                                            'percent_fga_from_x10_16_range','percent_fga_from_x16_3p_range','percent_fga_from_x3p_range',
                                                            'fg_percent_from_x2p_range','fg_percent_from_x0_3_range','fg_percent_from_x3_10_range',
                                                            'fg_percent_from_x10_16_range','fg_percent_from_x16_3p_range','fg_percent_from_x3p_range',
                                                            'percent_assisted_x2p_fg','percent_assisted_x3p_fg','percent_dunks_of_fga','num_of_dunks',
                                                            'percent_corner_3s_of_3pa','corner_3_point_percent','num_heaves_attempted','num_heaves_made'],'float')
        df_Player_Shooting = drop_columns(df_Player_Shooting,['birth_year'])
        print("Player Shooting TRANSFORMED")
        insert_data(df_Player_Shooting,"player_shooting")
        print("Player Shooting LOADED")

    if player_totals == True:
        df_Player_Totals = getkaggle_data('Player Totals.csv')
        df_Player_Totals = replace_na(df_Player_Totals,['gs','mp',
                                                        'x3p','x3pa','x3p_percent',
                                                        'x2p_percent','e_fg_percent','ft_percent',
                                                        'orb','drb','trb','stl','blk','tov'],'float')
        df_Player_Totals = drop_columns(df_Player_Totals,['birth_year'])
        print("Player Totals TRANSFORMED")
        insert_data(df_Player_Totals,"player_totals")
        print("Player Totals LOADED")
        
    print("Player pipeline completed successfully!")