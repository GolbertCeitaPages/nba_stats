from raw_extract_kaggle_data import getkaggle_data
from raw_transform_nba_data import drop_columns,replace_na,remove_rows,merge_frames,divide_columns
from raw_load_kaggle_data import insert_data

def trigger_award_p(all_star_selections=False,
                    end_of_season_teams_voting=False,
                    end_of_season_teams=False,
                    player_award_shares=False,
                    player_career_info=False,
                    team_abbrev=False):
    
    if all_star_selections == True:
        df_All_Star_Selections = getkaggle_data('All-Star Selections.csv')
        print('All-Star Selections EXTRACTED')
        insert_data(df_All_Star_Selections, "all_star_selections")
        print('All-Star Selections LOADED')

    if end_of_season_teams_voting == True:
        df_End_of_Season_Teams_Voting = getkaggle_data('End of Season Teams (Voting).csv')
        print("End of Season Teams (Voting) EXTRACT")
        df_End_of_Season_Teams_Voting = replace_na(df_End_of_Season_Teams_Voting,['position'],'str')
        df_End_of_Season_Teams_Voting = replace_na(df_End_of_Season_Teams_Voting,['pts_won','pts_max','share','x1st_tm','x2nd_tm','x3rd_tm'],'float')
        print("End of Season Teams (Voting) TRANSFORMED")
        insert_data(df_End_of_Season_Teams_Voting,"end_of_season_teams_voting")
        print("End of Season Teams (Voting) LOADED")

    if end_of_season_teams == True:
        df_End_of_Season_Teams = getkaggle_data('End of Season Teams.csv')
        print("End of Season Teams EXTRACTED")
        df_End_of_Season_Teams = replace_na(df_End_of_Season_Teams,['position'],'str')
        df_End_of_Season_Teams = drop_columns(df_End_of_Season_Teams,['birth_year'])
        print("End of Season Teams TRANSFORMED")
        insert_data(df_End_of_Season_Teams,"end_of_season_teams")
        print("End of Season Teams LOADED")

    if player_award_shares == True:
        df_Player_Award_Shares = getkaggle_data('Player Award Shares.csv')
        print("Player Award Shares EXTRACTED")
        df_Player_Award_Shares = replace_na(df_Player_Award_Shares,['first','pts_won','pts_max','share'],'float')
        print("Player Award Shares TRANSFORMED")
        insert_data(df_Player_Award_Shares,"player_award_shares")
        print("Player Award Shares LOADED")

    if player_career_info == True:
        df_Player_Career_Info = getkaggle_data('Player Career Info.csv')
        print("Player Career Info EXTRACTED")
        df_Player_Directory = getkaggle_data('Player Directory.csv')
        print("Player Directory EXTRACTED")
        df_Player_Career_Info = merge_frames(df_Player_Career_Info,df_Player_Directory,['player','first_seas','last_seas'],['player','from','to'])
        df_Player_Career_Info = drop_columns(df_Player_Career_Info,['birth_year','from','to','hof_y'])
        df_Player_Career_Info = replace_na(df_Player_Career_Info,['ht_in_in','wt'],'float')
        df_Player_Career_Info = replace_na(df_Player_Career_Info,['birth_date','colleges','slug'])
        # Rename column for consistancy
        df_Player_Career_Info = df_Player_Career_Info.rename(columns={'hof_x':'hof'})
        print("Player Career Info TRANSFORMED")
        insert_data(df_Player_Career_Info,"player_career_info")
        print("Player Career Info LOADED")

    if team_abbrev == True:
        df_Team_Abbrev = getkaggle_data('Team Abbrev.csv')
        print("Team Abbrev EXTRACTED")
        df_Team_Abbrev = replace_na(df_Team_Abbrev,['abbreviation'])
        print("Team Abbrev TRANSFORMED")
        insert_data(df_Team_Abbrev,"team_abbrev")
        print("Team Abbrev LOADED")
    print("Pipeline completed successfully!")